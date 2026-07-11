# =====================================================
# FarmGuardian AI
# Climate Advisory Generator
# =====================================================


from utils.climate import get_climate_data




def generate_advisory(
    location,
    crops
):


    climate = get_climate_data(
        location
    )


    advisory = {


        "location": location,


        "zone": climate["zone"],


        "risks": climate["risks"],


        "recommendations": climate["recommendations"],


        "crop_advice": []

    }



    for crop in crops:


        if crop in climate["crop_risks"]:


            advisory["crop_advice"].append(

                {

                "crop": crop,

                "risks":
                climate["crop_risks"][crop]

                }

            )


    return advisory