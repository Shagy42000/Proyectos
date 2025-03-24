# Importar módulos necesarios
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  


def main():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Agenda Personal")
    root.geometry("800x500")

    # Función para agregar eventos
    def agregar_evento():
        # Obtener valores de los campos
        fecha = date_entry.get()
        hora = time_entry.get()
        descripcion = desc_entry.get()

        # Validar campos vacíos
        if not (fecha and hora and descripcion):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Insertar en el TreeView
        treeview.insert('', tk.END, values=(fecha, hora, descripcion))

        # Limpiar campos de entrada
        time_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)

    # Función para eliminar eventos
    def eliminar_evento():
        seleccion = treeview.selection()
        if not seleccion:
            messagebox.showinfo("Información", "Seleccione un evento para eliminar")
            return

        # Diálogo de confirmación
        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            treeview.delete(seleccion[0])

    # Frame principal para organización
    main_frame = ttk.Frame(root)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Sección de visualización (TreeView)
    tree_frame = ttk.Frame(main_frame)
    tree_frame.pack(fill=tk.BOTH, expand=True)

    # Configurar TreeView
    columnas = ("Fecha", "Hora", "Descripción")
    treeview = ttk.Treeview(
        tree_frame,
        columns=columnas,
        show="headings",
        selectmode="browse"
    )

    # Configurar columnas
    for col in columnas:
        treeview.heading(col, text=col)
        treeview.column(col, width=100, anchor=tk.W)

    # Scrollbar vertical
    scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    treeview.pack(fill=tk.BOTH, expand=True)

    # Sección de entrada de datos
    input_frame = ttk.Frame(main_frame)
    input_frame.pack(pady=10, fill=tk.X)

    # Selector de fecha
    ttk.Label(input_frame, text="Fecha:").grid(row=0, column=0, padx=5)
    date_entry = DateEntry(
        input_frame,
        date_pattern="dd/mm/yyyy",
        locale="es_ES"
    )
    date_entry.grid(row=0, column=1, padx=5)

    # Entrada para hora
    ttk.Label(input_frame, text="Hora:").grid(row=0, column=2, padx=5)
    time_entry = ttk.Entry(input_frame, width=10)
    time_entry.grid(row=0, column=3, padx=5)

    # Entrada para descripción
    ttk.Label(input_frame, text="Descripción:").grid(row=0, column=4, padx=5)
    desc_entry = ttk.Entry(input_frame, width=30)
    desc_entry.grid(row=0, column=5, padx=5)

    # Sección de botones
    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(pady=5, fill=tk.X)

    btn_agregar = ttk.Button(
        btn_frame,
        text="Agregar Evento",
        command=agregar_evento
    )
    btn_agregar.pack(side=tk.LEFT, padx=5)

    btn_eliminar = ttk.Button(
        btn_frame,
        text="Eliminar Evento",
        command=eliminar_evento
    )
    btn_eliminar.pack(side=tk.LEFT, padx=5)

    btn_salir = ttk.Button(
        btn_frame,
        text="Salir",
        command=root.destroy
    )
    btn_salir.pack(side=tk.RIGHT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()