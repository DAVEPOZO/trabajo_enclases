import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar los datos de los alumnos
alumnos = {}

# Función para calcular la calificación según la nota
def calcular_calificacion(nota):
    if nota < 5:
        return "SS"
    elif nota < 7:
        return "AP"
    elif nota < 9:
        return "NT"
    else:
        return "SB"

# Ventana para introducir alumno
def ventana_introducir():
    ventana = tk.Toplevel(root)
    ventana.title("Introducir Alumno")

    tk.Label(ventana, text="DNI:").grid(row=0, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.grid(row=0, column=1)

    tk.Label(ventana, text="Apellidos:").grid(row=1, column=0)
    entry_apellidos = tk.Entry(ventana)
    entry_apellidos.grid(row=1, column=1)

    tk.Label(ventana, text="Nombre:").grid(row=2, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=2, column=1)

    tk.Label(ventana, text="Nota:").grid(row=3, column=0)
    entry_nota = tk.Entry(ventana)
    entry_nota.grid(row=3, column=1)

    def introducir_alumno():
        dni = entry_dni.get()
        apellidos = entry_apellidos.get()
        nombre = entry_nombre.get()
        try:
            nota = float(entry_nota.get())
            if dni in alumnos:
                messagebox.showerror("Error", "Ya existe un alumno con este DNI.")
                return
            alumnos[dni] = [apellidos, nombre, nota, calcular_calificacion(nota)]
            messagebox.showinfo("Éxito", "Alumno añadido correctamente.")
            ventana.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce una nota válida.")

    tk.Button(ventana, text="Añadir", command=introducir_alumno).grid(row=4, columnspan=2, pady=10)

# Ventana para eliminar alumno
def ventana_eliminar():
    ventana = tk.Toplevel(root)
    ventana.title("Eliminar Alumno")

    tk.Label(ventana, text="DNI:").grid(row=0, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.grid(row=0, column=1)

    def eliminar_alumno():
        dni = entry_dni.get()
        if dni in alumnos:
            del alumnos[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

    tk.Button(ventana, text="Eliminar", command=eliminar_alumno).grid(row=1, columnspan=2, pady=10)

# Ventana para consultar alumno
def ventana_consultar():
    ventana = tk.Toplevel(root)
    ventana.title("Consultar Alumno")

    tk.Label(ventana, text="DNI:").grid(row=0, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.grid(row=0, column=1)

    def consultar_alumno():
        dni = entry_dni.get()
        if dni in alumnos:
            apellidos, nombre, nota, calificacion = alumnos[dni]
            messagebox.showinfo("Consulta", f"{dni} {apellidos}, {nombre} {nota} {calificacion}")
        else:
            messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")
        ventana.destroy()

    tk.Button(ventana, text="Consultar", command=consultar_alumno).grid(row=1, columnspan=2, pady=10)

# Ventana para modificar la nota de un alumno
def ventana_modificar():
    ventana = tk.Toplevel(root)
    ventana.title("Modificar Nota")

    tk.Label(ventana, text="DNI:").grid(row=0, column=0)
    entry_dni = tk.Entry(ventana)
    entry_dni.grid(row=0, column=1)

    tk.Label(ventana, text="Nueva Nota:").grid(row=1, column=0)
    entry_nota = tk.Entry(ventana)
    entry_nota.grid(row=1, column=1)

    def modificar_nota():
        dni = entry_dni.get()
        try:
            nueva_nota = float(entry_nota.get())
            if dni in alumnos:
                alumnos[dni][2] = nueva_nota
                alumnos[dni][3] = calcular_calificacion(nueva_nota)
                messagebox.showinfo("Éxito", "Nota modificada correctamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce una nota válida.")

    tk.Button(ventana, text="Modificar", command=modificar_nota).grid(row=2, columnspan=2, pady=10)

# Ventana para mostrar alumnos por tipo
def ventana_mostrar(tipo):
    ventana = tk.Toplevel(root)
    ventana.title(f"Mostrar {tipo}")

    texto = ""
    for dni, (apellidos, nombre, nota, calificacion) in alumnos.items():
        if (tipo == "Suspensos" and calificacion == "SS") or \
           (tipo == "Aprobados" and calificacion in ["AP", "NT", "SB"]) or \
           (tipo == "Candidatos a MH" and nota == 10):
            texto += f"{dni} {apellidos}, {nombre} {nota} {calificacion}\n"

    tk.Label(ventana, text=texto or f"No hay alumnos {tipo.lower()}").pack(pady=10)

# Interfaz principal
root = tk.Tk()
root.title("Gestión de Calificaciones")

tk.Button(root, text="Introducir Alumno", command=ventana_introducir).pack(pady=5)
tk.Button(root, text="Eliminar Alumno", command=ventana_eliminar).pack(pady=5)
tk.Button(root, text="Consultar Alumno", command=ventana_consultar).pack(pady=5)
tk.Button(root, text="Modificar Nota", command=ventana_modificar).pack(pady=5)
tk.Button(root, text="Mostrar Suspensos", command=lambda: ventana_mostrar("Suspensos")).pack(pady=5)
tk.Button(root, text="Mostrar Aprobados", command=lambda: ventana_mostrar("Aprobados")).pack(pady=5)
tk.Button(root, text="Mostrar Candidatos a MH", command=lambda: ventana_mostrar("Candidatos a MH")).pack(pady=5)

root.mainloop()
