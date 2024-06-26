import sqlalchemy as db

get_db_url = lambda schema: f'sqlite:///mem.db'

_engine = db.create_engine(get_db_url("fitness"))

def clean_and_create_cache_schema(cache_schema, drop=False):
        if drop:
                with _engine.connect() as connection:
                        #connection.execute(db.text(f"DROP SCHEMA IF EXISTS {cache_schema}"))
                        #connection.execute(db.text(f"CREATE SCHEMA {cache_schema}"))
                        #connection.commit()
                        ...
        return db.create_engine(get_db_url(cache_schema))

if __name__ == '__main__':
    get_db_url(None)
    clean_and_create_cache_schema("fitness")
