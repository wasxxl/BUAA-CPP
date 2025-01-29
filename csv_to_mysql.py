import pandas as pd
import mysql.connector
from mysql.connector import Error

# Function to create a connection to the MySQL database
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a query
def execute_query(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Database connection parameters
host_name = "localhost"
user_name = "root"
user_password = "17377756"
db_name = "buaa_online_judge"

# Create a connection to the database
connection = create_connection(host_name, user_name, user_password, db_name)

# # Read the CSV file into a DataFrame
df = pd.read_csv('whole_record.csv')


#
# # Prepare the data for insertion
# data = list(df.itertuples(index=False, name=None))
#
# # Define the insert query (assuming the table is already created)
# insert_query = """
# INSERT INTO your_table_name (id, name, age)
# VALUES (%s, %s, %s)
# """
#
# # Execute the query to insert data
# execute_query(connection, insert_query, data)