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
5. Create the two necessary python files with `touch models.py app.py`
6. After setting up at least one model, we need to modify the env.py inside the migrations folder and update the target_metadata

```py
from models import Base
target_metadata = Base.metadata
```

## Handling Migrations

- To generate a migration file we run `alembic revision --autogenerate -m "The message"`
- To apply the migration, we run `alembic upgrade head`
