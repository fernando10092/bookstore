from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", default="unsafe-secret-key")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="").split(" ")

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("SQL_DATABASE", default=BASE_DIR / "db.sqlite3"),
        "USER": config("SQL_USER", default="user"),
        "PASSWORD": config("SQL_PASSWORD", default="password"),
        "HOST": config("SQL_HOST", default="localhost"),
        "PORT": config("SQL_PORT", default="5432"),
    }
}
