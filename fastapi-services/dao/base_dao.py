import mysql.connector
import config


class BaseDAO:
    __connection = None
    __cursor = None

    def __init__(self):
        self.__connection = mysql.connector.connect(host=config.HOST, port=config.PORT, database=config.DB_NAME,
                                                    user=config.USER, password=config.PASSWORD)
        self.__cursor = self.__connection.cursor()

    def query(self, sql, params):
        self.__cursor.execute(sql, params)
        return self.__cursor

    def close(self):
        self.__cursor.close()
        self.__connection.close()

    def commit(self):
        self.__connection.commit()
