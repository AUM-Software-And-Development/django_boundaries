# This script imports django, and initializes the supplementary method for inputing command line instructions.
# It will enable the use of Django commands such as migrations.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                'Django did not import. This may be due to an issue regarding the PYTHONPATH environment variable.\
                 Please ensure that a virtual environment is being utilized.'
            )
        raise
    execute_from_command_line(sys.argv)