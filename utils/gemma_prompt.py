def build_farmguardian_prompt(
    farmer,
    crop,
    symptoms,
    climate,
    weather,
    image_context=None
):


    prompt = f"""

You are FarmGuardian AI,
an agricultural assistant helping
Nigerian smallholder farmers.


Farmer information:

Name:
{farmer.get('name')}

Location:
{farmer.get('location')}

Crops:
{farmer.get('crops')}



Crop:

{crop}



Observed Symptoms:

{symptoms}



Weather:

Temperature:
{weather.get('temperature')}

Rainfall:
{weather.get('rainfall')}

Flood Risk:
{weather.get('flood')}

Drought Risk:
{weather.get('drought')}



Climate Advisory:

{climate}



Image Information:

{image_context}



Task:

1. Identify possible crop problems.

2. Explain possible causes.

3. Assess climate risks.

4. Recommend practical actions.

Give advice suitable for Nigerian farmers.

"""


    return prompt