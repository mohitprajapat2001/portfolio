from pathlib import Path
from os.path import join
from utils.constants import Settings, EmailConfig
from dotenv import dotenv_values

env = dotenv_values(".env")

# BASE Directory Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Project Secret Key
SECRET_KEY = env.get("SECRET_KEY", "")

APPEND_SLASH = True

# AUTH User Model
AUTH_USER_MODEL = "aboutme.Profile"

# Cities Light
CITIES_LIGHT_INCLUDE_COUNTRIES = ["IN"]

ROOT_URLCONF = Settings.ROOT_URLCONF

LANGUAGE_CODE = Settings.LANGUAGE_CODE

USE_TZ = True

LANGUAGES = [
    ("en", "English"),
    ("hi", "Hindi"),
]
LOCALE_PATHS = [
    join(BASE_DIR, "locale"),
]

TIME_ZONE = Settings.TIME_ZONE

USE_I18N = Settings.USE_I18N


USE_TZ = Settings.USE_TZ
DEFAULT_AUTO_FIELD = Settings.DEFAULT_AUTO_FIELD

# Web Server Gateway Interface
WSGI_APPLICATION = Settings.WSGI_APPLICATION

# Email Configuration
EMAIL_BACKEND = EmailConfig.EMAIL_BACKEND
EMAIL_HOST = EmailConfig.EMAIL_HOST
EMAIL_USE_SSL = True  # use port 465
EMAIL_USE_TLS = False  # use port 587
EMAIL_PORT = EmailConfig.PORT_465 if EMAIL_USE_SSL else EmailConfig.PORT_587
EMAIL_HOST_USER = env.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = env.get("EMAIL_HOST_PASSWORD", "")

# Fixtures Directories
ADDRESS_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "address.json")
COMPANY_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "company.json")
EXPERIENCE_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "experience.json")
PROJECT_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "project.json")
SKILLS_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "skills.json")
TECHNOLOGY_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "technologies.json")
PROFILE_FIXTURE_DIRS = join(BASE_DIR, "aboutme", "fixtures", "profile.json")

# Superuser Credentials
SUPERUSER_USERNAME = env.get("SUPERUSER_USERNAME", "admin")
SUPERUSER_EMAIL = env.get("SUPERUSER_EMAIL", "admin@example.com")
SUPERUSER_PASSWORD = env.get("SUPERUSER_PASSWORD", "Admin123")

# User Default Password
USER_PASSWORD = env.get("USER_PASSWORD", "User123")
