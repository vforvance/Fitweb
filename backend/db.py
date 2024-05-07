import sqlalchemy as db
from db_utils import  _engine, clean_and_create_cache_schema
import json


schema_creation_script = """
CREATE TABLE user (
        userid INTEGER NOT NULL,
        username VARCHAR(16),
        email VARCHAR(60),
        firstname VARCHAR(60),
        lastname VARCHAR(60),
        height INTEGER,
        weight INTEGER,
        fitnessgoal TEXT,
        PRIMARY KEY (userid)
);

CREATE TABLE exercise (
        exerciseid INTEGER NOT NULL,
        name VARCHAR(50),
        musclegroup VARCHAR(128),
        difficultylevel INTEGER,
        equipment VARCHAR(100),
        description TEXT,
        PRIMARY KEY (exerciseid)
);

CREATE TABLE workout (
        workoutid INTEGER NOT NULL,
        userid INTEGER NOT NULL,
        name VARCHAR(50),
        starttime DATETIME,
        endtime DATETIME,
        notes TEXT,
        PRIMARY KEY (workoutid),
        FOREIGN KEY(userid) REFERENCES user (userid)
);

CREATE TABLE log (
        logid INTEGER NOT NULL,
        exerciseid INTEGER,
        workoutid INTEGER,
        "set" INTEGER,
        rep INTEGER,
        weight INTEGER,
        duration INTEGER,
        PRIMARY KEY (logid),
        FOREIGN KEY(exerciseid) REFERENCES exercise (exerciseid),
        FOREIGN KEY(workoutid) REFERENCES workout (workoutid)
);

CREATE TABLE goal (
        goalid INTEGER NOT NULL,
        userid INTEGER NOT NULL,
        logid INTEGER,
        description TEXT,
        achievedtime DATETIME,
        isachieved BOOLEAN,
        targetdate DATE,
        PRIMARY KEY (goalid),
        FOREIGN KEY(userid) REFERENCES user (userid),
        FOREIGN KEY(logid) REFERENCES log (logid)
);
"""

schema = {

  'user': [{'name': 'userid',
           'type': 'int',
           'isrelationship': False,
           'otherside': None},
          {'name': 'username',
           'type': 'str',
           'isrelationship': False,
           'otherside': None},
          {'name': 'email',
           'type': 'str',
           'isrelationship': False,
           'otherside': None},
          {'name': 'firstname',
           'type': 'str',
           'isrelationship': False,
           'otherside': None},
          {'name': 'lastname',
           'type': 'str',
           'isrelationship': False,
           'otherside': None},
          {'name': 'height',
           'type': 'int',
           'isrelationship': False,
           'otherside': None},
          {'name': 'weight',
           'type': 'int',
           'isrelationship': False,
           'otherside': None},
          {'name': 'fitnessgoal',
           'type': 'str',
           'isrelationship': False,
           'otherside': None}],
 'exercise': [{'name': 'exerciseid',
               'type': 'int',
               'isrelationship': False,
               'otherside': None},
              {'name': 'name',
               'type': 'str',
               'isrelationship': False,
               'otherside': None},
              {'name': 'musclegroup',
               'type': 'str',
               'isrelationship': False,
               'otherside': None},
              {'name': 'difficultylevel',
               'type': 'int',
               'isrelationship': False,
               'otherside': None},
              {'name': 'equipment',
               'type': 'str',
               'isrelationship': False,
               'otherside': None},
              {'name': 'description',
               'type': 'str',
               'isrelationship': False,
               'otherside': None}],
 'workout': [{'name': 'workoutid',
              'type': 'int',
              'isrelationship': False,
              'otherside': None},
             {'name': 'userid',
              'type': 'int',
              'isrelationship': True,
              'otherside': 'user'},
             {'name': 'name',
              'type': 'str',
              'isrelationship': False,
              'otherside': None},
             {'name': 'starttime',
              'type': 'datetime',
              'isrelationship': False,
              'otherside': None},
             {'name': 'endtime',
              'type': 'datetime',
              'isrelationship': False,
              'otherside': None},
             {'name': 'notes',
              'type': 'str',
              'isrelationship': False,
              'otherside': None}],
 'log': [{'name': 'logid',
          'type': 'int',
          'isrelationship': False,
          'otherside': None},
         {'name': 'exerciseid',
          'type': 'int',
          'isrelationship': True,
          'otherside': 'user'},
         {'name': 'workoutid',
          'type': 'int',
          'isrelationship': True,
          'otherside': 'user'},
         {'name': 'set',
          'type': 'int',
          'isrelationship': False,
          'otherside': None},
         {'name': 'rep',
          'type': 'int',
          'isrelationship': False,
          'otherside': None},
         {'name': 'weight',
          'type': 'int',
          'isrelationship': False,
          'otherside': None},
         {'name': 'duration',
          'type': 'int',
          'isrelationship': False,
          'otherside': None}],
 'goal': [{'name': 'goalid',
           'type': 'int',
           'isrelationship': False,
           'otherside': None},
          {'name': 'userid',
           'type': 'int',
           'isrelationship': True,
           'otherside': 'user'},
          {'name': 'logid',
           'type': 'int',
           'isrelationship': True,
           'otherside': 'user'},
          {'name': 'description',
           'type': 'str',
           'isrelationship': False,
           'otherside': None},
          {'name': 'achievedtime',
           'type': 'datetime',
           'isrelationship': False,
           'otherside': None},
          {'name': 'isachieved',
           'type': 'bool',
           'isrelationship': False,
           'otherside': None},
          {'name': 'targetdate',
           'type': 'date',
           'isrelationship': False,
           'otherside': None}]}
"""
user = db.Table(
    "user",
    metadata,
    db.Column("userid", db.Integer, primary_key=True),
    db.Column("username", db.String(16)),
    db.Column("email", db.String(60)),
    db.Column("firstname", db.String(60)),
    db.Column("lastname", db.String(60)),
    db.Column("height", db.Integer),
    db.Column("weight", db.Integer),
    db.Column("fitnessgoal", db.Text)
)

exercise = db.Table(
    "exercise",
    metadata,
    db.Column("exerciseid", db.Integer, primary_key=True),
    db.Column("name", db.String(50)),
    db.Column("musclegroup", db.String(128)),
    db.Column("difficultylevel", db.Integer),
    db.Column("equipment", db.String(100)),
    db.Column("description", db.Text)
)

workout = db.Table(
    "workout",
    metadata,
    db.Column("workoutid", db.Integer, primary_key=True),
    db.Column("userid", db.Integer, db.ForeignKey("user.userid"), nullable=False),
    db.Column("name", db.String(50)),
    db.Column("starttime", db.DateTime),
    db.Column("endtime", db.DateTime),
    db.Column("notes", db.Text)
)

log = db.Table(
    "log",
    metadata,
    db.Column("logid", db.Integer, primary_key=True),
    #db.Column("userid", db.Integer, db.ForeignKey("user.userid"), nullable=False),
    db.Column("exerciseid", db.Integer, db.ForeignKey("exercise.exerciseid")),
    db.Column("workoutid", db.Integer, db.ForeignKey("workout.workoutid"), nullable=True),
    db.Column("set", db.Integer),
    db.Column("rep", db.Integer),
    db.Column("weight", db.Integer),
    db.Column("duration", db.Integer)
)

goal = db.Table(
    "goal",
    metadata,
    db.Column("goalid", db.Integer, primary_key=True),
    db.Column("userid", db.Integer, db.ForeignKey("user.userid"), nullable=False),
    db.Column("logid", db.Integer, db.ForeignKey("log.logid")),
    db.Column("description", db.Text),
    db.Column("achievedtime", db.DateTime),
    db.Column("isachieved", db.Boolean),
    db.Column("targetdate", db.Date)
)
"""
fake_data = None
fake_data2 = None

def insert_test_data(engine):
    with engine.connect() as conn:
        _ = [conn.execute(
            db.insert(
                data['table']
                ), data['data']
        )  for data in fake_data]
        conn.commit()

"""
def generate_schema():
    schema = {
        table_name: [{
            'name': c.name, 
            'type': str(c.type.python_type.__name__), 
            'isrelationship': len(c.foreign_keys) > 0,
            'otherside': list(workout.c.userid.foreign_keys)[0].column.table.name if len(c.foreign_keys) > 0 else None
            } for c in table.c]
        for table_name, table in metadata.tables.items()
    }
    return schema
"""
def make_om(table, column, name):
    return {
        'table': table,
        'column': column,
        'name': name
    }

one_to_many = {
    'user': [make_om('workout', 'userid', 'workouts')],
    'workout': [make_om('log', 'workoutid', 'logs')]
}

def handle_to_many(base_id, rel):
    filter_expr = f"{rel['table']}.{rel['column']} = {base_id}"
    return filter_expr

def wrap_column(column):
    return f"`{column['name']}`"

def handle_record(conn, table, result):
    if len(result) == 0: return result
    _id = result.get(f'{table}id')
    to_many = one_to_many.get(table, [])
    to_many_results = {
        to_many_field['name']: serialize_resource(conn, to_many_field['table'], handle_to_many(_id, to_many_field)) for to_many_field in to_many
    }
    return {**result, **to_many_results}

def serialize_resource(conn, table, _filter, args={}):
    columns = schema[table]
    wrapped_column = [wrap_column(column) for column in columns]
    select_expr = f"select {','.join(wrapped_column)} from {table} where {_filter};"
    #sql_table = metadata.tables[table]
    #print(select_expr)
    result = conn.execute(db.text(select_expr), args)
    result = result.all()
    results = [handle_record(conn, table, {
        c['name']: row[cid] for cid, c in enumerate(columns)
        } if result is not None else {}) for row in result]
    return results

def get_id_given_name(username):
    engine = clean_and_create_cache_schema("fitness")
    query = "SELECT userid FROM user WHERE username = :username"
    stmt = db.text(query)
    with engine.connect() as conn:
        result = conn.execute(stmt, {'username':username}).first()
        user_id = result[0]
        return {'id': user_id}

def get_user_max_by_weights():
    query = """select
                exercisename,
                max(username),
                max_weight from user join workout on user.userid = workout.userid join log on log.workoutid = workout.workoutid join (
                    select
                        exerciseid,
                        exercise.name as exercisename,
                        max(weight) as max_weight
                    from exercise join log using (exerciseid) group by exerciseid
            ) as temp on temp.max_weight = log.weight group by exercisename, max_weight;"""
    stmt = db.text(query)
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        rows = conn.execute(stmt)
        rows = [[*row] for row in rows]
        return {'items': list(rows)}
    ...


def wrap_serialize(table, _id):
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        return serialize_resource(conn, table, f'{table}id = {_id}')[0]
    
def get_personal_bests(user_id):
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        query = db.text(f"""
                select exercise.name, max(log.weight) from user join workout on user.userid = workout.userid join log on log.workoutid = workout.workoutid
                join exercise on exercise.exerciseid = log.exerciseid where user.userid = :userid group by exercise.name
                """)
        row = conn.execute(query, {'userid': user_id}).all()
        row = [[*row] for row in row]
        return {_row[0]: _row[1] for _row in row}

def get_workout_by_name(user, name):
    user = int(user)
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        return serialize_resource(conn, 'workout', (f"workout.userid={user} and workout.name like :safe"), {'safe': f'%{name}%'})

def get_workout_by_user(user):
    user = int(user)
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        return serialize_resource(conn, 'workout', f"workout.userid={user}")

if __name__ == '__main__':
    #print(metad    ata.tables.values())
    engine = clean_and_create_cache_schema("fitness", False)
    #with engine.connect() as conn:
    #    conn.execute(schema_creation_script)
    print(wrap_serialize('user', 1))
    print(get_workout_by_user(1))

