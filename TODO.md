# Ejercicios de Pydantic BaseModel API

Este documento contiene ejercicios prácticos basados en diferentes apartados de la documentación oficial de Pydantic BaseModel API: https://docs.pydantic.dev/latest/api/base_model/

Cada ejercicio incluye una referencia al apartado específico de la documentación para que puedas consultar cómo resolverlo.

---

## Ejercicio 1: Creación básica de un modelo BaseModel

**Descripción:** Crea un modelo `Usuario` que herede de `BaseModel` con los campos:
- `id`: entero
- `nombre`: cadena de texto
- `email`: cadena de texto opcional

Instancia el modelo con datos válidos y muestra sus atributos.

**Referencia:** [BaseModel - Creación de modelos](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel)

---

## Ejercicio 2: Validación con `model_validate()`

**Descripción:** Crea un modelo `Producto` con los campos `nombre` (str) y `precio` (float). 
Usa el método `model_validate()` para validar datos desde un diccionario. Prueba con datos válidos e inválidos y maneja las excepciones.

**Referencia:** [BaseModel.model_validate()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate)

---

## Ejercicio 3: Validación desde JSON con `model_validate_json()`

**Descripción:** Define un modelo `Evento` con los campos `titulo` (str) y `fecha` (datetime).
Usa `model_validate_json()` para crear una instancia del modelo desde una cadena JSON. 
Incluye el manejo de errores para JSON mal formado.

**Referencia:** [BaseModel.model_validate_json()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_json)

---

## Ejercicio 4: Serialización con `model_dump()`

**Descripción:** Crea un modelo `Libro` con los campos `titulo`, `autor` y `año_publicacion`.
Instancia el modelo y usa `model_dump()` para convertirlo a diccionario. Prueba los parámetros:
- `mode='json'` vs `mode='python'`
- `exclude` para excluir campos
- `include` para incluir solo ciertos campos

**Referencia:** [BaseModel.model_dump()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump)

---

## Ejercicio 5: Serialización a JSON con `model_dump_json()`

**Descripción:** Usa el modelo `Libro` del ejercicio anterior y serialízalo a JSON usando `model_dump_json()`.
Compara el resultado con usar `json.dumps(model_dump())`. Prueba con diferentes valores de `indent` para formatear el JSON.

**Referencia:** [BaseModel.model_dump_json()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_dump_json)

---

## Ejercicio 6: Generación de JSON Schema con `model_json_schema()`

**Descripción:** Crea un modelo `Configuracion` con varios campos de diferentes tipos (str, int, bool, Optional).
Genera el JSON Schema usando `model_json_schema()` y analiza su estructura. 
Experimenta con el parámetro `by_alias` para ver cómo afecta al schema.

**Referencia:** [BaseModel.model_json_schema()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_json_schema)

---

## Ejercicio 7: Acceso a campos con `model_fields`

**Descripción:** Crea un modelo `Empleado` con varios campos usando `Field()` con diferentes configuraciones (descripción, alias, validaciones).
Accede a `model_fields` y itera sobre los campos para mostrar:
- Nombre del campo
- Tipo del campo
- Si es opcional
- Si tiene alias
- Descripción si existe

**Referencia:** [BaseModel.model_fields](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields)

---

## Ejercicio 8: Configuración del modelo con `model_config`

**Descripción:** Crea un modelo `Cliente` y configura `model_config` para:
- Permitir campos extra (`extra='allow'`)
- Usar alias al serializar (`populate_by_name=True`)
- Validación estricta (`strict=True`)

Prueba cada configuración y observa cómo afecta al comportamiento del modelo.

**Referencia:** [BaseModel.model_config](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_config)

---

## Ejercicio 9: Construcción sin validación con `model_construct()`

**Descripción:** Crea un modelo `Pedido` con validaciones en los campos (por ejemplo, precio > 0).
Usa `model_construct()` para crear una instancia sin validación y compara el resultado con la creación normal.
Observa qué sucede cuando pasas datos inválidos a `model_construct()`.

**Referencia:** [BaseModel.model_construct()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct)

---

## Ejercicio 10: Copia de modelos con `model_copy()`

**Descripción:** Crea una instancia de un modelo `Usuario` con varios campos.
Usa `model_copy()` para crear una copia y modifica algunos campos usando el parámetro `update`.
Compara la instancia original con la copia modificada.

**Referencia:** [BaseModel.model_copy()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_copy)

---

## Ejercicio 11: Reconstrucción de modelos con `model_rebuild()`

**Descripción:** Crea un modelo `A` que referencia a un modelo `B` definido después (forward reference).
Usa `model_rebuild()` para reconstruir el modelo después de que `B` esté definido.
Observa cómo esto resuelve las referencias forward.

**Referencia:** [BaseModel.model_rebuild()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild)

---

## Ejercicio 12: Validación de strings con `model_validate_strings()`

**Descripción:** Crea un modelo `Producto` con campos de diferentes tipos (int, float, bool, datetime).
Usa `model_validate_strings()` para validar datos donde todos los valores vienen como strings.
Compara el comportamiento con `model_validate()` normal.

**Referencia:** [BaseModel.model_validate_strings()](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_strings)

---

## Ejercicio 13: Uso de `model_parametrized_name`

**Descripción:** Si trabajas con modelos genéricos o parametrizados, investiga cómo funciona `model_parametrized_name`.
Crea un modelo genérico simple y observa cómo se comporta este atributo.

**Referencia:** [BaseModel.model_parametrized_name](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_parametrized_name)

---

## Ejercicio 14: Integración completa - API REST simulada

**Descripción:** Crea un sistema completo que simule una API REST:
1. Define varios modelos relacionados (Usuario, Post, Comentario)
2. Usa `model_validate_json()` para recibir datos de una "request"
3. Valida y procesa los datos
4. Usa `model_dump_json()` para devolver respuestas
5. Genera el JSON Schema de todos los modelos para documentación

**Referencia:** Combinación de múltiples métodos de BaseModel API

---

## Ejercicio 15: Manejo de errores y validación avanzada

**Descripción:** Crea un modelo con validaciones complejas y usa `model_validate()` con diferentes datos.
Captura y analiza las excepciones `ValidationError` de Pydantic:
- Muestra todos los errores
- Accede a los errores por campo
- Formatea los errores de manera legible

**Referencia:** [Validación y manejo de errores](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate) y [ValidationError](https://docs.pydantic.dev/latest/api/errors/#pydantic.ValidationError)

---

## Notas adicionales

- Todos los ejercicios deben seguir PEP 8 para el código Python
- Usa type hints en todos los modelos
- Documenta tus funciones y clases siguiendo PEP 8
- Considera crear tests para cada ejercicio usando Gherkin para la documentación de tests
- Consulta la documentación oficial para detalles específicos de cada método
