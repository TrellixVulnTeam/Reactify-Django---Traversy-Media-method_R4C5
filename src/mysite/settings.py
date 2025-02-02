"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gjkdr#j44i@5w!#ce=c+&cf66b*(pw8($79@6%h37((3e0)1uz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'corsheaders', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 

    'crispy_forms',
    'sslserver',
    'oauth2_provider',

    'rest_framework',
    'rest_framework.authtoken',

    'allauth', 
    'allauth.account',
    'allauth.socialaccount.providers.google',

    'rest_auth',
    'rest_auth.registration',

    'chatterbot',
    'chatterbot.ext.django_chatterbot',

    'frontend',
    'core',
    
]

CHATTERBOT = {
    'name': 'Charlie',
    # 'django_app_name':'django_chatterbot',
    # 'logic_adapters': [
    #     'chatterbot.logic.MathematicalEvaluation',
    #     'chatterbot.logic.TimeLogicAdapter',
    #     'chatterbot.logic.BestMatch'
    # ],
    # 'storage_adapter':'chatterbot.storage.SQLStorageAdapter',
    'storage_adapter':'chatterbot.storage.SQLStorageAdapter',
    'database_uri':'sqlite:///db.sqlite3',
    # 'read_only':True
}

REACT_ROUTES = [
    'inbox',
    'search',
    'settings',
    'password-reset',
    'password-change',
    'about',
]

SITE_ID = 2

# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
SESSION_SAVE_EVERY_REQUEST =True
SESSION_COOKIE_AGE=1209
# SESSION_CACHE_ALIAS = "default"
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30  # One month (defined in seconds)

AUTH_PROFILE_MODULE = 'core.profile'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 100

# LOGIN_REDIRECT_URL = '/post/'
# LOGOUT_REDIRECT_URL='account_login'
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # 1 day
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = False

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.AllowAllUsersModelBackend',
    'django.contrib.auth.backends.AllowAllUsersRemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend', 
    'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'mysite.middleware.AddHeadersAPIMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', 
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'), 
]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static-cdn-local')


# CORS_URLS_REGEX = r'^/api.*'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False 
# CORS_ORIGIN_WHITELIST = [ 
#     'http://dms.com:8000',
#     'http://dms.com:3000',
#     'http://localhost:8000', 
#     'http://localhost:3000', 
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:3000',
#     'http://192.168.0.100:3000',
#     'https://dms.com:8000',
#     'https://dms.com:3000',
#     'https://localhost:8000', 
#     'https://localhost:3000', 
#     'https://127.0.0.1:8000',
#     'https://127.0.0.1:3000',
#     'https://192.168.0.100:3000'
# ]
# CORS_ALLOW_HEADERS = [
  
#     'cookie',
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

CRISPY_TEMPLATE_PACK = 'bootstrap4'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_AUTHENTICATION_METHOD = ('username' | 'email') # (="username" | "email" | "username_email)
EMAIL_VERIFICATION = 'mandatory'
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'core.api.serializers.LoginSerializer',
    'TOKEN_SERIALIZER': 'core.api.serializers.TokenSerializer',
    'PASSWORD_RESET_SERIALIZER': 'core.api.serializers.PasswordResetSerializer',
    'PASSWORD_RESET_CONFIRM_SERIALIZER': 'core.api.serializers.PasswordResetConfirmSerializer',
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

ACCESS_TOKEN_EXPIRE_SECONDS=315569520
OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'ACCESS_TOKEN_EXPIRE_SECONDS': 315569520,
}



# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # mail service smtp
EMAIL_HOST_USER = 'dms24081999@gmail.com'  # email id
EMAIL_HOST_PASSWORD = 'hpeytpfcstxsdenv'  # password
EMAIL_PORT = 587
EMAIL_USE_TLS = True

