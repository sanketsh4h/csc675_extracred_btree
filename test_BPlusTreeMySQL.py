import unittest
from BPlusTreeMySQL import MySQLBPlusTree
import mysql.connector

# MySQL connection setup for testing
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testing_btree"
)

cursor = db.cursor()

class TestMySQLBPlusTree(unittest.TestCase):
    def setUp(self):
        self.tree = MySQLBPlusTree(order=3)
        cursor.execute("DELETE FROM test_table")
        db.commit()

    def test_insert(self):
        self.tree.insert(10, (10, 10.5, "test1", "2024-05-20"))
        self.tree.insert(20, (20, 20.5, "test2", "2024-05-21"))
        self.tree.insert(5, (5, 5.5, "test3", "2024-05-22"))
        self.tree.show()

    def test_update(self):
        self.tree.insert(10, (10, 10.5, "test1", "2024-05-20"))
        self.tree.update(10, 15, (15, 15.5, "test_updated", "2024-05-23"))
        self.tree.show()

    def test_delete(self):
        self.tree.insert(10, (10, 10.5, "test1", "2024-05-20"))
        self.tree.insert(20, (20, 20.5, "test2", "2024-05-21"))
        self.tree.delete(10)
        self.tree.show()

    def test_show(self):
        self.tree.insert(10, (10, 10.5, "test1", "2024-05-20"))
        self.tree.insert(20, (20, 20.5, "test2", "2024-05-21"))
        self.tree.insert(5, (5, 5.5, "test3", "2024-05-22"))
        self.tree.show()

if __name__ == '__main__':
    unittest.main()
