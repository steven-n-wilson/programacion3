# import pprint
import colorama
import sys, traceback
import sys, time
import os
import csv
import requests




def Esthetics1():
    """Imprime una linea en blanco"""
    print('')
    

def produceContactID2(nombre,apellido):
    """Crea el contactID, le da retur a key. Utiliza el nombre y apellido con lower"""
    nombre = nombre.lower()
    apellido = apellido.lower()
    key=str(nombre) + str(apellido)
    return key

def pprint(diccionario):
    """Pretty print, imprime el diccionario ordenado y separado por categoria"""
    for key, value in diccionario.items():
        print('')
        print("ContactID:", key)
        for key, value in value.items():
            print(key,value)
        
#################################################################################################################################################################################
#FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #
#################################################################################################################################################################################
#FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #FASE 1 #
#################################################################################################################################################################################
def documentacionDeLaFase1():
    '''
    Fase 1:
    1. addContact: Nombre, Apellido y Telefono 
    2. listContacts:  “pretty”
    3. removeContact:  “Nombre Apellido” del contacto y lo elimine 
    '''



def addContacts3(nombre, apellido, telefono,diccionarioMaestro):
    """Agrega un nuevo contacto al diccionario con el input del nombre, apellido, telefono"""
    key = produceContactID2(nombre,apellido)
    nestedDictionary = {'nombre':nombre,'apellido':apellido,'telefono':telefono}
    diccionarioMaestro[key] = nestedDictionary
    return diccionarioMaestro
    

def listContacts4(diccionarioMaestro):
    """Imprime el diccionario de una forma ordena, este formato no toma en cuenta el uso de un nested dictionary, no usa el contactID"""
    print('DiccionarioMaestro: → ',diccionarioMaestro)
    print("Contact List → \n")
    
    for key in diccionarioMaestro:
        if key != 'favorites':
            print("Nombre Del Contacto: {} {}, Teléfono: {}".format(diccionarioMaestro[key]['nombre'], diccionarioMaestro[key]['apellido'], diccionarioMaestro[key]['telefono']))
        else:
            pass

def listFavoritesContacts4punto5(favorites):
    if bool(favorites) != False:
        for key in favorites:
            print("Nombre Del Contacto en favoritos: {} {}, Teléfono: {}".format(favorites[key]['nombre'], favorites[key]['apellido'], favorites[key]['telefono']))
    else:
        print('Fvorites is empty.')


def removeContact5(nombre,apellido,diccionarioMaestro):
    """Remueve del diccionario el contacto ingresado"""
    key = produceContactID2(nombre,apellido)
    try:
        del diccionarioMaestro[key]
        # valid2 = 'yes'
    except:
        print("El contacto ingresado está mal escrito o no existe en la lista de contactos")

    return diccionarioMaestro
    
#################################################################################################################################################################################
#FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #
#################################################################################################################################################################################
#FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #FASE 2 #
#################################################################################################################################################################################
def documentacionDeLaFase2():
    """ Fase 2: 
    1. Leer/cargar (automaticamente) los contactos de un archivo llamado InitialContacts.txt, si y solo si el archivo existe en el mismo directorio que su programa.py
    2. Agregarlos a la “lista” que anteriormente estaba vacia , es decir ahora su lista ya va a estar pre-inicializada
    3. Obviamente estos contactos deben ser ordenados dentro de la “lista” de contactos

    Recuerde que los contactos se clasifican y se ordenan por apellido, si el apellido no esta
    presente el nombre dictara en que “Letra” alfabetica se pondra el contacto. Estos contactos
    estaran en el archivo de una manera desordenada."""



def readFile6(filename):
    """Lee un archivo externo, le quita las lineas en blanco, y lo agrega los contactos al diccionario en base al nombre, appelido, telefono"""
    with open(filename) as archivo:
        print("el archivo a leer es {}".format(filename))
        reader = archivo.readlines()
        stringedList = "".join(reader)
        #
        listToIterate = stringedList.splitlines()
        # print(listToIterate)
        combinedList = []
        iteration = 0
        for n in listToIterate:
            if listToIterate[iteration] != '':
                combinedList.append(listToIterate[iteration])
            iteration = iteration + 1

        finalList = []
        for line in combinedList:
            separated = line.split(",")
            finalList.append(separated)
        return finalList

# print(readFile(filename))

# def addContactsFromTxt7(filename,diccionarioMaestro):
#     lines=readFile6(filename)
#     # lines.strip("-")
#     for line in lines:
#         words = line.split(",")
#         newContactID = words[0]+words[1]

#         diccionarioMaestro.update( {newContactID : {"nombre": words[0], "apellido": words[1], "telefono": words[2]}})
#     return diccionarioMaestro

#################################################################################################################################################################################
#FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #
#################################################################################################################################################################################
#FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #FASE 3 #
#################################################################################################################################################################################
#def documentacionDeLaFase3():
    ''' 
    Fase 3:
    ContactID: cada contacto debe estar guardado mediante un contactID (puede ser un numer
    correlativo o algo mas elaborado)

    1. callContact({contactID}): que recibiendo un ID de contacto pueda “llamar” a un contacto, 
    para llamar a un contacto basta con desplegar por 60 segundos o hasta que el usuario presione la letra “C”

        “Llamando a: Antonio Melgar
        Telefono: 777-777-777 ”

    2. msgContacts ({contactIDs}[]) : que reciba una lista de 1 o mas contact IDs (Nombre y Apellido) y que reciba un texto que 
    represente el mensaje que se desea enviar “To: Juan Guzman (55-555-555),Pablo Alvarez (33-333-333),Luis Fernandez (22-222-222)
    Msg: Hola solo queria saber si vendran al laboratorio" 

    3. addToFavorite({contactID}): este metodo debe de agregar el contacto que reciba a una nueva lista de favoritos. 
    (esta es una nueva lista con nuevos contactID)

    4. getFavoriteList() : metodo que despliega esta lista de contactos de una manera “pretty”

    5. removeFromFavorite({contactIDinFavorite}): que recibiendo el apellido y el nombre del contacto elimine ese contacto de la lista.
    Todos estos funciones deberan pertenecer a la fase 3 pero debera mostrar un sub-menu que

    muestre todas estas opciones, y la manera de interactuar con los contactos es de manera list &
    scroll. Es decir los contactos deben mostrarse :
    1. Haciendo un scroll y cada contacto debera tener un correlativo (1. Juan Guzman,555555 )
    2. Solo mostrando la lista con los contactos y un correlativo y elegir el numero de correlativ
    '''



def callContact8(contactID,diccionarioMaestro):
    """Llama al contacto ingresado"""
    try:
        if  contactID in diccionarioMaestro:
            contactID = diccionarioMaestro[contactID]['nombre'] + ' ' + diccionarioMaestro[contactID]['apellido'] #se ingresa el ID para que llame a la persona que desea 
            Esthetics1()
            print("Llamando a: {}".format(contactID)) #imprime el nombre de la persona con el texto llamando a
            #print("Teléfono: {}".format)
            for restantes in range(60, 0, -1): #contador de en retroseso de 60 segundos 
                    sys.stdout.write("\r")
                    #sys.stdout.write("Llamando a: {}".format(nombre))
                    sys.stdout.write("{:2d} Segundos restantes".format(restantes)) #se utilizo sys,stdout porque se pueden combinar int y string
                    sys.stdout.flush()
                    time.sleep(1)
            sys.stdout.write("\rSe realizo la llamada con éxito!!            \n")
        else:
            print('\nEl contacto está mal escrito o no existe.')
    except KeyboardInterrupt:
                print("\nla llamada se cancelo")
                Esthetics1()


def msgContacts9(mensaje,contactsToSendTo,diccionarioMaestro ):
        """Manda un mensaje a los contactos si estan en el diccionario ingresado"""
        listSplit = contactsToSendTo.split(',')
        verifiedSplit = []
        invalidSplit = []
        iteration1 = 0
        for items in listSplit:
            if listSplit[iteration1] in diccionarioMaestro:
                verifiedSplit.append(listSplit[iteration1])
            else:
                invalidSplit.append(listSplit[iteration1])
            iteration1 = iteration1 + 1


        
        if len(invalidSplit) != 0:
            print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
            print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

        elif len(invalidSplit) == 0:
            print('To: {}'.format(', '.join(verifiedSplit)),' → ', mensaje)

        
def addFavoriteList10(favoriteContactAddition,favorites,diccionarioMaestro):
    """Agrega contactos a favoritos"""
    listSplit = favoriteContactAddition.split(',')
    verifiedSplit = []
    invalidSplit = []
    iteration1 = 0
    for items in listSplit:
        if listSplit[iteration1] in diccionarioMaestro:
            verifiedSplit.append(listSplit[iteration1])
        else:
            invalidSplit.append(listSplit[iteration1])
        
        iteration1 = iteration1 + 1
        
    if len(invalidSplit) != 0:
        print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
        print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

    elif len(invalidSplit) == 0:
        iteration2 = 0
        for n in verifiedSplit:
            favorites[verifiedSplit[iteration2]] = diccionarioMaestro[verifiedSplit[iteration2]]
            iteration2 = iteration2 + 1
        diccionarioMaestro['favorites'] = favorites
        print('Se a agregado → {} ← a favoritos.'.format(verifiedSplit))


def removeFromFavorites11(favoriteContactdelete,favorites,diccionarioMaestro):
    """Remueve contactos de favoritos"""
    value = diccionarioMaestro.get('favorites')
    if value != 'None':
        listSplit = favoriteContactdelete.split(',')
        verifiedSplit = []
        invalidSplit = []
        iteration1 = 0
        for items in listSplit:
            if listSplit[iteration1] in diccionarioMaestro:
                verifiedSplit.append(listSplit[iteration1])
            else:
                invalidSplit.append(listSplit[iteration1])
            
            iteration1 = iteration1 + 1

        
        
        if len(invalidSplit) != 0:
            print('Contacto(s) → {} ← parece(n) no existir en la lista de contactos'.format(', '.join(invalidSplit)))
            print("Porfavor asegúrese de haber escrito el contacto correctamente y que el contacto si exista en el directorio.")

        elif len(invalidSplit) == 0:
            iteration2 = 0
            
            for n in verifiedSplit:
                try:
                    del diccionarioMaestro['favorites'][verifiedSplit[iteration2]]
                    del favorites[verifiedSplit[iteration2]]
                    iteration2 = iteration2 + 1
                except:
                    print('Tu contacto no pudo ser eliminado por que no se encuentra en "favoritos".')
            print(', '.join(verifiedSplit))
        else:
            print('No tienes lista de favoritos.')

#################################################################################################################################################################################
#FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #
#################################################################################################################################################################################
#FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #FASE 4 #
#################################################################################################################################################################################
#def documentacionDeLaFase4():
    '''
    Fase 4:
    loadFromFile(externalFile), que reciba el nombre de un
    archivo del cual se leerán los contactos, su método debe ser failsafe, es decir si el archivo no
    existe no ejecutar nada y devolver un “error”
    El programa (CLI) debe pedir el full path del archivo “~/Downloads/contacts.txt”
    .txt, .csv, .lists, .contacts
    '''



def loadFromFile12(filename,diccionarioMaestro):
    """Agrega contactos de un archivo externo al diccionario"""
    words = readFile6(filename)
    iteration = 0
    for line in words:
        # for words in line:
        key = produceContactID2(words[iteration][0], words[iteration][1])
        diccionarioMaestro.update( {key : {"nombre": words[iteration][0], "apellido": words[iteration][1], "telefono": words[iteration][2]}})
        iteration = iteration + 1
    return diccionarioMaestro
    
# print(loadFromFile(filename,diccionarioMaestro))


#################################################################################################################################################################################
#FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #
#################################################################################################################################################################################
#FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #FASE 6 #
#################################################################################################################################################################################
#def documentacionDeLaFase6():
    '''
    Fase 6
    Save to Web via HTTP methods, en lo visto en clase aprendimos GET y POST.
    El dia del proyecto se le proveera con una URL (por ejemplo: http://marcosapi.com/) a la cual
    usted debera: crear un contact list y obtener un contact list
    POST:
    - http://demo7862839.mockable.io/contacts?gid=100 usando el metodo POST debera
    exportar y crear su “current” contact list mediante un payload (data) que contenga su
    contact list en forma dictionary (JSON, ver ejemplo abajo)
    GET:
    - http://demo7862839.mockable.io/contacts?gid=100
    - gid=100 es el request parameter (query param) y es igual a 100, por que ese es mi fake
    gid.
    En ambos casos puede usar gid como query parameter o proveer un custom request header
    gid: HTTP
    _ID
    '''



def post13(gid,urlPost,diccionarioMaestro):
    """Manda contactos del diccionario a un URL"""
    #urlPost="https://reqres.in/api/users"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    urlPost=input("Ingrese la url con la desea utilizar el método POST:\n  ")#Metodo 2 Si desea que la url se ingrese
    gid = 0
    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    #payload={'FirstName': 'Michael', 'LastName': 'Kirk', 'phone': '123123'}
    payload=diccionarioMaestro
    #la información (data) para subir

    postResponse=requests.post(urlPost, params = params, json=payload)
    dataPost=postResponse.json()
    print(postResponse)
    #imprime el status code
    print(dataPost)
    #imprime la data 

def get14(gid,urlGet,diccionarioMaestro):
    """Recibe contactos de un URL y los ingresa al diccionario"""
    #urlGet="http://demo7862839.mockable.io/contacts?gid=100"#Metodo 1 Si desea que la url este ingresada pero solo se desea cambiar una vez

    
    params = {'gid':gid}
    #Se ingresa el gid que es el valor

    getResponse=requests.get(urlGet, params = params)
    dataGet=getResponse.json()
    print(getResponse)
    #imprime el status code
    print(dataGet)
    #imprime la data
    diccionarioMaestro = dataGet
    return diccionarioMaestro

###########################################################################################################################################################################################################################
#EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS 
###########################################################################################################################################################################################################################
#EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS #EXPORTACION DE DATOS
###########################################################################################################################################################################################################################

def impresionDirectaALaTerminal15(diccionarioMaestro,favorites):
    Esthetics1()
    listContacts4(diccionarioMaestro)
    listFavoritesContacts4punto5(favorites)
    Esthetics1()

def exportacionDeLaDataAUnArchivoNuevo16(diccionarioMaestro,favorites,newFileName):
    #esto va en el main
    # newFileName = input('Ingrese el nombre del archivo aquí: → ') + input('Ingrese la extensión aquí: ("txt","csv") → ')
    #esto va en el main
    with open(newFileName, "w+") as newFile:
        newFile.write('En Contactos: \n')
        
        for key in diccionarioMaestro:
            if key != 'favorites':
                line = '=> ' + diccionarioMaestro[key]['nombre'] + ',' + diccionarioMaestro[key]['apellido'] + ',' + diccionarioMaestro[key]['telefono'] + '\n'
                newFile.write(line)
        
        newFile.write('\n')
        newFile.write('EnFavoritos: \n')
        for key1 in favorites:
            
            line1 = '=> ' + favorites[key1]['nombre'] + ',' + favorites[key1]['apellido'] + '\n'
            newFile.write(line1)
            


def exportacionAUnaURL17():
    pass

