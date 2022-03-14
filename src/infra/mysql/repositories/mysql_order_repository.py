import mysql.connector
from mysql.connector import MySQLConnection

from src.domain.entities.order import Order
from src.domain.repositories.order_repository import OrderRepository
from src.domain.value_objects.order_id import OrderId
from src.infra.mysql.data_access_objects.order_dao import OrderDAO


class MysqlOrderRepository(OrderRepository):
    __connection: MySQLConnection

    def __init__(self):
        self.__connection = mysql.connector.connect(user="root", password="", host="127.0.0.1", port="3306",
                                                    database="acai_api")

    def save(self, order: Order):
        dao = OrderDAO.from_entity(order)
        cursor = self.__connection.cursor()
        query = dao.build_insert_query()
        cursor.execute(query)
        self.__connection.commit()
        # for row in cursor:
        #     print(row)

    def select_all(self) -> list[Order]:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM acai_api.order;")
        self.__connection.commit()
        print(list[cursor.get_rows()])

    def find_by_id(self, id: OrderId) -> Order:
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM acai_api.order WHERE id ='" + str(id) + "' ;")
        self.__connection.commit()

        return cursor
