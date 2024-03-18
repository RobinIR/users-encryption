import bcrypt
import json
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()

# key = Fernet.generate_key()
key = os.getenv('JWT_SECRET_KEY')
print(key)
cipher = Fernet(key) 
# Load the users.json file
with open("users.json", "r") as f:
    users = json.load(f)

# Encrypt the username and password values for each user
for user in users["users"]:
    user["username"] = cipher.encrypt(user["username"].encode('utf-8')).decode('utf-8')
    user["password"] = bcrypt.hashpw(user["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Write the encrypted users.json file
with open("users.json", "w") as f:
    json.dump(users, f)
