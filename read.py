import codecs
f = codecs.open('IITB.en-hi.en', mode="r", encoding="utf-8")
d = codecs.open('ff.txt', mode="w", encoding="utf-8")
for line in f:
	a=len(line.split())
	if(a>8):
		d.write(line)
