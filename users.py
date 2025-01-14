import hashlib
import uuid

# In-memory user database
users_db = {}

def hash_password(password):
    salt = uuid.uuid4().hex
    hashed_pw = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_pw, salt

def verify_password(stored_password, salt, provided_password):
    return stored_password == hashlib.sha256((provided_password + salt).encode()).hexdigest()

def create_user(username, password):
    if username in users_db:
        return {"error": "Username already exists"}
    hashed_pw, salt = hash_password(password)
    users_db[username] = {"password": hashed_pw, "salt": salt}
    return {"message": "User created successfully"}

def authenticate_user(username, password):
    user = users_db.get(username)
    if not user:
        return False
    return verify_password(user["password"], user["salt"], password)
