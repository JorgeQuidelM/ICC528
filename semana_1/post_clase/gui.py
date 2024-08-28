import tkinter as tk
from tkinter import messagebox
from cifrado_cesar import cifrar, descifrar


def crear_ventana(titulo, dimensiones):
    ventana = tk.Tk()
    ventana.title(titulo)
    ventana.geometry(dimensiones)
    ventana.config(bg='#D3D3D3')
    ventana.resizable(False, False)
    return ventana


def crear_etiqueta(master, mensaje):
    etiqueta = tk.Label(master=master, text=mensaje, font=('Arial', 13), bg='#D3D3D3')
    etiqueta.pack(pady=10)
    return etiqueta


def crear_entrada(master, ancho):
    entrada = tk.Entry(master=master, width=ancho, font=('Arial', 10))
    entrada.pack(pady=5)
    return entrada


def crear_boton(master, mensaje, comando):
    boton = tk.Button(master=master, text=mensaje, height=2, width=20, relief='flat', command=comando, bg="#000000", fg='#FFFFFF')
    boton.pack(pady=10)
    return boton


def configurar_ventana(ventana):
    crear_etiqueta(ventana, "Ingrese el mensaje:")
    entrada_mensaje = crear_entrada(ventana, 50)

    crear_etiqueta(ventana, "Ingrese la clave de desplazamiento:")
    entrada_clave = crear_entrada(ventana, 50)

    crear_etiqueta(ventana, "Ingrese el alfabeto:")
    entrada_alfabeto = crear_entrada(ventana, 50)

    etiqueta_cifrado = crear_etiqueta(ventana, "Mensaje cifrado:")
    etiqueta_descifrado = crear_etiqueta(ventana, "Mensaje descifrado:")

    comando = lambda: procesar(entrada_mensaje, entrada_clave, entrada_alfabeto, etiqueta_cifrado, etiqueta_descifrado)
    crear_boton(ventana, "Procesar", comando)


def procesar(entrada_mensaje, entrada_clave, entrada_alfabeto, etiqueta_cifrado, etiqueta_descifrado):
    mensaje = entrada_mensaje.get()
    clave = entrada_clave.get()
    alfabeto = entrada_alfabeto.get()
    try:
        clave = int(clave)
    except ValueError:
        messagebox.showerror("Error", "La clave debe ser un número entero.")
        return

    mensaje_cifrado = cifrar(mensaje, clave, alfabeto)
    mensaje_descifrado = descifrar(mensaje_cifrado, clave, alfabeto)

    etiqueta_cifrado.config(text=f"Mensaje cifrado: {mensaje_cifrado}")
    etiqueta_descifrado.config(text=f"Mensaje descifrado: {mensaje_descifrado}")


def main():
    ventana = crear_ventana("Cifrado y Descifrado", "800x500")
    configurar_ventana(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
