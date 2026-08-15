# Prueba Técnica – Backend Python / Django (Junior / Mid)

**Duración sugerida:** 2 a 3 horas
**Herramientas permitidas:** Python, Django, Django REST Framework (opcional), PostgreSQL o SQLite, documentación oficial.

---

## Contexto

Vas a construir una pequeña API para gestionar una **biblioteca de libros**. El sistema debe permitir administrar libros, autores y préstamos.

---

## Parte 1 – Modelado (25%)

Crea los siguientes modelos en Django:

1. **Author**
   - `name` (string)
   - `nationality` (string, opcional)

2. **Book**
   - `title` (string) 
   - `author` (FK a `Author`)
   - `isbn` (string, único)
   - `published_date` (date)
   - `copies_available` (int, no puede ser negativo)

3. **Loan** (préstamo)
   - `book` (FK a `Book`)
   - `borrower_name` (string)
   - `loan_date` (date, auto al crear)
   - `return_date` (date, nullable)
   - `returned` (boolean, default `False`)

**Requisitos:**
- Define correctamente las relaciones y `related_name`.
- Agrega validaciones a nivel de modelo donde corresponda (por ejemplo, que `copies_available` no sea negativo).
- Incluye las migraciones correspondientes.

---

## Parte 2 – API REST (35%)

Implementa los siguientes endpoints (con DRF o vistas puras, a tu elección):

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/books/` | Lista todos los libros, con filtro opcional por `author` y `title` (query params) |
| POST | `/api/books/` | Crea un libro nuevo |
| GET | `/api/books/<id>/` | Detalle de un libro |
| PUT/PATCH | `/api/books/<id>/` | Actualiza un libro |
| DELETE | `/api/books/<id>/` | Elimina un libro |
| POST | `/api/books/<id>/loan/` | Crea un préstamo para ese libro (debe descontar `copies_available` en 1; si no hay copias disponibles, debe devolver error 400) |
| POST | `/api/loans/<id>/return/` | Marca el préstamo como devuelto, setea `return_date` y devuelve la copia (+1 a `copies_available`) |

**Requisitos:**
- Serializers con las validaciones necesarias.
- Manejo correcto de códigos de estado HTTP (200, 201, 400, 404, etc.).
- Respuestas en formato JSON consistente.

---

## Parte 3 – Lógica de negocio (20%)

Responde con código:

1. Escribe una función o método que devuelva **todos los libros que están actualmente prestados** (con al menos un `Loan` sin devolver).
2. Escribe una función o método que devuelva **el top 3 de autores con más libros prestados** en total (histórico).

Puedes implementarlas como:
- Métodos en el modelo/manager, **o**
- Endpoints adicionales (`/api/books/on-loan/`, `/api/authors/top/`)

---
## Parte 4 – Testing (15%)

Escribe al menos **3 tests** usando `Django TestCase` o `pytest-django` que cubran:

1. Que no se puede crear un préstamo si `copies_available == 0`.
2. Que al devolver un libro, `copies_available` aumenta correctamente.
3. Que el endpoint de listado de libros filtra correctamente por autor.

---

## Parte 5 – Preguntas teóricas cortas (5%)

Responde en pocas líneas (no hace falta código):

1. ¿Cuál es la diferencia entre `select_related` y `prefetch_related`? ¿Cuándo usarías cada uno?
2. ¿Qué problema resuelve una migración de Django y qué pasa si dos desarrolladores generan migraciones en paralelo sobre el mismo modelo?
3. ¿Qué diferencia hay entre `@api_view` y `APIView`/`ViewSet` en Django REST Framework?
4. Menciona una diferencia entre `ForeignKey` con `on_delete=CASCADE` y `on_delete=SET_NULL`.

---

## Entregables

- Código fuente (repo o carpeta comprimida).
- `requirements.txt` o `pyproject.toml`.
- Instrucciones para levantar el proyecto (`README.md` corto).
- (Opcional pero valorado) Colección de Postman/Insomnia o ejemplos de `curl` para probar los endpoints.

---

## Criterios de evaluación

- Buenas prácticas de Django (organización de apps, uso correcto de ORM).
- Claridad y consistencia del código.
- Manejo de errores y validaciones.
- Cobertura y calidad de los tests.
- Capacidad de justificar decisiones de diseño (te podrán hacer preguntas sobre tu solución).

¡Éxitos! 🚀