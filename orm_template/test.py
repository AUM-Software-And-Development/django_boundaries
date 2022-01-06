# Django settings
import inspect
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from django.db import connection
# Reads the settings
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Imports classes from the programmed application files:
# standalone\models.py->+Test
from standalone.models import Test

# Restore test to an uninitialized state
def restore_null():
    Test.objects.all().delete()

# Start the model setup test cases
def model_setup():
    try:
        restore_null()
        test = Test(name="name")
        test.save()
        # Check the count of the table:
        assert Test.objects.count() > 0
        print('The model test ran with no errors.')
    except AssertionError as exception:
        print('The model test produced this error: ')
        raise (exception)
    except:
        # !Important # If the Postgres password is wrong, this will print
        print('An uncaught error has occurred. Please refer to standalone\models.py->+Test')

model_setup()