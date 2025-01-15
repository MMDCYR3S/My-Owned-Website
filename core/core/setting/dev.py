from core.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(ngrmex$$^y(#5a6w2d_r_kk^0y84gryhisqq_1rf6+bj+e39f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["cyr3s.pythonanywhere.com"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Define Site ID(Site Framework)
SITE_ID = 1

# STATIC And MEDIA ROOTS
# If the direction os static root has changed,
# you can use STATICFILES_DIRS.
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

MEDIA_ROOT = BASE_DIR / 'media'

# X-Frame Options Set
X_FRAME_OPTIONS = "SAMEORIGIN"