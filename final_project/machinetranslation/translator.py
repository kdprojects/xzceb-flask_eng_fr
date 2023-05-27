import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apiKey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

TRANSLATOR_OPT= {
    "EN_FR":"en-fr",
    "FR_EN":"fr-en"
}

# models = language_translator.list_models().get_result()
# print(json.dumps(models, indent=2))

def translate(text, direction):
    translation = None
    
    try:
        # Invoke a method
        translation = language_translator.translate(
            text=text,
            model_id=direction).get_result()
        # print(json.dumps(translation, indent=2, ensure_ascii=False))

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
        return "Method fail"

    return translation["translations"][0]["translation"]

def englishToFrench(englishText):
    #write the code here
    frenchText = translate(englishText, TRANSLATOR_OPT["EN_FR"])
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = translate(frenchText, TRANSLATOR_OPT["FR_EN"])
    return englishText