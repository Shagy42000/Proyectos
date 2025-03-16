# Importar la librería Tkinter para crear la interfaz gráfica
import tkinter as tk

# Función para agregar datos a la lista desde el campo de entrada
def agregar():
    texto = entrada.get().strip()  # Obtener texto y eliminar espacios en blanco
    if texto:  # Verificar que el texto no esté vacío
        lista.insert(tk.END, texto)  # Añadir texto al final de la lista
        entrada.delete(0, tk.END)  # Limpiar el campo de entrada

# Función para limpiar el campo de entrada y la lista completa
def limpiar():
    entrada.delete(0, tk.END)  # Limpiar campo de entrada
    lista.delete(0, tk.END)  # Eliminar todos los elementos de la lista

# Configuración inicial de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI - Gestor de Datos")  # Título descriptivo
ventana.geometry("500x400")  # Tamaño inicial de la ventana

# Configurar expansión de filas y columnas para mejor redimensionamiento
ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Creación y posicionamiento de widgets
# Etiqueta informativa
tk.Label(ventana, text="Ingrese su dato:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)

# Campo de entrada de texto
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Botón para agregar datos (con atajo de teclado Enter)
tk.Button(ventana, text="Agregar (Enter)", command=agregar).grid(
    row=1, column=0, padx=10, pady=5, sticky="ew"
)
entrada.bind("<Return>", lambda event: agregar())  # Vincula Enter a la función agregar

# Botón para limpiar contenido
tk.Button(ventana, text="Limpiar Todo", command=limpiar).grid(
    row=1, column=1, padx=10, pady=5, sticky="ew"
)

# Componente Listbox con Scrollbar para mostrar datos
marco_lista = tk.Frame(ventana)
marco_lista.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

scrollbar = tk.Scrollbar(marco_lista)
lista = tk.Listbox(
    marco_lista,
    width=50,
    yscrollcommand=scrollbar.set,
    selectbackground="#a0a0a0",  # Color de selección personalizado
)
scrollbar.config(command=lista.yview)

# Empaquetado de componentes en el marco
lista.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Iniciar el bucle principal de la aplicación
ventana.mainloop()