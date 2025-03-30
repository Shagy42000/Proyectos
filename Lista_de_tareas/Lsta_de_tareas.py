import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Configuración de la interfaz gráfica
        self._crear_widgets()
        self._configurar_layout()
        self._bind_eventos()

    def _crear_widgets(self):
        """Crea y configura los widgets de la interfaz."""
        # Campo de entrada para nuevas tareas
        self.entrada = tk.Entry(self.root, font=('Arial', 12))
        # Botones de acción
        self.btn_agregar = tk.Button(self.root, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_marcar = tk.Button(self.root, text="Marcar Completada", command=self.marcar_completada)
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        # Contenedor para la lista y scrollbar
        self.frame_lista = tk.Frame(self.root)
        self.lista = tk.Listbox(self.frame_lista, font=('Arial', 12), selectbackground="#a6a6a6", height=15)
        self.scrollbar = tk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.lista.yview)
        self.lista.configure(yscrollcommand=self.scrollbar.set)

    def _configurar_layout(self):
        """Organiza los widgets en la ventana usando grid."""
        self.entrada.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky='ew')
        self.btn_agregar.grid(row=1, column=0, padx=2, pady=2, sticky='ew')
        self.btn_marcar.grid(row=1, column=1, padx=2, pady=2, sticky='ew')
        self.btn_eliminar.grid(row=1, column=2, padx=2, pady=2, sticky='ew')
        self.frame_lista.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky='nsew')
        self.lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Configura expansión de fila/columna
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(2, weight=1)

    def _bind_eventos(self):
        """Vincula eventos de teclado y ratón."""
        self.entrada.bind('<Return>', lambda e: self.agregar_tarea())
        self.lista.bind('<Double-Button-1>', lambda e: self.marcar_completada())

    def agregar_tarea(self):
        """Añade una nueva tarea a la lista."""
        tarea = self.entrada.get().strip()
        if tarea:
            self.lista.insert(tk.END, f"[ ] {tarea}")
            self.entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea.")

    def marcar_completada(self):
        """Marca o desmarca una tarea como completada."""
        seleccionado = self.lista.curselection()
        if seleccionado:
            indice = seleccionado[0]
            tarea = self.lista.get(indice)
            # Cambia el estado y el color de fondo
            if tarea.startswith("[ ] "):
                nueva_tarea = tarea.replace("[ ] ", "[✓] ", 1)
                color = "#d0f0d0"  # Verde claro
            else:
                nueva_tarea = tarea.replace("[✓] ", "[ ] ", 1)
                color = "#ffffff"  # Blanco
            self.lista.delete(indice)
            self.lista.insert(indice, nueva_tarea)
            self.lista.itemconfig(indice, {'bg': color})

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada."""
        seleccionado = self.lista.curselection()
        if seleccionado:
            self.lista.delete(seleccionado[0])


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()