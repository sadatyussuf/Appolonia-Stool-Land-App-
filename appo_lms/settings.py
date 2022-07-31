from dotenv import load_dotenv

from pathlib import Path
import os

# Loading environment variables
load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# if os.name == 'nt':
#     VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
#     os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
#     os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h=4fw5xs%jtov)_@jz%a#it7vzq!2^i=-57rg73)n_hv!m9vsr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #My own apps
    'main',   
    'users',
    'bootstrap5',
    'rest_framework_gis',
    'leaflet'
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

ROOT_URLCONF = 'appo_lms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'appo_lms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': DATABASE_NAME ,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD ,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT
    }
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


# Leaflet Configurations
LEAFLET_CONFIG = {

#you can use your own   5.796733790344598, -0.07945842216120023

"DEFAULT_CENTER" : (13.3888599 ,52.5170365),

"DEFAULT_ZOOM" : 15,

"MAX_ZOOM" : 20,

"MIN_ZOOM" : 3,

"DEFAULT_PRECISION": 6,

"SCALE" : 'both',

"ATTRIBUTION_PREFIX" : "My Custom Leaflet map"

}











# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATICFILES_DIR = [
#     os.path.join(BASE_DIR, 'static')
# ]

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GOOGLE_API_KEY = "AIzaSyBf4mB4ZfsTmvktmiT_aCIqbQUcpJpgJSs"
RECAPTCHA_KEY = "6LcD1AQdAAAAAMRxmWIlqSH8xBUHRh_qFP_-G0P3"
RECAPTCHA_SECRET_KEY = "6LcD1AQdAAAAAHRniYjc5khzokVxqiMkdCpft42T"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_URL = "users:sign-in"
# LOGIN_REDIRECT_URL = "users:account"
# LOGOUT_REDIRECT_URL = "users:sign-in"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'





GDAL_LIBRARY_PATH = r'C:\Program Files\QGIS 3.8\bin\gdal204'
GEOS_LIBRARY_PATH = r'C:\Program Files\QGIS 3.8\bin\geos_c.dll'
PROJ_LIBRARY_PATH = r'C:\Program Files\QGIS 3.8\bin\proj'