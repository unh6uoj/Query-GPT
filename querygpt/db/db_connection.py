import pymysql

from querygpt.common import singleton


@singleton
class DBConnection:
    def __init__(
        self,
        host: str = None,
        port: int = None,
        user: str = None,
        passwd: str = None,
        db: str = None,
        charset: str = "utf8",
    ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset,
        )

        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def execute_one(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def execute_all(self, query: str) -> list:
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_table_schema(self, table_name: str) -> list:
        return self.execute_all(
            f"""
                SELECT * FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = SCHEMA()
                AND TABLE_NAME = '{table_name}'
                ORDER BY ORDINAL_POSITION;
            """
        )
