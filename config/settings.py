# settings.py
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=5j%o4t0pxpbe4h^oizb!ej5vm^+6r3j3z9y-7c8#9$7#aj7+='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

DJANGO_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [

    'apps.users',
    'apps.posts',
    'apps.comments',
    'apps.notification',
    'apps.voting',
    'apps.search',
    'apps.profiles',
]

THIRD_PARTY_APPS = [
    
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'django_filters',
    'rest_framework.authtoken',
    'rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    'allauth.socialaccount.providers.google',
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS




MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

ASGI_APPLICATION = "config.asgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}


DOMAIN = "http://localhost:8000"

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gabrielokemwa83@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_TIMEOUT = 60
EMAIL_USE_LOCALTIME = True

# Email verification settings
EMAIL_VERIFICATION = False
EMAIL_VERIFICATION_AFTER_SIGNUP = False
EMAIL_VERIFICATION_AFTER_PASSWORD_RESET = False

#celery settings

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
CELERY_RESULT_EXTENDED = True
CELERY_DISABLE_RATE_LIMITS = True
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_RESULT_PERSISTENT = True
CELERY_IGNORE_RESULT = False
CELERY_ACCEPT_CONTENT = ["application/json", "application/x-python-serialize"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TASK_DEFAULT_QUEUE = "default"
CELERY_TASK_DEFAULT_ROUTING_KEY = "default"

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

MEDIA_FILE_MAX_AGE = 90

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media" 


# Logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} | {asctime} | {filename} | {funcName} | {lineno} | {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
    },
}


# import cloudinary
# import cloudinary.api
# import cloudinary.uploader

# cloudinary.config(
#     cloud_name="dyae2aocp",
#     api_key="856165385862893",
#     api_secret="bN7eBdQZJo4aZZ0k7uJHbI1e_Rg",
# )

# UPLOAD_PRESET = "sharehub"

# upload_preset_config = {
#     "upload_preset": UPLOAD_PRESET,
#     "cloud_name": "dyae2aocp",
#     "api_key": "856165385862893",
#     "api_secret": "bN7eBdQZJo4aZZ0k7uJHbI1e_Rg",
#     "folder": "sharehub",
#     "resource_type": "auto",
#     "overwrite": True,
#     "notification_url": "https://webhook.site/7d0a6e4a-4d7d-4e6d-8c7d-4e6d8c7d",
#     "tags": "sharehub",
#     "use_filename": True,
#     "unique_filename": False,
#     "eager": [
#         {"width": 300, "height": 300, "crop": "pad", "audio_codec": "none"},
#         {
#             "width": 160,
#             "height": 100,
#             "crop": "crop",
#             "gravity": "south",
#             "audio_codec": "none",
#         },
#     ],
#     "eager_async": True,
#     "eager_notification_url": "https://webhook.site/7d0a6e4a-4d7d-4e6d-8c7d-4e6d8c7d",
#     "type": "upload",
# }