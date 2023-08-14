import psycopg2


# connect to "chinook" database
#connection = psycopg2.connect(database = "chinook")
connection = psycopg2.connect("dbname=chinook user=postgres password=password")

# build a cursor object of the database. A cursor object is another way of saying a 'set' or 'list', similar to an 'array' in JavaScript.
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table. USE SINGLE QUOTES!!!
# cursor.execute('SELECT * FROM "Artist"')

# Query 2- select only the "Name" column from the "Artist" table.
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3- select only the "Queen" from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])  # %s - Python string placeholder

# Query 4 - select only by "ArtistId" #51 from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])  # %s - Python string placeholder

# Query 5 - select only by albums with "ArtistId" #51 on the "Album" table.
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])  # %s - Python string placeholder

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table.
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Santana"])  # %s - Python string placeholder

# fetch the results (multiple). if we need to query multiple records from our database, we should use the .fetchall() method.
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the collection
connection.close()

# print results
for result in results:
    print(result)
