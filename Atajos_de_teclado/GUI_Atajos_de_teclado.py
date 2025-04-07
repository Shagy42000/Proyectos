import tkinter as tk
from tkinter import ttk

# Función para añadir nuevas tareas a la lista
def agregar_tarea(event=None):
    """Obtiene el texto del campo de entrada, lo añade a la lista y limpia el campo"""
    tarea = entrada.get()  # Obtenemos el texto del Entry
    if tarea:  # Verificamos que no esté vacío
        lista_tareas.insert(tk.END, tarea)  # Insertamos al final de la lista
        lista_tareas.itemconfig(tk.END, {'bg': 'white'})  # Color inicial blanco
        entrada.delete(0, tk.END)  # Limpiamos el campo de entrada

# Función para marcar tareas como completadas
def marcar_completada(event=None):
    """Cambia el color de fondo de la tarea seleccionada a verde claro"""
    if root.focus_get() == entrada:  # Evita acción si el foco está en el Entry
        return
    try:
        indice = lista_tareas.curselection()[0]  # Índice de la tarea seleccionada
        lista_tareas.itemconfig(indice, {'bg': '#d0f0c0', 'fg': '#404040'})  # Cambia color
    except IndexError:  # Si no hay selección
        pass

# Función para eliminar tareas seleccionadas
def eliminar_tarea(event=None):
    """Elimina la tarea seleccionada de la lista"""
    if root.focus_get() == entrada:  # Evita acción durante la edición del texto
        return
    try:
        indice = lista_tareas.curselection()[0]  # Índice de la tarea
        lista_tareas.delete(indice)  # Elimina de la lista
    except IndexError:  # Si no hay selección
        pass

# Configuración inicial de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas - Productivo v1.0")
root.geometry("500x400")
root.configure(padx=10, pady=10, bg='#f0f0f0')  # Márgenes y color de fondo

# --------------------------------------------------
# Sección Superior: Campo de entrada y botón Añadir
# --------------------------------------------------
frame_superior = tk.Frame(root, bg='#f0f0f0')
frame_superior.pack(fill='x')  # Empaca el frame horizontalmente

# Campo de entrada de texto
entrada = tk.Entry(
    frame_superior,
    font=('Arial', 12),
    relief='flat',  # Borde plano
    highlightthickness=1  # Grosor del borde al enfocar
)
entrada.pack(side='left', fill='x', expand=True, padx=5)

# Botón para añadir tareas
boton_agregar = tk.Button(
    frame_superior,
    text="➕ Añadir",
    command=agregar_tarea,
    bg='#4CAF50',  # Verde
    fg='white',
    relief='flat',  # Sin relieve
    activebackground='#45a049'  # Color al hacer clic
)
boton_agregar.pack(side='left', padx=5)

# --------------------------------------------------
# Sección Central: Lista de tareas con Scrollbar
# --------------------------------------------------
frame_central = tk.Frame(root, bg='#f0f0f0')
frame_central.pack(fill='both', expand=True, pady=10)

# Componente Listbox para mostrar las tareas
lista_tareas = tk.Listbox(
    frame_central,
    font=('Arial', 12),
    selectbackground='#e0e0e0',  # Color de selección
    activestyle='none',  # Sin subrayado al seleccionar
    relief='flat',
    highlightthickness=0  # Sin borde de enfoque
)

# Scrollbar vertical
scrollbar = tk.Scrollbar(frame_central)
lista_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas.yview)

# Empacar componentes
lista_tareas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# --------------------------------------------------
# Sección Inferior: Botones de Acción
# --------------------------------------------------
frame_inferior = tk.Frame(root, bg='#f0f0f0')
frame_inferior.pack(fill='x')

# Botón para marcar como completada
boton_completada = tk.Button(
    frame_inferior,
    text="✓ Completada",
    command=marcar_completada,
    bg='#2196F3',  # Azul
    fg='white',
    relief='flat',
    activebackground='#1e88e5'
)
boton_completada.pack(side='left', padx=5)

# Botón para eliminar tareas
boton_eliminar = tk.Button(
    frame_inferior,
    text="🗑 Eliminar",
    command=eliminar_tarea,
    bg='#f44336',  # Rojo
    fg='white',
    relief='flat',
    activebackground='#e53935'
)
boton_eliminar.pack(side='left', padx=5)

# ==================================================
# Configuración de Atajos de Teclado
# ==================================================
entrada.bind('<Return>', agregar_tarea)  # Enter para añadir
root.bind('<c>', marcar_completada)     # Tecla C para completar
root.bind('<d>', eliminar_tarea)        # Tecla D para eliminar
root.bind('<Escape>', lambda e: root.destroy())  # Escape para salir

# ==================================================
# Estilos Adicionales y Configuraciones Finales
# ==================================================
ttk.Style().configure('TButton', padding=5, relief='flat')  # Estilo uniforme

# Iniciar el bucle principal de la aplicación
if __name__ == "__main__":
    root.mainloop()