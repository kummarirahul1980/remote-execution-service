
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e%ljemx0o6*j5ye#qu@*^kp+n#u%7-)3&9wjx3@nth71v%8f!c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'watch'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'android.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'android.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

MESSAGE_MANAGER = {}
MESSAGE_MANAGER["CREDENTIAL_MANAGER"] = {}
MESSAGE_MANAGER["CREDENTIAL_MANAGER"]["KEY"] = "chaduvuko_first"
MESSAGE_MANAGER["CREDENTIAL_MANAGER"]["username_alias"] = "password"
MESSAGE_MANAGER["CREDENTIAL_MANAGER"]["password_alias"] = "night_changes"
MESSAGE_MANAGER["EXECUTION_MANAGER"] = {}
MESSAGE_MANAGER["EXECUTION_MANAGER"]["KEY"] = "neekenduku_exec"
MESSAGE_MANAGER["EXECUTION_MANAGER"]["command_key"]="command"
MESSAGE_MANAGER["EXECUTION_MANAGER"]["command_key"]="command"
MESSAGE_MANAGER["EXECUTION_MANAGER"]["argument_list_key"]  = "args"
from datetime import datetime
from pathlib import Path


def write_log(log_string: str , *args):
    log_file = Path(BASE_DIR) / "android.log"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with log_file.open("a", encoding="utf-8") as f:
        f.write(
            f"{timestamp}\n"
            f"{log_string}\n\n"
        )



DEVELOPER_MODE:bool = FALSE