from pathlib import Path
from dotenv import load_dotenv

def load_env_vars():
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path, override=True)
