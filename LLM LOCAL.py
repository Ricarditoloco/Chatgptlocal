import tkinter as tk
from transformers import AutoTokenizer, AutoModelForCausalLM

# Cargar el modelo y el tokenizador
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b-it")

# Función para generar el poema
def generate_poem():
    input_text = text_entry.get()  # Obtener el texto de la entrada
    input_ids = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**input_ids)
    poem = tokenizer.decode(outputs[0])
    output_label.config(text=poem)  # Mostrar el poema en la etiqueta de salida

# Crear la ventana principal
root = tk.Tk()
root.title("Chat Gpt Local")

# Crear la entrada de texto
text_entry = tk.Entry(root, width=50)
text_entry.pack(padx=20, pady=10)  # Añadir espacio en los costados y en la parte superior e inferior

# Crear el botón de generación de poema
generate_button = tk.Button(root, text="Generar Respuesta", command=generate_poem)
generate_button.pack(pady=5)

# Crear la etiqueta para mostrar el poema generado
output_label = tk.Label(root, text="", wraplength=400, justify="center")
output_label.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()

