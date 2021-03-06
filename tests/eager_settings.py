import os
import djcelery
djcelery.setup_loader()

ADMINS = ()
DATABASES = {}


database_implementation = os.getenv('DATABASE', 'sqlite3')

DATABASES['default'] = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_atomic_signals.db',
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'NAME': 'djac',
        'OPTIONS': {
            'autocommit': True,
        },
    },
}[database_implementation]

CELERY_ALWAYS_EAGER = True
BROKER_URL = 'django://'

SECRET_KEY = '_uobce43e5osp8xgzle*yag2_16%y$sf*5(12vfg25hpnxik_*'

INSTALLED_APPS = (
    'djcelery',
    'django_atomic_signals',
    'django_atomic_celery',
    'tests',
    'django_nose',
)

DEBUG = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--verbosity=2', '--detailed-errors', '--rednose']
