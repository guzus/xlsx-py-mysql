import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

USER = os.getenv("DB_USER") or "user"
PASSWD = os.getenv("DB_PASSWORD") or "passwd"
HOST = os.getenv("DB_HOST") or "host"
DB = os.getenv("DB_DATABASE") or "db"

XLSX_FILE_PATH = "./example.xlsx"
XLSX_FILE_SHEET = "Student Info"
XLSX_ROW_RANGE = (3, 7)  # closed interval
XLSX_COLUMN_TO_DB_TABLE_COLUMN = {"B": "name", "C": "phone_number", "D": "email"}

TARGET_DB_TABLE = "example"
