
import json
import psycopg2
from src.constants.http_status_codes import *


json_file = 'src/config/allChars.json'

with open(json_file, 'r', encoding='utf-8') as file:
    directory_path = json.load(file)

# Database connection information
host = HOST
database = DATABASE
user = USER
password = PASSWORD

def populate_db():

    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Iterate over the data and insert into the database
    for item in directory_path:
        # Extract the desired information from the JSON data
        name = item['name']
        status = item['status']
        species = item['species']
        type_char = item['type']
        gender = item['gender']
        origin_name = item['origin']['name']
        location_name = item['location']['name']
        image = item['image']

        # Add more attributes as needed

        # Define the SQL query for inserting the data
        sql_query = "INSERT INTO character (name, status, species, type_char, gender, origin_name, location_name, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # Execute the SQL query with the extracted data
        cursor.execute(sql_query, (name, status, species, type_char, gender, origin_name, location_name, image))

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
