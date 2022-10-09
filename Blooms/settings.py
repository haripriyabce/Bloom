"""
Django settings for Blooms project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+uhymlv45lcdhk3bp%4ugk9xj07#@u0ci_7)++e6p=x&14mcw!'

#SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'admin_p',
    'category',
    'cart',
    'order',
    'content',
    'user_profile',
    'mathfilters',
    'product',
    'user_sec',
    'crispy_forms',
    'debug_toolbar',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Blooms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Blooms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if not DEBUG:
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
        #   'NAME': os.environ.get('NAME'),
        #   'USER': os.environ.get('USER'),
        #   'PASSWORD': os.environ.get('PASSWORD'),
        #   'HOST': os.environ.get('HOST'),
        #   'PORT':  os.environ.get('PORT'),
            'NAME':'myblooms',
            'USER':'bloomuser',
            'PASSWORD':'bloompass',
            'HOST':'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',       
            'NAME':'ne_bloom',
            'USER':'postgres',
            'PASSWORD':'password',
            'HOST':'localhost',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = 'ims/'
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
else:
    STATIC_ROOT=''
    
RAZORPAY_KEY_ID='rzp_test_CLJZAjlkyL5HrW'
RAZORPAY_KEY_SECRET='QCaYdk2SVhSH9aQPbShWNmtB'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/ims')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
INTERNAL_IPS = [
    "127.0.0.1",
]
if not DEBUG:
    
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# if ENVIRONMENT == 'production':
#    SECURE_BROWSER_XSS_FILTER = True
#    X_FRAME_OPTIONS = 'DENY'
#    SECURE_SSL_REDIRECT = True
#    SECURE_HSTS_SECONDS = 3600
#    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#    SECURE_HSTS_PRELOAD = True
#    SECURE_CONTENT_TYPE_NOSNIFF = True
#    SESSION_COOKIE_SECURE = True 
#    CSRF_COOKIE_SECURE = True 
#    SECURE_REFERRER_POLICY = 'same-origin'