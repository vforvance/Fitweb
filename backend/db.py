import sqlalchemy as db
from db_utils import create_all, metadata, _engine, clean_and_create_cache_schema

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

fake_data = [
    {
        'table': user,
        'data': [
            {
                "userid": 1,
                "username": 'john',
                "email": "john@ku.edu",
                "firstname": "John",
                "lastname": "Doe",
                "height": 170,
                "weight": 78,
                "fitnessgoal": "Be like Arnold"
            },
            {
                "userid": 2,
                "username": 'kevin',
                "email": "kevin@ku.edu",
                "firstname": "Kevin",
                "lastname": "Malone",
                "height": 170,
                "weight": 180,
                "fitnessgoal": "Be like Jim"
            }
        ]
    }, 
    {
        'table': exercise,
        "data": [
            {
                "exerciseid": 1,
                "name": "Bench Press",
                "musclegroup": "chest",
                "difficultylevel": 2,
                "equipment": "Bench, Barbell",
                "description": None
            },
            {
                "exerciseid": 2,
                "name": "Squat",
                "musclegroup": "legs",
                "difficultylevel": 3,
                "equipment": "Squat rack, Barbell",
                "description": None
            }
        ]
    },
    {
        'table': workout,
        "data": [
            {
                "workoutid": 1,
                "userid": 1,
                "name": "Monday morning workout",
                "starttime": None,
                "endtime": None,
                "notes": "Nice workout"
            },
            {
                "workoutid": 2,
                "userid": 1,
                "name": "Monday evening workout",
                "starttime": None,
                "endtime": None,
                "notes": "Nice workout, the second one"
            },
            {
                "workoutid": 3,
                "userid": 2,
                "name": "Workout with John",
                "starttime": None,
                "endtime": None,
                "notes": "Nice workout"
            },
            {
                "workoutid": 4,
                "userid": 2,
                "name": "Workout without Jim",
                "starttime": None,
                "endtime": None,
                "notes": "Nice workout, the second one"
            },
        ]
    },
    {
        'table': log,
        "data": [
            {
                "logid": 1,
                "exerciseid": 1,
                "workoutid": 1,
                "set": 5,
                "rep": 5,
                "weight": 180,
                "duration": 20
            },
            {
                "logid": 2,
                "exerciseid": 2,
                "workoutid": 1,
                "set": 4,
                "rep": 1,
                "weight": 350,
                "duration": 40 
            },
            {
                "logid": 3,
                "exerciseid": 2,
                "workoutid": 3,
                "set": 4,
                "rep": 9,
                "weight": 350,
                "duration": 190
            },

        ]
    }
]

def insert_test_data(engine):
    with engine.connect() as conn:
        _ = [conn.execute(
            db.insert(
                data['table']
                ), data['data']
        )  for data in fake_data]
        conn.commit()

def generate_schema():
    schema = {
        table_name: [{'name': c.name, 'type': str(c.type.python_type.__name__), 'isrelationship': len(c.foreign_keys) > 0} for c in table.c]
        for table_name, table in metadata.tables.items()
    }
    return schema

if __name__ == '__main__':
    print(metadata.tables)
    generate_schema()
    #engine = clean_and_create_cache_schema("fitness", True)
    #metadata.create_all(engine)
    #insert_test_data(engine)
