import sqlalchemy as db
from sqlalchemy.sql.sqltypes import Integer

engine = db.create_engine('sqlite:///users.db')

connection = engine.connect()

metadata = db.MetaData()

def create_db_table(metadata, engine):
    users = db.Table(
            'users', metadata,
            db.Column("User_Id", db.Integer),
            db.Column("First_Name", db.String),
            db.Column("Last_Name", db.String),
            db.Column("EmailAddress", db.String)
            )

    try:
        metadata.create_all(engine)
        print("tables created")
        return users

    except Exception as e:
        print("error occurred during Table creation!")
        print(e)
        return None

# users = create_db_table(metadata, engine)
users = db.Table('users', metadata, autoload=True, autoload_with=engine)

user_records = [(2, 'Sky', 'Moore', 'skymoore@hyde.com'),
        (3, 'Sarbani', 'Roy', 'sarbani@alnylam.com'),
        (4, 'Ranadeep', 'Singh', 'rana@facebook.com')]


# query = users.insert().values(User_Id=1, First_Name="Sid", Last_Name="Roy", EmailAddress="sid@google.com")
# connection.execute(query)

query = db.select([users])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)
