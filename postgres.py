from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_config import DBConfig


class Postgres:

    @staticmethod
    def execute(query: str):
        with DBConfig().load.connect() as conn:
            return conn.execute(query).fetchall()

    @staticmethod
    def init_session():
        session = sessionmaker(DBConfig().init_connection_engine())
        return session()
