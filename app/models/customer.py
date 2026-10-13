from app.database.db import get_connection
import sqlite3

class Customer:
    def __init__(self, id, name, phone_number):
        self.id = id
        self.name = name
        self.phone_number = phone_number

    def save(self):
        connection = get_connection()

        try:
            cursor = connection.execute(
                """
                INSERT INTO customers (name, phone_number)
                VALUES (?, ?) 
                """,
                (self.name, self.phone_number)
            )
            connection.commit
            self.id = cursor.lastrowid

        finally:
            connection.close
    

