import json


def load_crop_database():

    with open(
        "data/crop_database.json",
        "r"
    ) as file:

        return json.load(file)



def analyze_crop_problem(crop, description):

    database = load_crop_database()

    crop_info = database.get(crop)

    if not crop_info:
        return None


    description = description.lower()


    results = []


    for problem in crop_info["problems"]:

        score = 0


        for symptom in problem["symptoms"]:

            if any(
                word in description
                for word in symptom.lower().split()
            ):
                score += 1


        results.append(
            {
                "problem": problem,
                "score": score
            }
        )


    results.sort(
        key=lambda x:x["score"],
        reverse=True
    )


    return results[0]["problem"]