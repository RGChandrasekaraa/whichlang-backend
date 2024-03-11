from langdetect import detect
import pycountry


def detect_language(text):
    try:
        # Detect the language code
        lang_code = detect(text)

        # Find the corresponding Language object and get its full name
        language = pycountry.languages.get(alpha_2=lang_code).name
        return language

    except Exception as e:
        return "Error detecting language"
