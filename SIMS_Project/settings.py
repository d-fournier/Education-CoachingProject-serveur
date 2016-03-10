"""
Django settings for SIMS_Project project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
DEFAULT_KEY = 'c=#a@6ph&-w-v61bbw(m9ini*rjbx4%7jp-!5=!!2uhl)d3_8x'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', DEFAULT_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
debugValue = os.environ.get('DJANGO_DEBUG', 'True')
DEBUG = debugValue == 'True'

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
    'auth_djoser',
    'user',
    'level',
    'sport',
    'message',
    'relation',
    'group',
    'device',
    'requests',
    'blog'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SIMS_Project.urls'

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

WSGI_APPLICATION = 'SIMS_Project.wsgi.application'


 # Database
  # https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASE_TYPE = os.environ.get('DJANGO_DATABASE_TYPE', 'SQLITE3')
if DATABASE_TYPE == 'SQLITE3':
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif DATABASE_TYPE == 'POSTGRES':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Serve static files with Heroku
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
 os.path.join(BASE_DIR, 'static'),
)

# Check if AmazonS3 is enable
awsS3AccessKeyId = os.environ.get('AWS_S3_ACCESS_KEY_ID', '')
awsS3SecretAccessKey = os.environ.get('AWS_S3_SECRET_ACCESS_KEY', '')
awsS3BucketName = os.environ.get('AWS_S3_BUCKET_NAME', '')

AWS_ACTIVATED = False

if awsS3AccessKeyId and awsS3SecretAccessKey and awsS3BucketName:
    AWS_ACTIVATED = True
    AWS_QUERYSTRING_AUTH = False
    INSTALLED_APPS = INSTALLED_APPS + ['storages']
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_STORAGE_BUCKET_NAME = awsS3BucketName
    AWS_S3_ACCESS_KEY_ID = awsS3AccessKeyId
    AWS_S3_SECRET_ACCESS_KEY = awsS3SecretAccessKey
else:
    MEDIA_ROOT = 'media'
    MEDIA_URL ='/media/'

### HEROKU config
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Add Log to Heroku
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
        }
    }
}


### GCM config for Cloud Messaging
GCM_ACTIVATED = False
# GCM_API_KEY = os.environ.get('GCM_API_KEY','')
GCM_API_KEY = 'AIzaSyBjRzHw3ineF7H5xX38kezDVdtfSW4_5ms'

if GCM_API_KEY:
    GCM_ACTIVATED = True
