import mysql.connector
from BPlusTree import BPlusTree


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testing_btree"
)

cursor = db.cursor()

# B+ Tree implementation 

class MySQLBPlusTree:
    def __init__(self, order):
        self.tree = BPlusTree(order)

    def insert(self, key, value):
        query = "INSERT INTO test_table (int_column, float_column, string_column, date_column) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, value)
        db.commit()
        self.tree.insert(key)

    def update(self, old_key, new_key, new_value):
        query = "UPDATE test_table SET int_column = %s, float_column = %s, string_column = %s, date_column = %s WHERE int_column = %s"
        cursor.execute(query, new_value + (old_key,))
        db.commit()
        self.tree.delete(old_key)
        self.tree.insert(new_key)

    def delete(self, key):
        query = "DELETE FROM test_table WHERE int_column = %s"
        cursor.execute(query, (key,))
        db.commit()
        self.tree.delete(key)

    def show(self):
        self.tree.show()

def main():
    order = int(input("Enter the order of the B+ Tree: "))
    my_tree = MySQLBPlusTree(order)
    print("Available commands: INSERT <int> <float> <string> <date>, DELETE <int>, UPDATE <old_int> <new_int> <float> <string> <date>, SHOW")

    while True:
        command = input("Enter command: ").strip()
        if command.startswith('INSERT'):
            _, int_val, float_val, str_val, date_val = command.split()
            my_tree.insert(int(int_val), (int_val, float_val, str_val, date_val))
            my_tree.show()
        elif command.startswith('DELETE'):
            _, int_val = command.split()
            my_tree.delete(int(int_val))
            my_tree.show()
        elif command.startswith('UPDATE'):
            _, old_int_val, new_int_val, float_val, str_val, date_val = command.split()
            my_tree.update(int(old_int_val), int(new_int_val), (new_int_val, float_val, str_val, date_val))
            my_tree.show()
        elif command == 'SHOW':
            my_tree.show()
        elif command.lower() == 'exit':
            print("Exiting B+ Tree Interactive Shell.")
            break

if __name__ == '__main__':
    main()
