#diccionario con todas las potencias
#se hace la potencia, se pasa a str y se rellena con ceros si faltan digitos (el uso del metodo .zfill(5) )
codigos = {
#Letras minúsculas del alfabeto español
    'a': str(2**2).zfill(5), #00004 aca se rellena con 4 ceros que son los digitos que faltan
    'b': str(3**2).zfill(5),
    'c': str(2**3).zfill(5),
    'd': str(4**2).zfill(5), #00016 aca con 3 ceros
    'e': str(2**4).zfill(5),
    'f': str(5**2).zfill(5),
    'g': str(3**3).zfill(5),
    'h': str(2**5).zfill(5),
    'i': str(6**2).zfill(5),
    'j': str(7**2).zfill(5),
    'k': str(8**2).zfill(5),
    'l': str(2**6).zfill(5),
    'm': str(3**4).zfill(5),
    'n': str(9**2).zfill(5),
    'ñ': str(10**2).zfill(5),
    'o': str(11**2).zfill(5),
    'p': str(12**2).zfill(5),
    'q': str(2**7).zfill(5),
    'r': str(13**2).zfill(5),
    's': str(14**2).zfill(5),
    't': str(15**2).zfill(5),
    'u': str(16**2).zfill(5),
    'v': str(2**8).zfill(5),
    'w': str(3**5).zfill(5),
    'x': str(17**2).zfill(5),
    'y': str(18**2).zfill(5),
    'z': str(19**2).zfill(5),
#Espacio en blanco
    ' ': str(6**3).zfill(5),
#Signos de puntuación
    ',': str(20**2).zfill(5),
    '.': str(21**2).zfill(5),
    ';': str(45**2).zfill(5),
    ':': str(46**2).zfill(5),
    '"': str(47**2).zfill(5),
    "'": str(48**2).zfill(5),
    '`': str(49**2).zfill(5),
    '«': str(50**2).zfill(5),
    '»': str(15**3).zfill(5),
    '(': str(7**4).zfill(5),
    ')': str(51**2).zfill(5),
    '[': str(52**2).zfill(5),
    ']': str(53**2).zfill(5),
    '{': str(54**2).zfill(5),
    '}': str(55**2).zfill(5),
    '-': str(56**2).zfill(5),
    '—': str(57**2).zfill(5),
    '¿': str(9**3).zfill(5),
    '?': str(22**2).zfill(5),
    '¡': str(8**3).zfill(5),
    '!': str(7**3).zfill(5),
#Letras mayúsculas del alfabeto español
    'A': str(23**2).zfill(5),
    'B': str(24**2).zfill(5),
    'C': str(25**2).zfill(5),
    'D': str(26**2).zfill(5),
    'E': str(27**2).zfill(5),
    'F': str(3**6).zfill(5),
    'G': str(8**3).zfill(5),
    'H': str(28**2).zfill(5),
    'I': str(29**2).zfill(5),
    'J': str(30**2).zfill(5),
    'K': str(31**2).zfill(5),
    'L': str(32**2).zfill(5),
    'M': str(2**10).zfill(5),
    'N': str(33**2).zfill(5),
    'Ñ': str(34**2).zfill(5),
    'O': str(35**2).zfill(5),
    'P': str(36**2).zfill(5),
    'Q': str(6**4).zfill(5), #01296 aca con un solo cero
    'R': str(37**2).zfill(5),
    'S': str(38**2).zfill(5),
    'T': str(39**2).zfill(5),
    'U': str(40**2).zfill(5),
    'V': str(41**2).zfill(5),
    'W': str(42**2).zfill(5),
    'X': str(43**2).zfill(5),
    'Y': str(44**2).zfill(5),
    'Z': str(14**3).zfill(5),
#Caracteres especiales (los mas comunes)
    '@': str(58**2).zfill(5),
    '#': str(59**2).zfill(5),
    '$': str(60**2).zfill(5),
    '%': str(61**2).zfill(5),
    '&': str(62**2).zfill(5),
    '*': str(63**2).zfill(5),
    '/': str(64**2).zfill(5),
    '\\': str(2**12).zfill(5), #barra invertida doble que significa barra normal para que no haya error de unicode
    '|': str(11*3).zfill(5),
    '_': str(65**2).zfill(5),
    '+': str(66**2).zfill(5),
    '=': str(67**2).zfill(5),
    '<': str(68**2).zfill(5),
    '>': str(69**2).zfill(5),
    '^': str(70**2).zfill(5),
    '~': str(71**2).zfill(5),
    '°': str(72**2).zfill(5),
    '¬': str(73**2).zfill(5),
    '¶': str(74**2).zfill(5),
    '§': str(75**2).zfill(5),
    '·': str(76**2).zfill(5),
    '©': str(77**2).zfill(5),
    '®': str(78**2).zfill(5),
    '™': str(79**2).zfill(5),
    '€': str(80**2).zfill(5),
    '¢': str(81**2).zfill(5),
    '¥': str(3**8).zfill(5),
#Letras con tilde o diéresis (minúsculas y mayúsculas)
    'á': str(82**2).zfill(5),
    'é': str(83**2).zfill(5),
    'í': str(41**3).zfill(5),
    'ó': str(84**2).zfill(5),
    'ú': str(85**2).zfill(5),
    'ü': str(86**2).zfill(5),
    'Á': str(42**3).zfill(5),
    'É': str(87**2).zfill(5),
    'Í': str(88**2).zfill(5),
    'Ó': str(89**2).zfill(5),
    'Ú': str(43**3).zfill(5),
    'Ü': str(90**2).zfill(5),
#Dígitos numéricos
    '0': str(91**2).zfill(5),
    '1': str(92**2).zfill(5),
    '2': str(93**2).zfill(5),
    '3': str(94**2).zfill(5),
    '4': str(95**2).zfill(5),
    '5': str(45**3).zfill(5),
    '6': str(96**2).zfill(5),
    '7': str(97**2).zfill(5),
    '8': str(98**2).zfill(5),
    '9': str(99**2).zfill(5)
}


#funcion para codificar
def codificar():
	#texto del usuria pasado a minuscula (por las dudas)
	texto = input('texto a codificar: ')
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

