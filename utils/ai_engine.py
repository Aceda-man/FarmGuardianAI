import random


def farmguardian_ai_response(prompt):

    """
    Temporary FarmGuardian AI reasoning engine.

    This will be replaced with Gemma 4
    during the competition.
    """



    prompt_lower = prompt.lower()



    # -----------------------------
    # Tomato Example
    # -----------------------------

    if "tomato" in prompt_lower:


        return {

            "analysis":
            """
Possible tomato stress detected.

The symptoms may be related to:

• Tomato yellow leaf curl virus
• Nutrient deficiency
• Water stress

Further image reasoning from Gemma 4
will improve confidence.
            """,


            "risk":
            "Medium - Monitor crop closely",


            "climate_warning":
            """
High temperature and irregular rainfall
can increase tomato stress and disease pressure.
            """,


            "recommendations":

            [

                "Remove severely infected plants",

                "Avoid waterlogging around roots",

                "Monitor insect vectors such as whiteflies",

                "Apply balanced fertilizer based on soil condition"

            ]

        }




    # -----------------------------
    # Maize Example
    # -----------------------------


    elif "maize" in prompt_lower:


        return {


            "analysis":

            """
Possible maize health problem detected.

Likely causes:

• Fall armyworm infestation
• Nitrogen deficiency
• Drought stress

            """,


            "risk":

            "High - Immediate field inspection recommended",



            "climate_warning":

            """
Dry conditions combined with high temperature
may increase crop stress.
            """,



            "recommendations":

            [

                "Inspect leaves for armyworm damage",

                "Improve nutrient management",

                "Maintain proper soil moisture",

                "Remove heavily damaged plants"

            ]

        }





    # -----------------------------
    # Cassava Example
    # -----------------------------


    elif "cassava" in prompt_lower:


        return {


            "analysis":

            """
Possible cassava disease detected.

Common concerns:

• Cassava mosaic disease
• Cassava bacterial blight

            """,


            "risk":

            "Medium",


            "climate_warning":

            """
High humidity may increase disease spread.
            """,


            "recommendations":

            [

                "Use disease-free planting materials",

                "Remove infected plants",

                "Monitor nearby cassava fields"

            ]

        }





    # -----------------------------
    # GENERAL RESPONSE
    # -----------------------------


    else:


        return {


            "analysis":

            """
FarmGuardian AI detected a possible crop health issue.

More information is needed for accurate diagnosis.

Please provide:

• Crop type

• Clear symptoms

• Weather conditions

• Crop image

            """,



            "risk":

            "Unknown",



            "climate_warning":

            """
Climate information will help determine
possible environmental stress.
            """,



            "recommendations":

            [

                "Provide clearer crop symptoms",

                "Upload a better crop image",

                "Check field conditions"

            ]

        }