#diccionario con todas las potencias
#se hace la potencia, se pasa a str y se rellena con ceros si faltan digitos (el uso del metodo .zfill(5)
codigos = {
    'a': str(7**1).zfill(5), #00007 aca se rellena con 4 ceros que sonnlos digitos que faltan
    'b': str(6**1).zfill(5),
    'c': str(5**1).zfill(5),
    'd': str(7**2).zfill(5),
    'e': str(6**2).zfill(5), #00036 aca con 3 ceros
    'f': str(5**2).zfill(5),
    'g': str(4**2).zfill(5),
    'h': str(3**2).zfill(5),
    'i': str(7**3).zfill(5),
    'j': str(6**3).zfill(5),
    'k': str(5**3).zfill(5),
    'l': str(4**3).zfill(5),
    'm': str(3**3).zfill(5),
    'n': str(7**4).zfill(5), #02401 aca con un solo cero
    'ñ': str(6**4).zfill(5),
    'o': str(5**4).zfill(5),
    'p': str(4**4).zfill(5),
    'q': str(3**4).zfill(5),
    'r': str(7**5).zfill(5), #16807 aca no se rellena
    's': str(6**5).zfill(5),
    't': str(5**5).zfill(5),
    'u': str(4**5).zfill(5),
    'v': str(3**5).zfill(5),
    'w': str(6**6).zfill(5),
    'x': str(5**6).zfill(5),
    'y': str(4**6).zfill(5),
    'z': str(3**6).zfill(5),
    ' ': str(9**4).zfill(5),
    ',': str(4**7).zfill(5),
    '.': str(8**5).zfill(5),
    '?': str(2**11).zfill(5),
    '!': str(11**3).zfill(5)
}

#funcion para codificar
def codificar():
	#texto del usuria pasado a minuscula (por las dudas)
	texto = input('texto a codificar: ').lower()
	frase = ''
	#agarra una letra, la busca en el diccionario, pone su version en numeros, lo suma al str
	for letra in texto:
		frase += codigos[letra]
	return frase

codigos_inversos = {}
#bucle para invertir los keys values del diccionario
for letra, valor in codigos.items():
	codigos_inversos[valor] = letra

#funcion para descodificar
def descodificador():
	texto_codificado = input('texto codificado: ')
	texto_decodificado = ''
	#bucle que empueza desde cero, termina en la cantidad de len y se va saltando de 5 en 5 (0, 5, 10, etc)
	for i in range(0, len(texto_codificado), 5):
		bloque = texto_codificado[i:i+5]
		#busca el valor, de esos 5 digitos,para pasar la letra
		letras = codigos_inversos[bloque]
		#sumamos la letra a un str
		texto_decodificado += letras
	return texto_decodificado

import os
def presentacion():
        os.system('clear')
        print('—'*60)
        print('–'*20 + '·Cifrado Exponencial·' + '–'*19)
        print('—'*60)

