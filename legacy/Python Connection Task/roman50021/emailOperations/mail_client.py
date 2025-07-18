import os
import ssl
import smtplib
import imaplib
import email
from email.message import EmailMessage
from datetime import datetime
from pathlib import Path
from typing import Final, Optional, List
import logging
from dotenv import load_dotenv

# ────────────────────── Downloading the configuration ──────────────────────
BASE_DIR = Path(__file__).parent
env_file = BASE_DIR / "file2.env"
print("Looking for .env at:", env_file)

load_dotenv(dotenv_path=env_file, override=True)

print("DEBUG ENV:", os.environ.get("EMAIL_LOGIN"))

def _env(key: str, default: str | None = None) -> str:
    val = os.getenv(key, default)
    if val is None:
        raise RuntimeError(f"Environment variable {key} is required but missing")
    return val

SMTP_HOST: Final[str] = _env("SMTP_HOST", "127.0.0.1")
SMTP_PORT: Final[int] = int(_env("SMTP_PORT", "25"))

IMAP_HOST: Final[str] = _env("IMAP_HOST", SMTP_HOST)
IMAP_PORT: Final[int] = int(_env("IMAP_PORT", "993"))

LOGIN: Final[str] = _env("EMAIL_LOGIN")
PASSWORD: Final[str] = _env("EMAIL_PASSWORD")
DOMAIN: Final[str] = _env("DOMAIN", "localhost")

FROM_ADDR: Final[str] = f"{LOGIN}@{DOMAIN}"
TO_ADDR: Final[str] = _env("TO_ADDR", FROM_ADDR)

TLS_VERIFY: Final[bool] = _env("TLS_VERIFY", "false").lower() == "true"

# ────────────────────── Logging settings ──────────────────────
logging.basicConfig(
    format="%(levelname)s: %(message)s",
    level=logging.INFO,
    force=True,
)
log = logging.getLogger(__name__)

# ────────────────────── SSL context ──────────────────────
def _ssl_ctx() -> ssl.SSLContext:
    if TLS_VERIFY:
        ctx = ssl.create_default_context()
        cafile = os.getenv("IMAP_CAFILE")
        if cafile and Path(cafile).is_file():
            ctx.load_verify_locations(cafile)
        return ctx
    return ssl._create_unverified_context()  # без перевірки сертифікату

# ────────────────────── Sending a letter ──────────────────────
def send_letter(subject: Optional[str] = None, body: Optional[str] = None) -> None:
    msg = EmailMessage()
    msg["From"] = FROM_ADDR
    msg["To"] = TO_ADDR
    msg["Subject"] = subject or f"Test {datetime.now():%Y-%m-%d %H:%M:%S}"
    msg.set_content(body or "Привіт! Це лист, надісланий скриптом Python")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
        smtp.set_debuglevel(1)
        smtp.ehlo()
        smtp.starttls(context=_ssl_ctx())
        smtp.ehlo()
        smtp.send_message(msg) # login не потрібен
    log.info("Letter sent to %s", TO_ADDR)

# ────────────────────── Receiving emails ──────────────────────
def _decode_header(raw_header: str | None) -> str:
    from email.header import decode_header

    if raw_header is None:
        return ""
    parts = decode_header(raw_header)
    return "".join(
        part.decode(enc or "utf-8") if isinstance(part, bytes) else part for part, enc in parts
    )

def fetch_my_letters(limit: int | None = None) -> List[email.message.EmailMessage]:
    ctx = _ssl_ctx()
    result: List[email.message.EmailMessage] = []

    with imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT, ssl_context=ctx) as imap:
        imap.login(LOGIN, PASSWORD)
        imap.select("INBOX")
        typ, data = imap.search(None, f'FROM "{FROM_ADDR}"')
        ids = data[0].split()
        if limit:
            ids = ids[-limit:]

        log.info("Inbox: %d message(s) from %s", len(ids), FROM_ADDR)

        for num in ids:
            typ, msg_data = imap.fetch(num, "(RFC822)")
            raw = msg_data[0][1]
            msg = email.message_from_bytes(raw)
            log.info("  — #%s: %s", num.decode(), _decode_header(msg["Subject"]))
            result.append(msg)
        imap.logout()
    return result

# ────────────────────── Main entry point ──────────────────────
if __name__ == "__main__":
    log.info("DEBUG → SMTP %s:%s  IMAP %s:%s  user=%s  TLS_VERIFY=%s",
             SMTP_HOST, SMTP_PORT, IMAP_HOST, IMAP_PORT, LOGIN, TLS_VERIFY)

    send_letter()
    fetch_my_letters(limit=10)