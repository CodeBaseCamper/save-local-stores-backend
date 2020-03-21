import os
import psycopg2
from psycopg2.extensions import AsIs

from loguru import logger

# from app import DefaultPaths

# log = logger
# log.add(f"{os.path.join(DefaultPaths.LOG_PATH)}/database.log", rotation="5 MB",
#         format="[{time:HH:mm:ss}] [{level}] {message}")


class SQL(object):
    def __init__(self, server_ip=None, sql_user=None, sql_pass=None, sql_db=None):
        self.db_config = {
            "host": server_ip,
            "user": sql_user,
            "password": sql_pass,
            "dbname": sql_db
        }
        self.server_ip = server_ip
        self.sql_user = sql_user
        self.sql_pass = sql_pass

        self.curr_conn = None

    def _connect(self):
        try:
            conn = psycopg2.connect(**self.db_config)
            conn.set_client_encoding('utf8')
            # create a cursor
            self.curr_conn = conn.cursor()
        except Exception as desc:
            print(desc)
            pass
            # log.exception('')

    def _close_connection(self):
        # close the communication with the PostgreSQL
        try:
            self.curr_conn.close()
        except Exception as desc:
            print(desc)
            pass
            # log.exception('')

        self.curr_conn = None

    def _execute(self, query, args=None):
        # connect to database
        self._connect()

        try:
            if args:
                self.curr_conn.execute(query, args)
            else:
                self.curr_conn.execute(query)

        except Exception as desc:
            print(desc)
            # log.exception('')
            if self.curr_conn is not None:
                self._close_connection()
            return False

        # fetch all data
        data = self.curr_conn.fetchall()
        # close current connection
        self._close_connection()

        return data

    def query(self, query, args=None):
        return self._execute(query, args)

    def query_all(self, table_name):
        query = "SELECT * FROM %(table_name)s"
        return self.query(query, {'table_name': AsIs(table_name)})


