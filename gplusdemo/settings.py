# Django settings for gplusdemo project.
import os

PROJECT_PATH  = os.path.abspath(os.path.dirname(__file__))
INSTANCE_NAME = os.path.basename(PROJECT_PATH)
DATABASE_NAME = "testdb.sqlite3"  # Change this."
SECRET_KEY    = "u!z4gemxjq0zgu5acng7-nvfs4283on*klxfp8eqe4rxuj!o7"
CACHE_LOCATION = "/tmp/gplusacts_%s" % INSTANCE_NAME

GPLUSACTS_POSTS_PER_PAGE = 5
GPLUSACTS_TITLE = "My Google+ Activities"

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_PATH, DATABASE_NAME),
    }
}
ALLOWED_HOSTS = []
# PREPEND_WWW = True
TIME_ZONE = 'Asia/Manila'
LANGUAGE_CODE = 'en-ph'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Media and Static.
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = PROJECT_PATH
STATIC_URL = "/static/"
# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
ROOT_URLCONF = "%s.urls" % INSTANCE_NAME
WSGI_APPLICATION = "%s.wsgi.application" % INSTANCE_NAME
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'gplusacts',   # But of course!
)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": CACHE_LOCATION,
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
