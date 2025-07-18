from dotenv import load_dotenv
from robot.api.deco import keyword

@keyword
def load_envs(env_file=None):
    load_dotenv(dotenv_path=env_file) if env_file else load_dotenv()
