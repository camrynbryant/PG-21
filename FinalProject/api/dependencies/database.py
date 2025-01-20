from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

SQLALCHEMY_DATABASE_URL = (f"mysql+pymysql://{os.getenv('db_user')}:{quote_plus(os.getenv('db_password'))}" +
                           f"@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_name')}" +
                           f"?charset=utf8mb4")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
