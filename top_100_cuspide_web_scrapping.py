#VERSION A MANO

import requests

def buscar_titulo(cantidad=int):
    
    url='https://www.cuspide.com/top100.aspx'
    html = requests.get(url).text #Busco en todo el HTML de la pagina
    for x in range(cantidad):
        #Tenemos que buscar nuestra palabra clave, use el metodo string FIND para que me de la posicion
        if x < 10:
            pos = html.find('ctl0' + str(x) + '_img_tapa')
        else:
            pos=html.find('ctl' + str(x) + '_img_tapa') #Aca empieza a contar del 10
            
            #Busco para adelante hasta llegar el nombre del titulo, A MANO, voy probando 50 para la derecha
            
        segmento=html[pos+58:pos+150]
        
        #Tengo que encontrar la comilla de este segmento
        pos_final=segmento.find('"')
        titulo_libro = segmento[:pos_final]
        if titulo_libro[1] == '.': titulo_libro=titulo_libro[3:] #ELIMINO LOS 2 1. Harry Potter
        if titulo_libro == '.me/ns/fb#': #Elimino los titulos que estan demas
            return None
        print(x+1,titulo_libro)
    

cantidad=int(input("Cuantos titulos del top 100 quiere averiguar?: "))        
buscar_titulo(cantidad)
 