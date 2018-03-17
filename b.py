import codecs
from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
hindi = ''
f = codecs.open('ff.txt', mode="r", encoding="utf-8")
d = codecs.open('iitBeP.txt', mode="w", encoding="utf-8")

for line in f:
	translations = translator.translate([line], dest='pa')
	for translation in translations:
		d.write(translation.text)
		d.write('\n')
            
	
'''
with open('test.txt') as fp:
    for line in fp:
        translations = translator.translate([line], dest='pa')
        for translation in translations:
            #print(translation.origin, ' -> ', translation.text)
            hindi += translation.text        
    print(hindi)
text_file = open("hindi1.txt", "w",encoding="iso-8859-1")
text_file.write(hindi)
text_file.close()
'''    
