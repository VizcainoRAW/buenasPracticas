from extensions import *

DATABASE_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': '3306',
    'database': 'TasksDB',
}

DB_URL = f"mysql+pymysql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

try:
    engine = create_engine(DB_URL)
    try:
       Session = sessionmaker(bind=engine)
       session = Session()
       print("Session made")
    except Exception as e:
        print(f"Session failed: {e}")
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")



