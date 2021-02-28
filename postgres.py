from db_config import DBConfig


class Postgres:

    @staticmethod
    def execute(query: str):
        with DBConfig().load.connect() as conn:
            return conn.execute(query).fetchall()
