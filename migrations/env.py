import os
import logging
from logging.config import fileConfig
from flask import current_app
from alembic import context
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access the Alembic Config object
config = context.config

# Force the sqlalchemy.url to use DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Interpret the config file for Python logging
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

# Import app and db to load models
from app import db
target_metadata = db.metadata  # Set the metadata for model detection


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = db.engine  # Use SQLAlchemy's engine

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

