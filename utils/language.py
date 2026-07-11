# =====================================================
# FarmGuardian AI
# Language Processing Layer
# =====================================================


def detect_language(text):

    """
    Basic language detector placeholder.

    Future:
    Gemma 4 multilingual reasoning
    """


    text = text.lower()


    yoruba_words = [
        "mo",
        "emi",
        "oko",
        "ewé",
        "irugbin",
        "arun"
    ]


    hausa_words = [
        "noma",
        "shuka",
        "ruwa",
        "kwari"
    ]


    igbo_words = [
        "ugbo",
        "osisi",
        "mmiri",
        "ahihia"
    ]



    for word in yoruba_words:

        if word in text:

            return "Yoruba"



    for word in hausa_words:

        if word in text:

            return "Hausa"



    for word in igbo_words:

        if word in text:

            return "Igbo"



    return "English"





def translate_to_english(text, language):


    """
    Translation placeholder.

    Gemma 4 will handle
    multilingual understanding.
    """


    if language == "English":

        return text



    return f"""
Translated farmer message:

{text}

Detected language:
{language}

"""





def simplify_response(response, language):


    """
    Converts technical AI output
    into farmer-friendly explanation.
    """


    if language == "English":

        return response



    return f"""

Farmer friendly explanation:

{response}

Language:
{language}

"""