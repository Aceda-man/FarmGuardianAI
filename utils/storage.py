import json
import os
from datetime import datetime


HISTORY_FILE = "data/history.json"



# =========================
# CREATE DATA FOLDER
# =========================

def ensure_storage():

    folder = os.path.dirname(HISTORY_FILE)

    if not os.path.exists(folder):

        os.makedirs(folder)



# =========================
# LOAD ALL HISTORY
# =========================

def load_data():

    ensure_storage()


    if not os.path.exists(HISTORY_FILE):

        return []


    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)




# =========================
# SAVE DIAGNOSIS
# =========================

def save_diagnosis(
    farmer_id,
    crop,
    problem,
    ai_result
):


    history = load_data()


    diagnosis = {

        "farmer_id": farmer_id,

        "crop": crop,

        "problem": problem,

        "analysis": ai_result.get(
            "analysis",
            ""
        ),

        "risk": ai_result.get(
            "risk",
            ""
        ),

        "climate_warning": ai_result.get(
            "climate_warning",
            ""
        ),

        "recommendations": ai_result.get(
            "recommendations",
            []
        ),

        "date": datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

    }



    history.append(
        diagnosis
    )


    ensure_storage()


    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(
            history,
            file,
            indent=4
        )




# =========================
# LOAD FARMER HISTORY ONLY
# =========================

def load_history(farmer_id):


    history = load_data()


    farmer_history = []


    for item in history:


        if item.get(
            "farmer_id"
        ) == farmer_id:


            farmer_history.append(
                item
            )


    return farmer_history