from sqlalchemy.engine import create_engine 
from sqlalchemy import schema,types

db=create_engine('postgresql://postgres:1ntpass1nt@localhost:5432/postgres')

schema.MetaData(bind=db)

