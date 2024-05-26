from googletrans import Translator

translator = Translator()


def translate_text(text: str, suffix: str):
    result = translator.translate(text, dest=suffix)
    print(result.text)

translate_text('Привет', 'en')
translate_text('Привет', 'fr')
translate_text('Привет', 'it')





