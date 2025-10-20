
# TuPrimeraPagina+Arroyo

Django (MVT) estilo blog con **herencia de plantillas**, **3 modelos** y formularios de **alta** y **búsqueda**.

## Pasos para probar (orden)
1) Crear venv e instalar
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
2) Migrar y cargar datos de ejemplo
```bash
python manage.py migrate
python manage.py loaddata seed
```
3) Ejecutar
```bash
python manage.py runserver
```
4) Navegar a `http://127.0.0.1:8000/` y probar:
- Crear Autor / Categoría / Post
- Buscar por texto y/o por categoría
- Listado con paginación y detalle de Post

Admin opcional:
```bash
python manage.py createsuperuser
# luego ir a /admin
```
