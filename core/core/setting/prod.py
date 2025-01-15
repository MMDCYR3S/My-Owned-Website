from core.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(ngrmex$$^y(#5a6w2d_r_kk^0y84gryhisqq_1rf6+bj+e39f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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

#
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend")
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Define CSRF Cookie Secure
CSRF_COOKIE_SECURE = True
