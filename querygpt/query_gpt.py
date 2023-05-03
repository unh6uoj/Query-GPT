from querygpt.db.db_connection import DBConnection
from querygpt.openai.openai import OpenAI


class QueryGPT:
    def __init__(self):
        self.openai = OpenAI()
        self.db_helper = None
        self.table_data = {}

    def config_database(
        self, host: str, port: int, user: str, passwd: str, db: str, charset: str = "utf8"
    ):
        """database connection configuration

        Args:
            host (str): host ip
            port (int): port number
            user (str): user name
            passwd (str): password
            db (str): database name
            charset (str, optional): charset. Defaults to "utf8".
        """
        self.db_helper = DBConnection(host, port, user, passwd, db, charset)

    def select_tables(self, tables: dict):
        """settings for tables to use

        Args:
            tables (dict): dictionary with table name as key and column list as value
        """
        for table_name, columns in tables.items():
            if not columns:
                table_schema = self.db_helper.get_table_schema(table_name)
            else:
                table_schema = self.db_helper.get_table_schema_with_columns(table_name, columns)

            self.table_data[table_name] = [
                {
                    "column_name": column["COLUMN_NAME"],
                    "column_type": column["COLUMN_TYPE"],
                }
                for column in table_schema
            ]
