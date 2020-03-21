import os
from typing import Union

import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import RealDictCursor

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

        self.curr_conn = None

    def _connect(self):
        try:
            conn = psycopg2.connect(**self.db_config)
            conn.set_client_encoding('utf8')
            # create a cursor
            self.curr_conn = conn.cursor(cursor_factory=RealDictCursor)
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
        # run a given query
        return self._execute(query, args)

    def query_all(self, table_name):
        # select all from given table
        query = "SELECT * FROM %(table_name)s"
        return self.query(query, {'table_name': AsIs(table_name)})

    def query_where(self, table_name: str, args: dict, select: Union[list, str] = "*", connector: str = 'AND') -> dict:
        query = None
        select = select if type(select) == str else ", ".join(select)
        query_base = f"SELECT {select} FROM %(table_name)s"

        if not args:
            return {'query': query, 'args': args}
        else:
            for column in args:
                print(column)
                if not query:
                    # first data
                    query = f"{query_base} WHERE {column} = %({column})s"
                else:
                    # append other data
                    query = f"{query} {connector} {column} = %({column})s"
        # add table name to args
        args['table_name'] = AsIs(table_name)

        return self.query(query, args)

