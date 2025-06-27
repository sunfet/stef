from googletrans import Translator
translator = Translator()
result = translator.translate('Hello', dest='zh-cn')
print(result.text)