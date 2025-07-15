# ⚙️ CentOS Script Repository for UA-1378 TAQC Students

This readme is written to help setup CentOS virtual machine up to TC09 Email From Blacklisted Sender requirement

---

## Setup

Create file with list of blocked sender:
```cmd
sudo nano /etc/postfix/sender_access
```

---

Enter spam sender email:
```cmd
spam_sender@example.com    REJECT
```
---

Compile file into Postifx DB format:
```cmd
sudo postmap /etc/postfix/sender_access
```
That creates /etc/postfix/sender_access.db.

---

Then open main.cf:
```cmd
sudo nano /etc/postfix/main.cf
```
and add:
```cmd
smtpd_sender_restrictions = check_sender_access hash:/etc/postfix/sender_access, permit
```
That rule gonna check sender by sender_access. If he in list, will block him.

---

Restart Postfix:
```cmd
sudo systemctl restart postfix
```
---

---

Don`t forget to add SPAM_SENDER variable to .env file.
```cmd
SPAM_SENDER = "spam_sender@example.com"
```

---

That short tutorial will make TC09 Email From Blacklisted Sender work correctly.
