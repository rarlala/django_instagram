import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# instagram/
ROOT_DIR = os.path.dirname(BASE_DIR)
JSON_FILE = os.path.join(ROOT_DIR, 'secrets.json')

SECRETS = json.load(open(JSON_FILE))
# try : SECRETS = json.load(open(JSON_FILE))
# except :
#     SECRETS = {
#         'AWS_ACCESS_KEY_ID': os.environ.get('AWS_ACCESS_KEY_ID'),
#         'AWS_SECRET_ACCESS_KEY': os.environ.get('AWS_SECRET_ACCESS_KEY'),
#         "client_id": "BSGbrKFgPs7p0wZLG3nY",
#         "client_secret": "cy77SSUoKr",
#         "DATABASES": {
#             "default": {
#                 "ENGINE": "django.db.backends.postgresql",
#                 "NAME": "instagram",
#                 "USER": "jsj",
#                 "PASSWORD": "Jsuji192625!",
#                 "HOST": "wps-jsj.cem8vmssrn1f.ap-northeast-2.rds.amazonaws.com",
#                 "PORT":"5432"
#             }
#           }
#     }

json_data = SECRETS

# django-secrets-manager의 SECRETS를 사용해서 비밀 값 할당
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']

# django-storages | AWS S3
AWS_STORAGE_BUCKET_NAME = 'wps-instagram-jsj'
AWS_DEFAULT_ACL = 'private'
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_REGION_NAME = 'ap-northeast-2'

DEBUG = True
SECRET_KEY = 'l4ux!g)8(18*h)02j*j)y-+@cy$_l-q$4%1b_#i3++(#+5nr$l'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
# 정적파일 설정 추가
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
# 각 application들의 static/폴더, STATICFILES_DIRS의 폴더들이 가진 정적파일들을 모을 폴더
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_URL = '/static/'

# instagram/.media
# User-uploaded static files의 기본 경로
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

# django-storages
# Django의 FileStorage로 S3Boto3Storage(AWS의 S3)를 사용
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '172.16.1.116',
    '*',
]
AUTH_USER_MODEL = 'members.User'

# Application definition

INSTALLED_APPS = [
    'members.apps.MembersConfig',
    'posts.apps.PostsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
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
            # os.path.join(BASE_DIR, 'templates'),
            TEMPLATES_DIR,
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
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = SECRETS['DATABASES']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True