from funcionesContactManager import *



favoriteContactDelete = 'davidcorzo'

favorites = {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'},'stevenwilson':{'nombre':'Steven','apellido':'Wilson','telefono': '12121212'}}
diccinario = {}
diccionarioMaestro = {'davidcorzo':{'nombre':'David','apellido':'Corzo','telefono':'30177050'}, 'favorites': {}}
# 'davidcorzo':{'nombre':'David','apellido':'Corzo','telefono':'30177050'}, 'favorites': {'davidcorzo': {'nombre': 'David', 'apellido': 'Corzo', 'telefono': '30177050'}}
# removeFromFavorites11(favoriteContactDelete,favorites,diccionarioMaestro)





newFileName = str(input('Ingrese el nombre de su archivo: (No olvide ponerle extensión) → '))
exportacionDeLaDataAUnArchivoNuevo16(diccionarioMaestro,favorites,newFileName)

