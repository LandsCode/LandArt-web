# 🎨 LandArt - Catálogo de Piezas Artesanales (En Construcción)

¡Bienvenido/a al repositorio de **LandArt**! Este es el desarrollo de una plataforma web y tienda en línea dedicada a la exposición y venta de piezas artesanales únicas hechas a mano, que incluye sombreros de autor, joyería en filigrana y cuadros sobre lienzo.

El proyecto se encuentra actualmente en **fase activa de desarrollo**.

---

## 🛠️ Estado Actual del Proyecto
La arquitectura base del sistema ya interactúa de manera dinámica entre el backend y las plantillas del cliente.

### **¿Qué funciones ya están listas?**
- [x] **Estructura Backend:** Servidor funcional configurado en **Flask (Python)**.
- [x] **Panel de Administración:** Formulario dinámico para la actualización de inventario (IDs, precios, técnicas y materiales).
- [x] **Catálogo Público:** Renderizado dinámico de tarjetas de producto mediante bucles de Jinja2 en el Frontend.
- [x] **Navegación:** Menú desplegable interactivo por categorías (Sombreros, Aretes, Cuadros).

### **Próximos Pasos (To-Do List) 🚧**
- [ ] **Procesamiento de Formularios:** Guardar de forma persistente los cambios del Administrador en una Base de Datos o archivo JSON.
- [ ] **Motor de Búsqueda:** Activar la ruta `/buscar` para filtrar piezas por nombre o técnica artesanal.
- [ ] **Interactividad del Carrito:** Lógica en JavaScript para añadir artículos y calcular el total de la compra.
- [ ] **Ajustes de Estilo (CSS):** Pulir los contrastes visuales y asegurar el diseño responsivo para dispositivos móviles.

---

## 🚀 Tecnologías Utilizadas
* **Backend:** Python 3 + Flask (Microframework)
* **Frontend:** HTML5, CSS3 (Estilos personalizados), Jinja2 (Motor de plantillas)
* **Vistas Configuradas:**
  * Vista del Cliente: Catálogo público e interfaz de usuario.
  * Vista del Administrador: Panel de control de inventario y referencias de ID.

---

## 📦 Instalación y Ejecución en Entorno Local

Para clonar este catálogo y ejecutar el servidor de Flask en tu computadora, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   ```
2. **Navegar a la carpeta del proyecto:**
   ```bash
   cd tu-repositorio
   ```
3. **Crear y activar un entorno virtual (Recomendado):**
   * En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * En Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
4. **Instalar las dependencias (Flask):**
   ```bash
   pip install flask
   ```
5. **Iniciar el servidor de desarrollo:**
   ```bash
   python app.py
   ```
   *(Nota: Asegúrate de reemplazar `app.py` por el nombre real de tu archivo principal de Python si es diferente).*

6. **Abrir en el navegador:**
   Ingresa a `http://127.0.0` para ver el catálogo.

---

## 📬 Contacto y Colaboración
Si deseas conocer más sobre el desarrollo técnico de esta galería artesanal:
* **Desarrollador/a:** [Landy Camacho]
* **GitHub:** [@LandsCode](https://github.com)
