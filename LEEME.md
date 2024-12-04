# Gestor de Tareas


El Gestor de Tareas es una aplicación de escritorio desarrollada con Tkinter que permite a los usuarios organizar sus tareas de manera eficiente. Con una interfaz gráfica intuitiva, los usuarios pueden añadir, editar, eliminar, buscar y completar tareas. Además, incluye una funcionalidad para programar recordatorios.

## Características
- **Añadir tareas**: Incluye descripción, categoría y recordatorio opcional.
- **Editar tareas**: Modifica cualquier tarea existente.
- **Eliminar tareas**: Borra tareas innecesarias.
- **Marcar tareas como completadas**: Lleva un registro del estado de tus tareas.
- **Buscar tareas**: Encuentra rápidamente tareas por su descripción.
- **Guardado y carga automática**: Las tareas se almacenan en un archivo JSON para mantenerlas entre sesiones.
- **Recordatorios**: Recibe alertas programadas para no olvidar tus tareas importantes.

## Requisitos
Para ejecutar este proyecto, necesitas:
- Python 3.x (el mas recomendado)
- Las siguientes bibliotecas (incluidas en el archivo `requirementos.txt`):
  - `tkinter`
  - `json`
  - `os`
  - `threading`
  - `time`

## Instalación
1. **Descarga el proyecto**:
   - Puedes clonar el repositorio o descargar los archivos directamente.
2. **Asegúrate de tener Python instalado**:
   - Verifica tu versión de Python ejecutando:
     ```bash
     python --version
     ```
3. **(Opcional) Instala las dependencias**:
   - Si deseas instalar las dependencias listadas en `requirementos.txt`, ejecuta:
     ```bash
     pip install -r requirementos.txt
     ```

## Uso
1. Ejecuta el archivo principal del proyecto:
   ```bash
   python CalculadoraTkinter.py


Usa la interfaz gráfica para:
Añadir nuevas tareas con sus respectivas categorías.
Editar, eliminar o marcar tareas como completadas.
Buscar tareas escribiendo en el cuadro de texto superior.
Guarda tus tareas para mantenerlas entre sesiones.
Archivos del Proyecto
CalculadoraTkinter.py: Código principal del programa.
mis_tareas.json: Archivo donde se almacenan las tareas guardadas.
requirementos.txt: Archivo que lista las dependencias necesarias.
LEEME.md: Documentación del proyecto.
Autor
[Diego Alejandro Ceballos Rodriguez]




