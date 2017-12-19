// pip (python installer package)
// pip3.5.exe install pygame // usado para instalar pacotes
// www.lfd.uci.edu/~gohlke/pythonlibs/ <!-- muitas bibliotecas prontas -->

type(variavel) // informa o tipo 
type(variavel), type(variavel) // exibe mais de um

a = ["A", "b", true, 3, 1.4] // vetor aceita tipos diferentes
print (a[2])
>>> true

a='laranja'
a.upper()
>>> 'LARANJA'

dir(a) // mostra funções do objeto

a, b = 1, 2.5
print(a)
>>> 1
print(b)
>>> 2.5

a=0o11
>>> 9
b=0b1001
>>> 9
c=0x010
>>> 16

_+2 // pega o ultimo resultado e soma + 2

type (_) // retorno tipo da ultima instrução

a = 3 + 4j
type (a)
>>> complex
a.real
>>> 3.0

number[1,2,3]
name['luis', 'jose', 'voce']
mix[1,2,3,'luidi', 'joseph', 'you']
lista[number, name, mix]

lista
>>> name[['luis', 'jose', 'voce'], name['luis', 'jose', 'voce'], mix[1,2,3,'luidi', 'joseph', 'you']]
lista[0][2]
>>> 'voce'
len(number)
>>> 3

numeros=[1,2,3]
numeros[0]
>>> 1
numeros[-1]
>>> 3

n=[0,1,2,3,4,5,6,7,8,9]
n[2:6]
>>> [3,4,5] (pega somento o meio)

n.append(3) //adiciona ao final do array/slice
n.sort() //organiza em ordem crescente
n.reverse() // ordem decrescente

n.pop() //tira o ultimo item do array
ultimo = n.pop() //armazena em 'ultimo' o ultimo item de 'n'

n=[1,2,3]
m=[7,8,9]
n.extend(m) // adiciona 'm' ao final de 'n'
n
>>> [1,2,3,7,8,9]
n.insert(2, 'ola') // insere apos a posição '2' iniciando em '1'
n
>>> [1, 2, 'ola', 3, 9, 8, 7]
n.remove(9) // remove extamente o valor '9'
n.index(8) // devolve o indice onde esta o '8'
n.count(7) // devolve quantos elementos '7' tem no array

T = (1,2,3) // cria tupla. Tupla uma vez criada nao pode ser alterada
dir(T) // exibe todos os methods para 'T'

D = {"jose":99999, "paty":987655, "hugo":34566, "voce":89371538 }
D["jose"]
>>> 99999
D.keys() //exibe os nomes
D.values() // exibe os valores
D.items () // exibe tudo
D.clear() // apaga tudo de 'D'

a,b = 5,3 // a=5; b=3
c = a if a > b else b // Se 'a' for maior que 'b' 'c=a' Senao 'c=b'

for i in range(26): print(chr(65+i) //exibe alfabeto 'chr(65) exibe letra 'A''

 #################################################################

Programas

a=5; b=8
if a > b:
    print("A é maior que B")
    c = "maior"
elif a == b:
    print("B é igual que A")
    c = "igual"
else:
    print("A é menor que B")
    c = "menor"
print(a,b,c)

 #################################################################
 
 // exibe cada letra em uma linha
 palavra='cachorro'
for aux in palavra:
    print(aux)

#################################################################

// exibe só os mumeros pares
for numero in range(10):
    if numero % 2 == 0:
        print(numero)

#################################################################

// começa de 1 até 10 pulando de 2 em 2
for numero in range(1,10,2):
    print(numero)
    
#################################################################

#cria uma lista/array das palavras separadas por espaço
naipes  = 'copas ouros espadas paus'.split() 
cartas  = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
#Cria lista dos baralhos
baralho = [ (c, n) for n in naipes for c in cartas]
print(baralho)
print(len(baralho))

RESULTADO
[('A', 'copas'), ('2', 'copas'), ('3', 'copas'), ('4', 'copas'), ('5', 'copas'), ('6', 'copas'), ('7', 'copas'), ('8', 'copas'), ('9', 'copas'), ('10', 'copas'), ('J', 'copas'), ('Q', 'copas'), ('K', 'copas'), ('A', 'ouros'), ('2', 'ouros'), ('3', 'ouros'), ('4', 'ouros'), ('5', 'ouros'), ('6', 'ouros'), ('7', 'ouros'), ('8', 'ouros'), ('9', 'ouros'), ('10', 'ouros'), ('J', 'ouros'), ('Q', 'ouros'), ('K', 'ouros'), ('A', 'espadas'), ('2', 'espadas'), ('3', 'espadas'), ('4', 'espadas'), ('5', 'espadas'), ('6', 'espadas'), ('7', 'espadas'), ('8', 'espadas'), ('9', 'espadas'), ('10', 'espadas'), ('J', 'espadas'), ('Q', 'espadas'), ('K', 'espadas'), ('A', 'paus'), ('2', 'paus'), ('3', 'paus'), ('4', 'paus'), ('5', 'paus'), ('6', 'paus'), ('7', 'paus'), ('8', 'paus'), ('9', 'paus'), ('10', 'paus'), ('J', 'paus'), ('Q', 'paus'), ('K', 'paus')]
52

#################################################################

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b
        
#################################################################

-------------------------------------------------------------------------------------------

// tratando erro
a = [1,2,3]
try:
    print(a[5])
except IndexError:
    print("Erro ao tentar acessar o indice 5")

-----------------------------------------------------------------------------------

// semelhante ao foreach
def media(*valores): // permite nao definir quantos elementos virão
    soma=0.
    for n in valores: // para cada valor de 'valores' é adicionado em n
        soma += n
    return soma/len(valores)

--------------------------------------------------------------------------------------

// entradas
nome=input("Digite seu nome:") // string
idade=int(input("Digite sua idade:")) // numeral

-------------------------------------------------------------------------------

// desenho circulo com turtle
import turtle
pen = turtle.Pen()
pen.circle(100)

---------------------------------------------------------

// desenho circulo modo hardwork
import turtle
pen = turtle.Pen()
for i range(360)
  pen.forward(1)
  pen.left(1)
  
--------------------------------------------------------------------

// soma a media de 4 numeros
n=[]
for i in range(4):
    n.append(int(input("Digite um numero: ")))
print(sum(n)/len(n))

--------------------------------------------------------------------------------

import random
random.randint(1,100)
>> 98
                          
lista=(1,2,3,4,5)
random.choice(lista)
>> 4
                          
----------------------------------------------------------------------------
// criptografa para chines
                          
def esconde(msg):
    s = ''
    for c in msg: s += chr(ord(c)+ 30000)
    return s

def mostra(msg):
    s = ''
    for c in msg: s += chr(ord(c) - 30000)
    return s
            
--------------------------------------------------------------------------------------

// criar servidor web http e exibe 'hello world'                          
from http.server import BaseHTTPRequestHandler, HTTPServer

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "<marquee>Hello World</marquee>"
        self.wfile.write(bytes(message,"utf8"))
        return

def run():
    print("Servidor up...")

    server_address = ('127.0.0.1',80)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("Servidot Funfou...")
    httpd.serve_forever()

run()                          

                          
