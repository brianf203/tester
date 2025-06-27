from utils import hash_password
from models import User

def login_user(username, password, db_conn):
    hashed = hash_password(password)
    user = User(username, hashed)
    print(f"Logging in {user.username}")
    # Pretend to check user in db_conn
