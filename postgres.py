import psycopg2

from config import config


class Postgres:
    @staticmethod
    def execute(query: str):
        """ Connect to the PostgreSQL database server """
        conn = None
        query_result = None
        try:
            # read connection parameters
            params = config()

            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            print('Executing : ' + query)
            cur.execute(query)

            # display the PostgreSQL database server version
            query_result = cur.fetchall()
            print(query_result)

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')

            return query_result
