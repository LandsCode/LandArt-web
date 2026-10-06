from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
# Importamos tus funciones de métodos
from pagina_d_ventas.metodos import obtener_lista_de_productos

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_para_alertas' 

# RUTA DEL JSON: Nos aseguramos de decirle a Flask dónde está tu archivo de sombreros
lista_json = 'productos.json'

def cargar_catalogo_completo():
    #"""Función auxiliar para leer el diccionario completo desde el JSON"""
    if not os.path.exists(lista_json):
        return {}
    with open(lista_json, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def guardar_catalogo_completo(catalogo):
   # """Función auxiliar para guardar el diccionario completo en el JSON"""
    with open(lista_json, 'w', encoding='utf-8') as archivo:
        json.dump(catalogo, archivo, indent=4, ensure_ascii=False)


# 1. Ruta del comprador: muestra todo el catálogo con detalles
@app.route('/')
def catalogo():
    # Tu función obtener_lista_de_productos ahora lee internamente el JSON (según cambiamos en metodos.py)
    productos_listados = obtener_lista_de_productos()
    return render_template('index.html', productos=productos_listados)


# 2. Ruta del dueño: panel de administración para modificar datos
@app.route('/admin', methods=['GET', 'POST'])
def administrador():
    # Cargamos el catálogo actual desde el archivo JSON
    catalogo_actual = cargar_catalogo_completo()

    if request.method == 'POST':
        id_prod = request.form.get('id_producto')
        campo = request.form.get('campo_a_modificar')
        nuevo_valor = request.form.get('nuevo_valor')
        
        # Validamos que el producto exista en el catálogo del JSON
        if id_prod in catalogo_actual:
            if campo == "precio":
                try:
                    catalogo_actual[id_prod][campo] = int(nuevo_valor)
                    # Guardamos el cambio de precio de manera permanente en el JSON
                    guardar_catalogo_completo(catalogo_actual)
                    flash("¡Producto modificado con éxito!")
                except ValueError:
                    flash("Error: El precio ingresado no es un número válido.")
            else:
                catalogo_actual[id_prod][campo] = nuevo_valor
                # Guardamos cualquier otro cambio de texto permanentemente en el JSON
                guardar_catalogo_completo(catalogo_actual)
                flash("¡Producto modificado con éxito!")
        else:
            flash("Error: El ID del sombrero ingresado no existe en el catálogo.")        
                
        return redirect(url_for('administrador'))          
    
    # Si es una consulta normal GET, listamos los productos leyendo el JSON
    productos_listados = obtener_lista_de_productos()            
    return render_template('admin.html', productos=productos_listados)
  
if __name__ == '__main__':
    app.run(debug=True)