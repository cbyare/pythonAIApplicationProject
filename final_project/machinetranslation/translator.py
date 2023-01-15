import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
#this set up for authentication
authenticator = IAMAuthenticator(apikey)
#adding instance of IBM Watson language transalator
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
#setting up the url 
language_translator.set_service_url(url)

def englishToFrench(english_text):
    #write the code here
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    english_text =translation.translations[0]
    return english_text

def frenchToEnglish(french_text):
    #write the code here
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    french_text =translation.translations[0]
    return french_text
    