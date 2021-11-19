import MySQLdb
import logging
import settings


class Database:
    def __init__(self):
        try:
            self.db = MySQLdb.connect(
                user=settings.USER,
                passwd=settings.PASSWD,
                host=settings.HOST,
                db=settings.DB,
                charset="utf8",
            )
            logging.info(f"Connecting to MySQL Database [{settings.DB}] succeeded")
        except Exception as e:
            logging.error(e)
            logging.error("Connecting to MySQL failed")

    def insert(self, column):
        try:
            params = list(column.keys())
            columns = list(column.values())
            logging.info(f"Column: {column}")

            cursor = self.db.cursor()
            cursor.execute(
                f"""
                INSERT INTO {settings.TARGET_DB_TABLE} ({','.join(params)})
                VALUES {tuple(columns)};
                """
            )
            self.db.commit()
            logging.info(f"Insert row to table [{settings.TARGET_DB_TABLE}] succeeded")
        except Exception as e:
            logging.error(e)
            logging.error("Insert failed")

    def draw_result(self):
        cursor = self.db.cursor()
        cursor.execute(
            f"""
            SELECT * FROM {settings.TARGET_DB_TABLE}
            """
        )
        results = cursor.fetchall()
        widths = []
        columns = []
        tavnit = "|"
        separator = "+"

        for cd in cursor.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-" + "%ss |" % (w,)
            separator += "-" * w + "--+"

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
        print(separator)
