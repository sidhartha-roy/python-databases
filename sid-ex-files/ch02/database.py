import sqlalchemy as db

# an engine allows the application to have multiple database connections
# and it manages the connections
engine = db.create_engine('sqlite:///movies.db')

# this is a proxy for the true python database connection
connection = engine.connect()

# holds all information about the table
metadata = db.MetaData()

# load movies table into sqlalchemy
movies = db.Table('Movies', metadata, autoload=True, autoload_with=engine)

# make queries to the table
# select all
query = db.select([movies])

# this proxies the cursor object from the python api
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

print(result_set[0])
print(result_set[:3])

query2 = db.select([movies]).where(movies.columns.Director == "Martin Scorsese")
result_proxy = connection.execute(query2)
result_set = result_proxy.fetchall()
print(result_set[0])

query = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", YEAR="1960")
connection.execute(query)

query = db.select([movies])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)
