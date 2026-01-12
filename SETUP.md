# Configuración del Entorno Conda

Este proyecto utiliza un entorno conda para gestionar las dependencias de Python.

## Activación del Entorno

Para activar el entorno conda en tu terminal:

```bash
conda activate pydantic_course
```

## Configuración del Editor

Si estás usando Cursor o VS Code, el editor debería detectar automáticamente el intérprete de Python del entorno conda gracias a los archivos de configuración:

- `.vscode/settings.json` - Configuración del intérprete de Python
- `pyrightconfig.json` - Configuración del type checker Pyright

### Selección Manual del Intérprete

Si el editor no detecta automáticamente el entorno:

1. Presiona `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac)
2. Escribe "Python: Select Interpreter"
3. Selecciona: `/home/dams/miniconda3/envs/pydantic_course/bin/python`

## Verificación

Para verificar que todo está configurado correctamente:

```bash
conda activate pydantic_course
python -c "import pydantic; print(f'Pydantic version: {pydantic.__version__}')"
```

## Instalación de Dependencias

Si necesitas instalar las dependencias en el entorno:

```bash
conda activate pydantic_course
pip install -r requirements.txt
```
