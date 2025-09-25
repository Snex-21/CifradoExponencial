from main import codificar, descodificador, presentacion
presentacion()
while True:
	#print('selecione una opcion:')
	print('[1] codificar texto\n[2] descodificar texto\n[3] terminar')
	eleccion = input('seleccione una opcion: ')
	if eleccion == '1':
		print('='*60+'\n')
		codi = codificar()
		print(f'tu frase codificada es:\n{codi}')
		print('\n'+'='*60)
	elif eleccion == '2':
		print('~•'*30+'\n')
		descodi = descodificador()
		print(f'tu frase descodificada es:\n{descodi}')
		print('\n'+'~•'*30)
	elif eleccion == '3':
		break
	else:
		print('tiene que ser un una de las opciones marcadas')

