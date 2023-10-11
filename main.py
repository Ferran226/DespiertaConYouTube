import tkinter as tk
import time
import webbrowser
from datetime import datetime
import threading


# URL específico a reproducir cuando se active la alarma
ALARMA_URL = "https://www.youtube.com/watch?v=j7dAe8vzFkw"

# Función para configurar una alarma
# Validación para los campos de entrada
def configurar_alarma():
    hora = int(hora_entry.get())
    minuto = int(minuto_entry.get())

    # Validar la hora
    if hora < 0 or hora > 23:
        raise ValueError("La hora debe estar entre 0 y 23.")

    # Validar el minuto
    if minuto < 0 or minuto > 59:
        raise ValueError("El minuto debe estar entre 0 y 59.")

    return datetime(datetime.now().year, datetime.now().month, datetime.now().day, hora, minuto)

# Función para reproducir el URL de la alarma
def reproducir_alarma():
    webbrowser.open(ALARMA_URL)

# Función para verificar si es hora de la alarma
def comprobar_alarma():
    try:
        alarma = configurar_alarma()
    except ValueError as e:
        resultado_label.config(text=e.args[0])
        return

    while True:
        now = datetime.now()
        if now >= alarma:
            resultado_label.config(text="La alarma se activó.")
            reproducir_alarma()  # Reproducir el URL de la alarma
            break
        else:
            resultado_label.config(text="Esperando la alarma...")
            time.sleep(10)  # Espera 10 segundos entre comprobaciones

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Reloj Despertador con Reproducción de YouTube")
ventana.geometry("400x200")  # Tamaño de la ventana: 400x200 píxeles

# Etiquetas y campos de entrada
hora_label = tk.Label(ventana, text="Hora (0-23):")
hora_label.pack()
hora_entry = tk.Entry(ventana)
hora_entry.pack()

minuto_label = tk.Label(ventana, text="Minuto (0-59):")
minuto_label.pack()
minuto_entry = tk.Entry(ventana)
minuto_entry.pack()

# Función para iniciar la comprobación de la alarma
def iniciar_comprobar_alarma():
    thread = threading.Thread(target=comprobar_alarma)
    thread.daemon = True  # El hilo se detendrá cuando se cierre la aplicación
    thread.start()

# Botón para configurar la alarma
configurar_button = tk.Button(ventana, text="Configurar Alarma", command=iniciar_comprobar_alarma)
configurar_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Mostrar la hora actual en tiempo real
def mostrar_hora_actual():
    hora_actual = time.strftime("%H:%M:%S")
    hora_actual_label.config(text=f"Hora Actual: {hora_actual}")
    ventana.after(1000, mostrar_hora_actual)

hora_actual_label = tk.Label(ventana, text="", font=("Helvetica", 12))
hora_actual_label.pack()
mostrar_hora_actual()

ventana.mainloop()







