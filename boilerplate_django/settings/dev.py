from .base import *

DEBUG = True

INSTALLED_APPS += [
    'django_nose',
	'faker',
	'model_mommy',
]

if DEBUG:
    def show_toolbar(request):
    	return True

    DEBUG_TOOLBAR_CONFIG = {
    	"SHOW_TOOLBAR_CALLBACK" : show_toolbar,
    }

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
    	'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

# Test runner required for Django Unit Testing
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# running tests will also run coverage + only include the apps listed below.
# inclusive will scan all files in working dir to see which are not being covered
NOSE_ARGS = [
	'--verbosity=2',
	'--with-coverage',
	'--cover-package=boilerplate_django',
	'--cover-inclusive',
	'--nocapture',
]

# settings.LANGUAGE_CODE is loaded
FAKER_LOCALE = None
# faker.DEFAULT_PROVIDERS is loaded (all)
FAKER_PROVIDERS = None

ALLOWED_HOSTS += ['localhost']
