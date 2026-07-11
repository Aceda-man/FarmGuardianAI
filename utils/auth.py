import json
import os
import uuid
import hashlib


USER_FILE = "data/users.json"



# -----------------------------
# Password Security
# -----------------------------

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



# -----------------------------
# Load Users
# -----------------------------

def load_users():

    if os.path.exists(USER_FILE):

        with open(
            USER_FILE,
            "r"
        ) as file:

            return json.load(file)

    return []



# -----------------------------
# Save Users
# -----------------------------

def save_users(users):

    with open(
        USER_FILE,
        "w"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )



# -----------------------------
# Register New Farmer
# -----------------------------

def register_farmer(
    name,
    location,
    password,
    crops=None,
    farm_size=None,
    experience=None,
    language=None
):

    users = load_users()


    # Prevent duplicate accounts

    for user in users:

        if (
            user["name"].lower()
            ==
            name.lower()

            and

            user["location"].lower()
            ==
            location.lower()
        ):

            return None




    farmer = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "location": location,
        "password": hash_password(password),
        "crops": crops if crops is not None else [],
        "farm_size": farm_size,
        "experience": experience,
        "language": language,
    }

    users.append(
        farmer
    )


    save_users(
        users
    )


    return farmer



# -----------------------------
# Login Farmer
# -----------------------------

def login_farmer(
    name,
    password
):

    users = load_users()


    hashed_password = hash_password(
        password
    )



    for farmer in users:


        if (

            farmer["name"].lower()
            ==
            name.lower()

            and

    
            farmer["password"]
            ==
            hashed_password

        ):

            return farmer



    return None