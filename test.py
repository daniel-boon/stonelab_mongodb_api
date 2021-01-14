from connection.settings import Database_connection
database = Database_connection('customers','stonelab')
database.check_connection()

# database = Database_connection('customers','stonelab')
# print(database.collection)
# database.check_connection()