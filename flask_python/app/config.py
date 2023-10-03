from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': '3306',
    'database': 'TasksDB',
}


DB_URL = f"mysql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)





