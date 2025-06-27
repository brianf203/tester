from auth import login_user
from db import connect_db
from utils import print_welcome

def main():
    print_welcome()
    conn = connect_db()
    login_user("admin", "secret", conn)

if __name__ == "__main__":
    main()
