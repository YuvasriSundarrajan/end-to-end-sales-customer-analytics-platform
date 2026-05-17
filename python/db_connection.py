import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    user = "root"
    host = "localhost"
    port = 3306
    database = "sales_analytics"

    raw_password = os.getenv("MYSQL_PASSWORD")
    if not raw_password:
        raise ValueError("MYSQL_PASSWORD not found")

    password = quote_plus(raw_password)

    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    return engine
