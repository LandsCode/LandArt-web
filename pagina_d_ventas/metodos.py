import json
import os

def mostrar_detalles_del_sombrero(catalogo , id_sombrero) :
    #buscamos el sombrero usando le parametro catalogo, qiue recibe la función
    sombrero= catalogo.get(id_sombrero)

    if sombrero:
       print("Consulta de inventario")
  #el sistema busca el id dentro del catalogo y lo muestra en la pantalla
       print(f"Producto:{sombrero ['nombre']}")
       print(f"Precio:{sombrero ['precio']} MXN")
       print(f"Técnica:{sombrero ['tecnica']}")
       print(f"Material:{sombrero ['material']}")
    else :
       print(f"Producto elegido no existe" )
    
       
    
#función cambiar datos del catálogo
def cambiar_detalles_del_catalogo(catalogo, id_sombrero, dato, dato_nuevo):
   detalles= catalogo.get(id_sombrero)
   if detalles:
      catalogo [id_sombrero][dato] = dato_nuevo
      mostrar_detalles_del_sombrero(catalogo, id_sombrero)
   else:
      print(f"No se pudo modificar: El producto con ID '{id_sombrero}' no existe.")   
   
   
         
   
#funcion lee directamnente desde el archivo json sin pedir parametros
def obtener_lista_de_productos():
   lista_json = 'productos.json'
#si el archivo no existepor alguna razón devolvemos una lista vacia   
   if not os.path.exists(lista_json):
       return []
    
    #leemos el archivo json real
   with open(lista_json, "r", encoding="utf_8") as archivo :
      catalogo =json.load(archivo)  
    
    
 #transforma tu dicionario en una lista limpia para el html
   lista_para_web =[]
   for id_sombrero, datos in catalogo.items():
      #copiamos los datos del sombrero
      sombrero_web = datos.copy()
      #le guardamos su id por si se necesita despues
      sombrero_web['id'] = id_sombrero
      lista_para_web.append(sombrero_web)
   return lista_para_web   
    
