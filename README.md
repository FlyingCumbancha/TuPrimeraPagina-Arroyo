
# Proyecto Pagina Web con Python

Proyecto web desarrollado con **Django** utilizando el patrón **MVT (Model–View–Template)**.  
Simula un **blog** con herencia de plantillas, formularios para alta de datos y búsqueda en la base de datos.

---

## ⚙️ Tecnologías utilizadas
- **Python 3.10+**
- **Django 5.x**
- **SQLite** 
- **Bootstrap 5 (CDN)** 

---

## 📦 Instalación y ejecución

### 1️⃣ Crear y activar el entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Crear las migraciones y aplicarlas
> Este paso genera las tablas necesarias en la base de datos.
```bash
python manage.py makemigrations blog
python manage.py migrate
```

### 4️⃣ Cargar datos de ejemplo
> El proyecto incluye un dataset en `blog/fixtures/seed.json` con autores, categorías y posts de prueba.
```bash
python manage.py loaddata seed
```

### 5️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```
El proyecto se visualiza en localhost:8000

---

## 🧩 Funcionalidades

### 🧱 Modelos (`blog/models.py`)
1. **Autor**  
   - `nombre`, `email`, `bio`  
   - Representa al creador de los posts.

2. **Categoria**  
   - `nombre`, `slug` (autogenerado con `save()`)  
   - Agrupa los posts por temática.

3. **Post**  
   - `titulo`, `contenido`, `fecha_pub`, `publicado`,  
     `autor` (FK a Autor) y `categoria` (FK a Categoria).  
   - Ordenado por fecha descendente.

---

### 🧾 Formularios (`blog/forms.py`)
- `AutorForm`, `CategoriaForm`, `PostForm` → Formularios para alta de datos.
- `BusquedaForm` → Permite buscar posts por texto y/o filtrar por categoría.

---

### 🌐 Vistas y URLs (`blog/views.py`, `blog/urls.py`)
- `/` → **Inicio:** lista de posts publicados, paginados (5 por página), con búsqueda.
- `/post/<id>/` → **Detalle** de un post.
- `/crear/autor/` → Formulario para crear un nuevo autor.
- `/crear/categoria/` → Formulario para crear una nueva categoría.
- `/crear/post/` → Formulario para crear un nuevo post.

---

### 🧱 Plantillas (`templates/`)
- **Herencia:** todas las páginas extienden de `base.html`.
- `base.html` → plantilla principal con menú y estilos Bootstrap.
- `blog/post_list.html` → listado y búsqueda de posts.  
- `blog/post_detail.html` → detalle del post seleccionado.  
- `blog/autor_form.html`, `blog/categoria_form.html`, `blog/post_form.html` → formularios de alta.

---

### 🔍 Búsqueda
La búsqueda se realiza desde la barra superior:
- Campo de texto libre (busca por título o contenido).
- Filtro opcional por categoría.
- Combinable con la paginación.

---

### 🧾 Dataset de ejemplo (`blog/fixtures/seed.json`)
Contiene:
- 2 autores (`Ana Banana`, `Bruno Díaz`).
- 2 categorías (`Tecnología`, `Ciencia`).
- 6 posts precargados con contenido básico.

Para cargarlo:
```bash
python manage.py loaddata seed
```

---

### ⚙️ Panel de administración (opcional)
Podés crear un superusuario y administrar todo desde `/admin`:
```bash
python manage.py createsuperuser
```

## 🧭 Orden sugerido para probar
1. Ejecutar el proyecto y visitar `/`.
2. Crear nuevos autores y categorías.
3. Crear posts y visualizarlos en el listado.
4. Usar la barra superior para buscar por texto o categoría.
5. Navegar entre páginas con la paginación.
6. (Opcional) Ingresar a `/admin` para ver la administración de modelos.
