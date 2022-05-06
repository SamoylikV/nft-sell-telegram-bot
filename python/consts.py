import os

PSQL_DBNAME = os.getenv('PSQL_DBNAME') or 'postgres'
PSQL_USERNAME = os.getenv('PSQL_USERNAME') or 'postgres'
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD') or 'postgtres'
PSQL_ADDRESS = os.getenv('PSQL_ADDRESS') or 'localhost'
PSQL_PORT = os.getenv('PSQL_PORT') or '5050'

TIMEZONE = 'Asia/Yekaterinburg'
