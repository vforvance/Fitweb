import sqlalchemy as db

get_db_url = lambda schema: f'mysql://%s:%s@%s:%s{f"/{schema}" if schema is not None else ""}?charset=utf8' % (
        'root',
        'ROOT',
        '127.0.0.1',
        3306)

_engine = db.create_engine(get_db_url("fitness"))

metadata = db.MetaData()

def clean_and_create_cache_schema(cache_schema, drop=False):
        if drop:
                with _engine.connect() as connection:
                        connection.execute(db.text(f"DROP SCHEMA IF EXISTS {cache_schema}"))
                        connection.execute(db.text(f"CREATE SCHEMA {cache_schema}"))
                        connection.commit()
        return db.create_engine(get_db_url(cache_schema))

        
def create_all():
    metadata.create_all(_engine)

if __name__ == '__main__':
    get_db_url(None)
    clean_and_create_cache_schema("fitness")
