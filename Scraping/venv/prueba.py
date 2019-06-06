import requests
import csv
from bs4 import BeautifulSoup as bs

##URL a la que queremos acceder
url = requests.get("http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx")
##Parseamos la url gracias a la libreria BeautifulSoup (url.content, es el contenido de nuestra url)
soup = bs(url.content, 'html.parser')

##Creamos un csv completamente vacio gracias a la libreria csv
##filename es el nombre del nuevo csv
filename = "resultado.csv"
csv_writer = csv.writer(open(filename, 'w'))

## EL CSV se rellena por filas, lo que quiere decir, que crearemos un nuevo array, que sera la fila que insertaaremos
##El primer array que tenemos que meter es el de los indices que nos pidan (Las cosas que tenemos que sacar de la URl
##En este caso, Nombre del indice, anterior...
data = []
data.append("Nombre del indice")
data.append("Anterior")
data.append("Ultimo")
data.append("%Diff")

## el if funciona si el array data no esta vacio.

if data:
    ##Printear no es necesario pero es una buena manera de ver por
    # consola si nuestro programa esta funcionando correctamente

    print("Inserting headers : {}".format(','.join(data)))
    #LO MAS IMPORTANTE, accedemos a nuestro csv_writer, y con la función writerow,
    # escribimos la fila que tengamos guardada en el array
    #Es muy importante tener en cuenta que TODO lo que haya en el array va a ser una nueva celda del csv
    csv_writer.writerow(data)
    #Vaciamos el array para no tener que crear uno nuevo (y asi no ocupar memoria innecesaria.
    data=[]

#SE VIENE LO CHINGON

#El objetivo de este bucle es acceder a los datos que queramos acceder, pero DE 1 EN 1
#Por lo que en el bucle dejaremos el for article PERO dentro del findAll,
# tendremos que acceder a los objetos que queramos obtener al completo, en nuestro caso los 'tr'
for article in soup.findAll('tr', align="right"):

    #MUY IMPORTANTE
    #MUY IMPORTANTE
    #MUY IMPORTANTE

    #ya estamos dentro del objeto, olvidad todo lo que no sea nuestro objeto
    #nuestro objeto se llama article porque asi lo hemos decidido en el for

    #Este ejemplo es muy facil, ya que todos los ficheros a los que queremos acceder tienen la misma etiqueta 'td'
    # Por lo que crearemos un array, al que llamaremos aux, donde se guardaran todos los td
    #Para un ejemplo más complejo mirar mi github
    aux=article.findAll('td')
    #Nombre

    #Acordas que todo se guarda en el mismo array, por lo que cogemos la posicion de lo que queramos meter
    #EN ORDEN, en la posicion 0 estara el objeto que antes est, en este caso el Nombre del indice
    data.append(aux[0].string.encode('utf-8'))
    data.append(aux[1].string.encode('utf-8'))
    data.append(aux[2].string.encode('utf-8'))
    data.append(aux[3].string.encode('utf-8'))

    #Es exactamente igual que el if anterior
    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        data=[]
    #volvemos a repetir al proceso para el siguiente articulo