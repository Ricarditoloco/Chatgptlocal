# Introduccion
Este código permite crear un chatbot sencillo con una interfaz casera utilizando Gemma 2b it.
Introducción a los modelos de Gemma 2 it
Gemma 2 it es una familia de modelos de lenguaje de gran tamaño (LLM) de Google AI, entrenados con un enfoque en la eficiencia y el rendimiento en dispositivos móviles. Estos modelos están diseñados para ser ligeros y rápidos, sin sacrificar la precisión o la calidad de la generación de texto.

Características principales:

Eficiencia: Los modelos de Gemma 2 it son significativamente más pequeños que otros LLM comparables, lo que los hace ideales para dispositivos con recursos limitados.
Rendimiento: Estos modelos son rápidos y receptivos, lo que los hace ideales para aplicaciones interactivas.
Precisión: Los modelos de Gemma 2 it generan texto de alta calidad, con una amplia gama de capacidades lingüísticas.
Flexibilidad: Los modelos están disponibles en diferentes tamaños y configuraciones, lo que permite a los desarrolladores elegir la mejor opción para sus necesidades.
Aplicaciones:

Los modelos de Gemma 2 it se pueden utilizar para una amplia gama de aplicaciones, como:

Traducción automática: Los modelos pueden traducir texto de un idioma a otro con precisión y fluidez.
Generación de texto: Los modelos pueden generar texto creativo, como poemas, historias, guiones y código.
Resumen de texto: Los modelos pueden resumir textos largos de manera precisa y concisa.
Respuesta a preguntas: Los modelos pueden responder a preguntas sobre una amplia gama de temas.

# El siguiente código muestra un ejemplo sencillo de cómo interactuar con el modelo Gemma 2 it usando la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI).
# Instalación:
Para poder usar el siguiente código, es necesario tener instaladas las siguientes librerías:

Tkinter: biblioteca para la creación de interfaces gráficas de usuario en Python.
PyTorch: biblioteca para el aprendizaje profundo.
Hugging Face: biblioteca para la carga y uso de modelos de lenguaje pre-entrenados.
Instalación de las librerías:

Puedes instalar las librerías usando el comando pip de la siguiente manera:

pip install tkinter
pip install pytorch
pip install transformers


# Además de las librerías, es necesario descargar el modelo de Gemma 2b-it. Puedes hacerlo usando el siguiente comando:

huggingface-cli download google/gemma-2b-it
Este comando descargará automáticamente el modelo completo, que pesa aproximadamente 35 GB.

# Aclaraciones sobre el código de ejemplo:
Funcionalidad:

Es importante tener en cuenta que el código proporcionado es solo un ejemplo y no está diseñado para ser una implementación completa y funcional. Su objetivo es mostrar cómo interactuar con el modelo Gemma 2b-it utilizando Tkinter y proporcionar una base para que puedas desarrollar tu propia aplicación.

# Pruebas de ejecución
![image](https://github.com/Ricarditoloco/Chatgptlocal/assets/107517375/50304bc7-4601-43d6-9afa-f0353bf635a7)

![image](https://github.com/Ricarditoloco/Chatgptlocal/assets/107517375/a1693fb2-7925-4079-972f-6cccdc123be3)

Cada vez que generes el texto, solo necesitas borrar tu búsqueda anterior y hacer clic nuevamente en el botón de generar búsqueda. No es necesario volver a ejecutar todo el código.
# Comparativo de Entradas de Texto en Español vs. Inglés

![image](https://github.com/Ricarditoloco/Chatgptlocal/assets/107517375/ee155333-420e-4f82-baa9-b3161d3a6e6d)

![image](https://github.com/Ricarditoloco/Chatgptlocal/assets/107517375/fbc884d4-6fc4-4804-b7c7-82f1bdc3adfb)

Está claro que se obtiene un mejor rendimiento al utilizar entradas de texto en inglés, pero también permite introducirlas en español sin ningún problema.



# Rendimiento:

Las pruebas las realice con una laptop con 16 GB de RAM, un Ryzen 5 5000 series y sin tarjeta gráfica son válidas para este código de ejemplo. Sin embargo, el rendimiento puede variar en función de la complejidad de la tarea que se le asigne al modelo y de las especificaciones de tu equipo.

# Limitaciones:

Es importante recordar que este código de ejemplo tiene algunas limitaciones:

No maneja preguntas complejas o ambiguas.
No tiene en cuenta la gestión de errores.
La interfaz gráfica de usuario es básica y puede mejorarse.
Recomendaciones:

Si deseas desarrollar una aplicación completa y funcional, te recomiendo que:

Profundices en la documentación oficial de Gemma 2b-it y Tkinter.
Implementes la gestión de errores para manejar las excepciones que puedan surgir.
Mejore la interfaz gráfica de usuario para que sea más atractiva y fácil de usar.

Agradezco tu interés en el código de ejemplo y espero que esta información te sea útil para desarrollar tu propia aplicación.
