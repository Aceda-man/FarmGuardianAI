import json
import os
from datetime import datetime


HISTORY_FILE = "data/history.json"



def save_diagnosis(
    farmer,
    location,
    crop,
    problem,
    result
):

    record = {

        "date":
        str(datetime.now()),

        "farmer":
        farmer,

        "location":
        location,

        "crop":
        crop,

        "problem":
        problem,

        "diagnosis":
        result["name"],

        "type":
        result["type"]

    }


    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            history = json.load(file)

    else:

        history = []


    history.append(record)


    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )



def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)


    return []