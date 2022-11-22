import glob
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))

CUSTOM_INSTALLED_APPS = (
    'monitoring',
)

ALWAYS_INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

ALWAYS_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

settings.configure(
    SECRET_KEY="django_tests_secret_key",
    BASE_URL="http://localhost:8000",
    DEBUG=False,
    TEST_MODE=True,
    TEMPLATE_DEBUG=False,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=ALWAYS_INSTALLED_APPS + CUSTOM_INSTALLED_APPS,
    MIDDLEWARE_CLASSES=ALWAYS_MIDDLEWARE_CLASSES,
    ROOT_URLCONF='tests.urls',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'monitoring-db',
        }
    },
    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,
    STATIC_URL='/static/',
    # Use a fast hasher to speed up tests.
    PASSWORD_HASHERS=(
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ),
    FIXTURE_DIRS=glob.glob(BASE_DIR + '/' + '*/fixtures/'),
    TEMPLATES=[
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
    ],
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
    PLUGINS={
        'MONITORING_SOURCES': {
            'INSTALLED': [
                'SQL_QUERY_V1',
                'SQL_SAGE_GATEWAY_V1',
                'NOT_SUCCESS_V1',
            ]
        }
    }
)

django.setup()

if len(sys.argv) <= 1:
    print('use test or makemigrations')
    exit(1)

if sys.argv[1] == "test":
    args = [sys.argv[0], 'test']
    # Current module (``tests``) and its submodules.
    test_cases = '.'

    # Allow accessing test options from the command line.
    offset = 2
    try:
        sys.argv[2]
    except IndexError:
        pass
    else:
        option = sys.argv[2].startswith('-')
        if not option:
            test_cases = sys.argv[2]
            offset = 3

    args.append(test_cases)
    # ``verbosity`` can be overwritten from command line.
    args.append('--verbosity=2')
    args.extend(sys.argv[offset:])
    execute_from_command_line(args)
elif sys.argv[1] == "makemigrations":
    args = sys.argv[:1] + ["makemigrations", "monitoring"]
    execute_from_command_line(args)
