import json
from random import randrange

with open('full%2Fsimplified%2Fairplane2.json', "r+") as contenido:
	archivos =json.load(contenido)
	for archivo in archivos:
		archivo['cx'] = randrange(100)
		archivo['cy'] = randrange(100)
	contenido.seek(0)  # rewind
   	json.dump(archivos, contenido)
   	contenido.truncate()
			#print(archivo.get('word'))


#ruta='full%2Fsimplified%2Fairplane2.json'
#cargar_datos(ruta)

#print "Leer archivos"
#leer = json.load(open('full%2Fsimplified%2Fairplane2.json'))
#print leer

#print "Imprimir elemento isActive"
#leer[0]['cx'] = 50
#print leer[0]['cx']
#print leer[0]
#json.dump(leer, 'full%2Fsimplified%2Fairplane2.json')
