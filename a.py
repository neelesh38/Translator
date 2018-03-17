import codecs
from googletrans import Translator
translator = Translator()
f = codecs.open('hindi.hi', mode="r", encoding="utf-8")
d = codecs.open('iitBhp.txt', mode="w", encoding="utf-8")
for line in f:
	translations = translator.translate([line], dest='pa')
        for translation in translations:
		d.write(translation.text)
		d.write('\n')
'''
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
hindi = ''
#f = codecs.open('out.txt', mode="w", encoding="iso-8859-1")
with open('a.txt') as fp:
    for line in fp:
        translations = translator.translate([line], dest='en')
        for translation in translations:
            print(translation)
            print(translation.origin, ' -> ', translation.text)
            hindi += translation.text        
    print(hindi)
text_file = open("h1.txt", "w",encoding='utf-8')
text_file.write(hindi)
text_file.close()
'''    
