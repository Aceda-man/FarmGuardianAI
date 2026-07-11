import json
import os
import uuid


USER_FILE = "data/users.json"



def load_users():

    if os.path.exists(USER_FILE):

        with open(USER_FILE, "r") as file:

            return json.load(file)

    return []




def save_users(users):

    with open(USER_FILE, "w") as file:

        json.dump(
            users,
            file,
            indent=4
        )




def register_farmer(name, location):

    users = load_users()


    farmer_id = str(
        uuid.uuid4()
    )[:8]


    farmer = {

        "id": farmer_id,

        "name": name,

        "location": location

    }


    users.append(farmer)


    save_users(users)


    return farmer




def find_farmer(name, location):

    users = load_users()


    for farmer in users:


        if (

            farmer["name"].lower()
            ==
            name.lower()

            and

            farmer["location"].lower()
            ==
            location.lower()

        ):

            return farmer


    return None