import mysql.connector
from mysql.connector import MySQLConnection

from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository


class MysqlOrderRepository(OrderRepository):
    __connection: MySQLConnection

    def __init__(self):
        self.__connection = mysql.connector.connect(user="root", password="", host="127.0.0.1", port="3306",
                                                    database="acai_api")

    def save(self, order: Order):
        cursor = self.__connection.cursor()
        cursor.execute("INSERT INTO acai_api.order (id, garnish) values ('" + str(order.id.value) + "', '" +
                       order.garnish.value + "');")
        self.__connection.commit()
        # for row in cursor:
        #     print(row)
