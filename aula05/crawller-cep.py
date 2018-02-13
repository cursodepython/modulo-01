from urllib.parse import urlencode
from urllib.request import Request, urlopen

def unescapeXml(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    s = s.replace("&amp;", "&")
    s = s.replace("&nbsp;", " ")
    return s

def unescapeString(s):
    s = s.replace('\\r', '')
    s = s.replace('\\t', '')
    s = s.replace('\\n', '')
    return s



url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
post_fields = {'relaxation': '74740110', 'tipoCEP': 'ALL', 'semelhante': 'N'}

request = Request(url, urlencode(post_fields).encode())
result = urlopen(request).read()
result = str(result)

result = unescapeString(result)
result = bytes(result, "iso-8859-1").decode("unicode_escape")
result = unescapeXml(result)

find = 'CEP:</th>'
posicao = int(result.index(find) + len(find))
result = result[ posicao : posicao  + 200]

findInicio = '<td width="150">'
findFim = '</td><td width="90">'
posicaoInicio = int(result.index(findInicio) + len(findInicio))
posicaoFim = int(result.index(findFim))
logradouro = result[ posicaoInicio : posicaoFim]

findInicio = '</td><td width="90">'
findFim = '</td><td width="80">'
posicaoInicio = int(result.index(findInicio) + len(findInicio))
posicaoFim = int(result.index(findFim))
bairro = result[ posicaoInicio : posicaoFim]

findInicio = '</td><td width="80">'
findFim = '</td><td width="55">'
posicaoInicio = int(result.index(findInicio) + len(findInicio))
posicaoFim = int(result.index(findFim))
cidade = result[ posicaoInicio : posicaoFim]


print("Logradouro: {0}".format(logradouro))
print("Bairro: {0}".format(bairro))
print("Cidade: {0}".format(cidade))
