## Torque & Lustre API Inventory

## Description

- This is the Backend that powers our Torque and Lustre Inventory API.
- We use fastapi as the framework and sqlalchemy for Database management.
- At the beginning, we will use sqlite and if we host the application , we will switch to postgres.

## Project Setup

1. Install the required packages with `pipenv install sqlalchemy alembic "fastapi[standard]"`
2. Activate the virtual environment with `pipenv shell`
3. Initialize migrations with the command `alembic init migrations`.
   _We only run this command once_
4. Update the alembic.ini file and set sqlalchemy.url to whatever the database should be i.e `sqlite:///TorqueandLustre.db`
