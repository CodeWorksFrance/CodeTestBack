import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker, close_all_sessions


class DBConfig:
    _instance = None
    _session = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBConfig, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_session(self):
        if self._session is None:
            self._session = sessionmaker(self.init_connection_engine())()

        return self._session

    def init_connection_engine(self):
        db_config = {
            # [START cloud_sql_postgres_sqlalchemy_limit]
            # Pool size is the maximum number of permanent connections to keep.
            "pool_size": 5,
            # Temporarily exceeds the set pool_size if no connections are available.
            "max_overflow": 2,
            # The total number of concurrent connections for your application will be
            # a total of pool_size and max_overflow.
            # [END cloud_sql_postgres_sqlalchemy_limit]

            # [START cloud_sql_postgres_sqlalchemy_backoff]
            # SQLAlchemy automatically uses delays between failed connection attempts,
            # but provides no arguments for configuration.
            # [END cloud_sql_postgres_sqlalchemy_backoff]

            # [START cloud_sql_postgres_sqlalchemy_timeout]
            # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
            # new connection from the pool. After the specified amount of time, an
            # exception will be thrown.
            "pool_timeout": 30,  # 30 seconds
            # [END cloud_sql_postgres_sqlalchemy_timeout]

            # [START cloud_sql_postgres_sqlalchemy_lifetime]
            # 'pool_recycle' is the maximum number of seconds a connection can persist.
            # Connections that live longer than the specified amount of time will be
            # reestablished
            "pool_recycle": 1800,  # 30 minutes
            # [END cloud_sql_postgres_sqlalchemy_lifetime]
        }

        if os.environ.get("DB_HOST"):
            return self.init_tcp_connection_engine(db_config)
        else:
            return self.init_unix_connection_engine(db_config)

    def init_tcp_connection_engine(self, db_config):
        # [START cloud_sql_postgres_sqlalchemy_create_tcp]
        # Remember - storing secrets in plaintext is potentially unsafe. Consider using
        # something like https://cloud.google.com/secret-manager/docs/overview to help keep
        # secrets secret.
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASS"]
        db_name = os.environ["DB_NAME"]
        db_host = os.environ["DB_HOST"]

        # Extract host and port from db_host
        host_args = db_host.split(":")
        db_hostname, db_port = host_args[0], int(host_args[1])

        pool = sqlalchemy.create_engine(
            # Equivalent URL:
            # postgres+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
            sqlalchemy.engine.url.URL(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                host=db_hostname,
                port=db_port,
                database=db_name
            ),
            **db_config
        )
        # [END cloud_sql_postgres_sqlalchemy_create_tcp]
        pool.dialect.description_encoding = None
        return pool

    def init_unix_connection_engine(self, db_config):
        # [START cloud_sql_postgres_sqlalchemy_create_socket]
        # Remember - storing secrets in plaintext is potentially unsafe. Consider using
        # something like https://cloud.google.com/secret-manager/docs/overview to help keep
        # secrets secret.
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASS"]
        db_name = os.environ["DB_NAME"]
        db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
        cloud_sql_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]

        pool = sqlalchemy.create_engine(

            # Equivalent URL:
            # postgres+pg8000://<db_user>:<db_pass>@/<db_name>
            #                         ?unix_sock=<socket_path>/<cloud_sql_instance_name>/.s.PGSQL.5432
            sqlalchemy.engine.url.URL(
                drivername="postgresql+pg8000",
                username=db_user,
                password=db_pass,
                database=db_name,
                query={
                    "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                        db_socket_dir,  # e.g. "/cloudsql"
                        cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
                }
            ),
            **db_config
        )
        # [END cloud_sql_postgres_sqlalchemy_create_socket]
        pool.dialect.description_encoding = None
        return pool

    def init_session(self):
        print(id(self.load))
        session = sessionmaker(self.load)
        return session()

    @staticmethod
    def close_all_sessions():
        close_all_sessions()
