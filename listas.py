import tkinter as tk
from tkinter import messagebox


class FrmUsuarios(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestión de Usuarios")
        self.geometry("400x400")

        # Lista para almacenar usuarios
        self.usuarios = []

        # Etiquetas y campos
        tk.Label(self, text="Nombre de usuario:").pack(pady=5)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)

        # Botones
        btn_agregar = tk.Button(self, text="Agregar Usuario", command=self.agregar_usuario)
        btn_agregar.pack(pady=5)

        btn_listar = tk.Button(self, text="Listar Usuarios", command=self.listar_usuarios)
        btn_listar.pack(pady=5)

        btn_salir = tk.Button(self, text="Salir", command=self.quit)
        btn_salir.pack(pady=5)

        # Área de lista
        self.lista_box = tk.Listbox(self, width=40, height=10)
        self.lista_box.pack(pady=10)

    def agregar_usuario(self):
        nombre = self.entry_usuario.get().strip()
        if nombre:
            self.usuarios.append(nombre)
            self.lista_box.insert(tk.END, nombre)
            self.entry_usuario.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' agregado.")
        else:
            messagebox.showwarning("Error", "El campo de usuario no puede estar vacío.")

    def listar_usuarios(self):
        if self.usuarios:
            lista = "\n".join(self.usuarios)
            messagebox.showinfo("Usuarios Registrados", lista)
        else:
            messagebox.showinfo("Usuarios", "No hay usuarios registrados.")


if __name__ == "__main__":
    app = FrmUsuarios()
    app.mainloop()
