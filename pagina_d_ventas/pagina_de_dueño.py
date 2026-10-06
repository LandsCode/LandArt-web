import metodos
import catalogo_sombreros

print("¿Qué sombrero quieres modificar?")         
       
       
id_del_producto = input("Escribe el sombrero que deseas buscar ") 


metodos.mostrar_detalles_del_sombrero(catalogo_sombreros.catalogo_de_sombreros , id_del_producto)
dato= input("Que quieres modificar: ")
if(dato == "tecnica"):
    msj="la nueva"
else :
    msj= "el nuevo"    
    
nuevo_dato= input(f"Introduce {msj} {dato} ")
metodos.cambiar_detalles_del_catalogo(catalogo_sombreros.catalogo_de_sombreros, id_del_producto, dato , nuevo_dato)
