import json
import os



def save_diagnosis(
    farmer_id,
    crop,
    problem,
    result
):

    folder = "data/farmers"


    os.makedirs(
        folder,
        exist_ok=True
    )


    file_path = (
        f"{folder}/{farmer_id}.json"
    )


    record = {

        "crop": crop,

        "problem": problem,

        "diagnosis": result["name"],

        "type": result["type"]

    }


    if os.path.exists(file_path):

        with open(file_path,"r") as file:

            history=json.load(file)

    else:

        history=[]


    history.append(record)


    with open(file_path,"w") as file:

        json.dump(
            history,
            file,
            indent=4
        )





def load_history(farmer_id):

    file_path = (
        f"data/farmers/{farmer_id}.json"
    )


    if os.path.exists(file_path):

        with open(file_path,"r") as file:

            return json.load(file)


    return []