import urllib.request

content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
content = str(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]

content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
content = str(content)
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao  + 4]


content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").read()
content = str(content)
find = 'xima">'
posicao = int(content.index(find) + len(find))
maxima = content[ posicao : posicao  + 2]

find = 'nima">'
posicao = int(content.index(find) + len(find))
minima = content[ posicao : posicao  + 2]


print("Dolar: " + dolar)
print("Euro: " + euro)
print("Temp. Maxima: " + maxima)
print("Temp. Minima: " + minima)

