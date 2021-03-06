"""
Django settings for instagram project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# instagram_project/instagram/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# instagram_project/
ROOT_DIR = os.path.dirname(BASE_DIR)
# instagram_project/.config_secret/
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')

# 1. CONFIG_SECRET_DIR 내의 'setting_common.json' 파일을 읽고,
# 그 결과를 config_secret_common_str 변수에 할당
# 2. json.loads(<json string>) 함수를 호출해서 JSON텍스트 파일의 내용을
# Python dict형태로 변환, config_secret_common변수에 할당
# 3. config_secret_common dict변수의 django > secret_key에
# 해당하는 value를 SECRET_KEY 변수에 할당
# 4. .gitignore에 .config_secret/ 폴더를 추가

# 1.
f = open(os.path.join(CONFIG_SECRET_DIR, 'settings_common.json'))
config_secret_common_str = f.read()
# 2.
config_secret_common = json.loads(config_secret_common_str)
# 3.
SECRET_KEY = config_secret_common['django']['secret_key']

# Facebook
FACEBOOK_APP_ID = config_secret_common['facebook']['app_id']
FACEBOOK_APP_SECRET_CODE = config_secret_common['facebook']['secret_code']
FACEBOOK_SCOPE = ['user_friends', 'public_profile', 'email']

# static의 경우 url부분에서 STATIC_URL, STATICFILES_DIRS가 생략되어있다고 생각하면 됨
STATIC_URL = '/static/'
# instagram_project/instagram/static => 이는 custom 변수이고
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATIC_URL로의 요청은 STATICFILES_DIRS 경로의 목록에서 파일을 찾아 리턴
STATICFILES_DIRS = [
    STATIC_DIR,
]
# instagram_project/instagram/media/ => 이는 django 내부에서 사용하는 변수
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# instagram_project/instagram/templates
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

AUTH_USER_MODEL = 'member.User'

REST_FRAMEWORK = {
    # DRF Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

# 기본 인증 백엔드에 페이스북 인증 백엔드를 추가함
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'member.backends.FacebookBackend',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party package
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',

    # Custom
    'member',
    'post',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
        ],
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

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = config_secret_common['django']['databases']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True
