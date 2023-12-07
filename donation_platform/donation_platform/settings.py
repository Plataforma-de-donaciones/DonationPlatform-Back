"""
Django settings for donation_platform project.

Generated by 'django-admin startproject' using Django 3.2.20.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'donation_platform',
    'users',
    'administrator',
    'moderator',
    'organization',
    'articles_states',
    'articles_types',
    'articles_zones',
    'donation',
    'event',
    'medical_equipment',
    'news',
    'sponsor',
    'volunteer',
    'notifications',
    'request',
    'categories_meq',
    'categories',
    'categories_don',
    'conversation',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Almacenar sesiones en la base de datos (también puedes usar 'django.contrib.sessions.backends.cache' o 'django.contrib.sessions.backends.file')
#SESSION_COOKIE_NAME = 'donation_cookie'

ROOT_URLCONF = 'donation_platform.urls'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}
AUTH_USER_MODEL = 'users.Users'
#SESSION_COOKIE_SECURE = False
#CSRF_COOKIE_SECURE = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = None  # o 'Lax' o 'Strict'
CSRF_COOKIE_SAMESITE = None  # o 'Lax' o 'Strict'
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True



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

WSGI_APPLICATION = 'donation_platform.wsgi.application'
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://localhost:3000",
    "http://localhost:3000",
  # Reemplaza con la URL de tu aplicación React
]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': {
                  'ENGINE': 'django.db.backends.postgresql_psycopg2',
                   'NAME': env('POSTGRESQL_NAME'),
                   'USER': env('POSTGRESQL_USER'),
                   'PASSWORD': env('POSTGRESQL_PASS'),
                   'HOST': env('POSTGRESQL_HOST'),
                   'PORT': env('POSTGRESQL_PORT'),
                   'OPTIONS': {
                       'options': '-c search_path=data',  # Especificar el esquema
              },
         }
  } 

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',

            'filename': os.path.join(BASE_DIR, 'django.log/'),
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-uy'

DEFAULT_CHARSET = 'utf-8'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

SERVER_URL = "https://plataformadonaciones-qa.azurewebsites.net"
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]
DEBUG = True
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
