import os
from configparser import ConfigParser, NoSectionError, NoOptionError
from pathlib import Path

_BASE_DIR = Path(__file__).resolve().parent.parent

_config = ConfigParser()
_config.read(_BASE_DIR / "config.ini", encoding="utf-8")


def get_value(key: str, section: str = "default") -> str:
    """
    looks for value from config.ini trying following locations: config.ini, environment variables
    throws KeyError if value is not found anywhere

    Arguments:
        key (str)
        section (str): used only for config.ini
    """
    try:
        return _config.get(section, key)
    except (NoSectionError, NoOptionError):
        return os.environ[key]
