import rtx_api_4_24 as rtx_api
from googletrans import Translator

def translate_text(text, src="en", dest="es"):
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    return translation.text


def get_resume(text):
    if text == "":
        return
    
    template = 'based on the following headers, make a resume parragraf alike of 150 word tring to guess what the text is about, with out mention that you are besed on header "{0}"'.format(text)
    print(template)

    response = rtx_api.send_message(template)

    return translate_text(response)