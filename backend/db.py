import sqlalchemy as db
from db_utils import create_all, metadata, _engine, clean_and_create_cache_schema
import json

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
            },
            {
                "userid": 3,
                "username": 'jane',
                "email": "jane@ku.edu",
                "firstname": "Jane",
                "lastname": "Doe",
                "height": 165,
                "weight": 60,
                "fitnessgoal": "Get fit"
            },
            {
                "userid": 4,
                "username": 'alex',
                "email": "alex@ku.edu",
                "firstname": "Alex",
                "lastname": "Smith",
                "height": 180,
                "weight": 85,
                "fitnessgoal": "Gain muscle"
            },
            {
                "userid": 5,
                "username": 'emma',
                "email": "emma@ku.edu",
                "firstname": "Emma",
                "lastname": "Johnson",
                "height": 165,
                "weight": 55,
                "fitnessgoal": "Stay healthy"
            },
            {
                "userid": 6,
                "username": 'mike',
                "email": "mike@ku.edu",
                "firstname": "Mike",
                "lastname": "Brown",
                "height": 175,
                "weight": 70,
                "fitnessgoal": "Improve endurance"
            },
            {
                "userid": 7,
                "username": 'sarah',
                "email": "sarah@ku.edu",
                "firstname": "Sarah",
                "lastname": "Wilson",
                "height": 160,
                "weight": 65,
                "fitnessgoal": "Increase flexibility"
            },
            {
                "userid": 8,
                "username": 'chris',
                "email": "chris@ku.edu",
                "firstname": "Chris",
                "lastname": "Anderson",
                "height": 185,
                "weight": 90,
                "fitnessgoal": "Build strength"
            },
            {
                "userid": 9,
                "username": 'laura',
                "email": "laura@ku.edu",
                "firstname": "Laura",
                "lastname": "Taylor",
                "height": 162,
                "weight": 63,
                "fitnessgoal": "Tone muscles"
            },
            {
                "userid": 10,
                "username": 'steve',
                "email": "steve@ku.edu",
                "firstname": "Steve",
                "lastname": "Wilson",
                "height": 178,
                "weight": 80,
                "fitnessgoal": "Reduce body fat"
            }
            # Add more user objects as needed
        ]
    },
    {
        'table': exercise,
        "data": [
            {
                "exerciseid": 1,
                "name": "Bench Press",
                "musclegroup": "Chest",
                "difficultylevel": 2,
                "equipment": "Bench, Barbell",
                "description": None
            },
            {
                "exerciseid": 2,
                "name": "Squat",
                "musclegroup": "Legs",
                "difficultylevel": 3,
                "equipment": "Squat rack, Barbell",
                "description": None
            },
            {
                "exerciseid": 3,
                "name": "Deadlift",
                "musclegroup": "Back",
                "difficultylevel": 4,
                "equipment": "Barbell",
                "description": "Lift the barbell from the ground to hip level while keeping your back straight."
            },
            {
                "exerciseid": 4,
                "name": "Pull-up",
                "musclegroup": "Back",
                "difficultylevel": 3,
                "equipment": "Pull-up bar",
                "description": "Pull your body up until your chin clears the bar, then lower yourself back down."
            },
            {
                "exerciseid": 5,
                "name": "Shoulder Press",
                "musclegroup": "Shoulders",
                "difficultylevel": 2,
                "equipment": "Dumbbells, Barbell",
                "description": "Push weights directly overhead until arms are fully extended."
            },
            {
                "exerciseid": 6,
                "name": "Barbell Row",
                "musclegroup": "Back",
                "difficultylevel": 3,
                "equipment": "Barbell",
                "description": "Pull the barbell towards your lower chest while keeping your back straight."
            },
            {
                "exerciseid": 7,
                "name": "Bicep Curl",
                "musclegroup": "Arms",
                "difficultylevel": 2,
                "equipment": "Dumbbells, Barbell, EZ bar",
                "description": "Curl the weight upwards by bending your elbow while keeping your upper arm stationary."
            },
            {
                "exerciseid": 8,
                "name": "Barbell Roll",
                "musclegroup": "Back",
                "difficultylevel": 3,
                "equipment": "Barbell",
                "description": "Roll the barbell with your arms to work your back muscles."
            },
            {
                "exerciseid": 9,
                "name": "Lunges",
                "musclegroup": "Legs",
                "difficultylevel": 2,
                "equipment": "None",
                "description": "Step forward with one leg, lowering your hips until both knees are bent at about a 90-degree angle."
            },
            {
                "exerciseid": 10,
                "name": "Tricep Dip",
                "musclegroup": "Arms",
                "difficultylevel": 2,
                "equipment": "Parallel bars",
                "description": "Lower your body by bending your elbows until your upper arms are parallel to the ground, then push yourself back up."
            }
            # Add more exercise objects as needed
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
            {
                "workoutid": 5,
                "userid": 3,
                "name": "Wednesday morning workout",
                "starttime": None,
                "endtime": None,
                "notes": "Great session"
            },
            {
                "workoutid": 6,
                "userid": 3,
                "name": "Wednesday evening workout",
                "starttime": None,
                "endtime": None,
                "notes": "Feeling strong"
            },
            {
                "workoutid": 7,
                "userid": 4,
                "name": "Alex's Friday Workout",
                "starttime": None,
                "endtime": None,
                "notes": "Heavy lifting day"
            },
            {
                "workoutid": 8,
                "userid": 5,
                "name": "Emma's Yoga Session",
                "starttime": None,
                "endtime": None,
                "notes": "Relaxing and rejuvenating"
            },
            {
                "workoutid": 9,
                "userid": 6,
                "name": "Mike's Run",
                "starttime": None,
                "endtime": None,
                "notes": "5-mile run in the park"
            },
            {
                "workoutid": 10,
                "userid": 7,
                "name": "Sarah's Pilates Class",
                "starttime": None,
                "endtime": None,
                "notes": "Core strengthening and flexibility"
            }
            # Add more workout objects as needed
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
            {
                "logid": 4,
                "exerciseid": 3,
                "workoutid": 4,
                "set": 5,
                "rep": 5,
                "weight": 220,
                "duration": 30
            },
            {
                "logid": 5,
                "exerciseid": 4,
                "workoutid": 5,
                "set": 4,
                "rep": 10,
                "weight": 0,
                "duration": 120
            },
            {
                "logid": 6,
                "exerciseid": 5,
                "workoutid": 6,
                "set": 5,
                "rep": 8,
                "weight": 40,
                "duration": 15
            },
            {
                "logid": 7,
                "exerciseid": 6,
                "workoutid": 7,
                "set": 4,
                "rep": 12,
                "weight": 120,
                "duration": 25
            },
            {
                "logid": 8,
                "exerciseid": 7,
                "workoutid": 8,
                "set": 5,
                "rep": 10,
                "weight": 20,
                "duration": 18
            },
            {
                "logid": 9,
                "exerciseid": 8,
                "workoutid": 9,
                "set": 4,
                "rep": 15,
                "weight": 60,
                "duration": 35
            },
            {
                "logid": 10,
                "exerciseid": 9,
                "workoutid": 10,
                "set": 3,
                "rep": 20,
                "weight": 0,
                "duration": 30
            }
            # Add more log objects as needed
        ]
    }
]


fake_data2 = [
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
    return getattr(metadata.tables[rel['table']].c, rel['column']) == base_id

def wrap_column(column):
    return db.func.concat('/api/', list(column.foreign_keys)[0].column.table.name, '/', column) if len(column.foreign_keys) > 0 else column

def handle_record(conn, table, result):
    if len(result) == 0: return result
    _id = result.get(f'{table}id')
    to_many = one_to_many.get(table, [])
    to_many_results = {
        to_many_field['name']: serialize_resource(conn, to_many_field['table'], handle_to_many(_id, to_many_field)) for to_many_field in to_many
    }
    return {**result, **to_many_results}

def serialize_resource(conn, table, _filter):
    sql_table = metadata.tables[table]
    columns = sql_table.c
    result = conn.execute(db.select(*[wrap_column(c) for c in columns]).where(_filter))
    result = result.all()
    results = [handle_record(conn, table, {
        c.name: row[cid] for cid, c in enumerate(columns)
        } if result is not None else {}) for row in result]
    return results

def get_id_given_name(username):
    engine = clean_and_create_cache_schema("fitness")
    query = "SELECT userid FROM user WHERE username = :username"
    stmt = db.text(query)
    with engine.connect() as conn:
        print(stmt)
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
        print(rows)
        return {'items': list(rows)}
    ...


def wrap_serialize(table, _id):
    engine = clean_and_create_cache_schema("fitness")
    with engine.connect() as conn:
        sql_table = metadata.tables[table]
        index = getattr(sql_table.c, f'{table}id')
        return serialize_resource(conn, table, index==_id)[0]
    
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

if __name__ == '__main__':
    #print(metadata.tables)
    generate_schema()
    engine = clean_and_create_cache_schema("fitness", True)
    metadata.create_all(engine)
    insert_test_data(engine)