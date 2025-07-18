import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.yml"


def load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)


config = load_config()

BASE_URL: str = config["base_url"]
ADMIN_USERNAME: str = config["admin_username"]
ADMIN_PASSWORD: str = config["admin_password"]
TIMEOUT_SECONDS: int = config["timeout_seconds"]
