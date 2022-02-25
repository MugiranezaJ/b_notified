"""
Django settings for bnotified project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&#y+&ki7q8&zl2%j*$0=9yl6=wks2heigvue=4jvsq(2^s^z1y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'bnotified.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'webapp',
    "fcm_django"
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

ROOT_URLCONF = 'bnotified.urls'

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

WSGI_APPLICATION = 'bnotified.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jackswalter7@gmail.com'
EMAIL_HOST_PASSWORD = 'fudfrzhthgtuggux'
EMAIL_USE_TLS = True

# Twilio
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TWILIO_ACCOUNT_SID = 'AC693733a262b0f7d59c3aedb6659135c9'
TWILIO_AUTH_TOKEN = '3653b728bdca46876391eb2ae52567b2'
TWILIO_NUMBER = '+19124937137'
SMS_BROADCAST_TO_NUMBERS = [ 
    "", # use the format +19735551234
    "", 
    "", 
]

from firebase_admin import initialize_app
from firebase_admin import credentials
BN_CRED = credentials.Certificate(os.getcwd()+'/bnotified-c05da-036863913602.json')
FIREBASE_APP = initialize_app(BN_CRED)

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAm36ZNzM:APA91bEYW08cAh7P-AZu3IAqNmlMH_6yTSdyVGQsIkFL8yuZB4CFDzRH4LCMR_AdY4U2I66h2ns7HIFxKsHsUNrSnBCsszpkn2vDG-C9aapW9xTlYsO63N_BzlmswJVCX7MWbjinMhDx"
}