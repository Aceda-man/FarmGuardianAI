# =====================================================
# FarmGuardian AI
# Climate Risk Knowledge Base
# SDG 11 & 13 - Climate Resilient Communities
# =====================================================


CLIMATE_DATABASE = {


    "Kwara": {

        "zone": "North Central",

        "risks": [

            "Heat stress",
            "Dry spells",
            "Erratic rainfall"

        ],

        "crop_risks": {

            "Maize": [

                "Poor pollination during high temperature",
                "Leaf rolling due to moisture stress"

            ],

            "Cassava": [

                "Reduced root development during drought"

            ],

            "Rice": [

                "Water shortage during grain filling"

            ]

        },


        "recommendations": [

            "Apply mulch to conserve soil moisture",

            "Plant early with the onset of rainfall",

            "Monitor soil moisture regularly",

            "Use drought tolerant varieties where available"

        ]

    },




    "Lagos": {

        "zone": "South West",

        "risks": [

            "Flooding",
            "High humidity",
            "Disease outbreaks"

        ],


        "crop_risks": {


            "Rice": [

                "Flood damage",
                "Fungal disease pressure"

            ],


            "Vegetables": [

                "Leaf diseases due to high humidity"

            ]

        },


        "recommendations": [

            "Improve farm drainage",

            "Avoid excessive irrigation",

            "Monitor fungal diseases",

            "Maintain proper plant spacing"

        ]

    },





    "Oyo": {

        "zone": "South West",

        "risks": [

            "Erratic rainfall",
            "Pest outbreaks"

        ],


        "crop_risks": {


            "Maize": [

                "Fall armyworm outbreaks",
                "Moisture stress"

            ],


            "Cassava": [

                "Cassava mosaic disease risk"

            ]

        },


        "recommendations": [

            "Inspect crops weekly",

            "Remove infected plants",

            "Maintain good field sanitation"

        ]

    },





    "Kaduna": {

        "zone": "North West",

        "risks": [

            "Drought",
            "High temperature",
            "Water scarcity"

        ],


        "crop_risks": {


            "Sorghum": [

                "Heat stress during flowering"

            ],


            "Maize": [

                "Reduced yield from moisture shortage"

            ]

        },


        "recommendations": [

            "Practice water conservation",

            "Use early maturing varieties",

            "Plant according to rainfall forecast"

        ]

    },





    "Rivers": {

        "zone": "South South",

        "risks": [

            "Flooding",
            "Waterlogging",
            "High humidity"

        ],


        "crop_risks": {


            "Cassava": [

                "Root damage from waterlogging"

            ],


            "Vegetables": [

                "Fungal disease increase"

            ]

        },


        "recommendations": [

            "Create drainage channels",

            "Avoid planting in flood-prone areas",

            "Monitor fungal infections"

        ]

    }


}




def get_climate_data(location):

    """
    Returns climate information
    based on farmer location.
    """


    location = location.strip().title()


    if location in CLIMATE_DATABASE:

        return CLIMATE_DATABASE[location]


    return {


        "zone": "Unknown",

        "risks": [

            "Climate uncertainty"

        ],


        "crop_risks": {},


        "recommendations": [

            "Monitor weather changes",

            "Maintain good farm practices"

        ]

    }