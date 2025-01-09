from __future__ import annotations

import os
import subprocess


os.environ["DJANGO_SETTINGS_MODULE"] = "LibraryProject.settings"
import django  # noqa: E402

django.setup()
from django.contrib.auth.models import User


def create_def_superuser():
    User.objects.create_superuser(username="admin", password="admin", email="admin@example.com")


def prepare_migrations():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    command = f"python3 manage.py makemigrations'"

    print("Running:", command)
    result = subprocess.run(command, shell=True, capture_output=True, cwd=root_dir, text=True)
    print()
    print("OUTPUT:", result.stdout)
    print("ERRORS:", result.stderr)


def run_migrations():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    command = "python3 manage.py migrate"

    print("Running:", command)
    result = subprocess.run(command, shell=True, capture_output=True, cwd=root_dir, text=True)
    print()
    print("OUTPUT:", result.stdout)
    print("ERRORS:", result.stderr)


def populate_db():
    root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    command = f"bash -c 'PYTHONPATH=. python3 tests/populate_db.py'"

    print("Running:", command)
    try:
        result = subprocess.run(command, shell=True, capture_output=True, cwd=root_dir, text=True)

        # Sprawdzanie, czy proces zakończył się niepowodzeniem (returncode różne od 0)
        if result.returncode != 0:
            # Analiza błędów w stderr
            # print("ERROR occurred during the process:")
            # print("stderr:", result.stderr)

            # Jeśli występuje błąd związany z IntegrityError (np. "UNIQUE constraint failed")
            if "UNIQUE constraint failed" in result.stderr:
                print("Most probably Database was already populated with basic data.")
            return None

        # Jeśli proces zakończył się sukcesem, wyświetl stdout
        print("OUTPUT:", result.stdout)

    except subprocess.CalledProcessError as e:
        print("Subprocess failed with exception:", str(e))
        return None

    except Exception as e:
        print("An unexpected exception occurred:", str(e))
        return None


if __name__ == "__main__":
    run_migrations()
    create_def_superuser()
    # prepare_migrations()
    populate_db()
