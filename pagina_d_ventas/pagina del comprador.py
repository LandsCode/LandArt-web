#importando módulo de metodos, y módulo de catálogo
import metodos
import catalogo_sombreros



print("¡Bienvenido a Tienda de sombreros!")  
print("¿Qué tipo de sombrero estás buscando?")     

seleccion_del_cliente = input("Escribe el sombrero que deseas buscar ") 
 
metodos.mostrar_detalles_del_sombrero(catalogo_sombreros.catalogo_de_sombreros , seleccion_del_cliente)  

