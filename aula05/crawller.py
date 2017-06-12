import urllib.request

def getDolar():
    content = urllib.request.urlopen("https://www.melhorcambio.com/dolar-hoje").read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    dolar = content[ posicao : posicao  + 4]
    return dolar

def getEuro():
    content = urllib.request.urlopen("https://www.melhorcambio.com/euro-hoje").read()
    content = str(content)
    find = '<input type="hidden" value="'
    posicao = int(content.index(find) + len(find))
    euro = content[ posicao : posicao  + 4]
    return euro

def getTemperatura():
    content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/88/goiania-go").read()
    content = str(content)
    find = 'xima">'
    posicao = int(content.index(find) + len(find))
    maxima = content[ posicao : posicao  + 2]

    find = 'nima">'
    posicao = int(content.index(find) + len(find))
    minima = content[ posicao : posicao  + 2]
    return [minima, maxima]




