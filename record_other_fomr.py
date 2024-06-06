import subprocess
from time import sleep
# from pynput.keyboard import Key, Controller
# from pynput.mouse import Button, Controller
from pynput import mouse,keyboard
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from obswebsocket import obsws, requests

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Grabacion con OBS")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.title("Grab")
        self.ventana1.geometry("300x100")
        self.agregar_componentes()
        self.agregar_menu()
        self.ventana1.mainloop()

    def agregar_componentes(self):
        self.label1=ttk.Label(self.labelframe1, text="Intervalo")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0, padx=5, pady=5)
        self.boton1=ttk.Button(self.labelframe1, text="Ejecutar Grabacion", command=self.obs_record)
        self.boton1.grid(column=1, row=2, padx=5, pady=5, sticky="we")

    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Acerca de...", command=self.acerca)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1) 
    
    def close_obs(self):
        self.keyboar.press(keyboard.Key.alt)
        sleep(0.7)
        self.keyboar.press(keyboard.Key.f4)
        self.keyboar.release(keyboard.Key.alt)
        sleep(0.1)
        with self.keyboar.pressed(keyboard.Key.alt):
            self.keyboar.release(keyboard.Key.alt)
        with self.keyboar.pressed(keyboard.Key.f4):
            self.keyboar.release(keyboard.Key.f4)
        self.ventana1.title("Grab")

    def obs_record(self):
        if self.dato1.get()=="":
            mb.showerror("Cuidado","No puede dejar el cuadro de entrada en blanco")
        else:
            # Ruta al archivo batch (.bat)
            ruta_archivo_ejecucion = "execute.bat"

            # Ejecutar el archivo batch
            self.ventana1.title("Recording...")
            proceso = subprocess.Popen(ruta_archivo_ejecucion, shell=True)
            sleep(4)
            proceso.terminate()

            self.keyboar = keyboard.Controller()
            self.mous = mouse.Controller()

            self.mous.position=(800,120)
            self.mous.position=(800,120)
            self.mous.press(mouse.Button.left)
            self.mous.release(mouse.Button.left)
            self.mous.position=(800,250)
            self.mous.press(mouse.Button.left)
            self.mous.release(mouse.Button.left)
            self.mous.position=(869,392)
            sleep(0.2)
            self.mous.press(mouse.Button.left)
            self.mous.release(mouse.Button.left)
            self.keyboar.press(keyboard.Key.delete)
            sleep(0.1)
            self.keyboar.press(keyboard.Key.delete)

            self.keyboar.press(keyboard.Key.delete)
            numero = self.dato1.get()
            if 0<= int(numero) <=60:
                for digito in numero:
                    if digito.isdigit():
                        key = keyboard.KeyCode.from_char(digito)
                        self.keyboar.press(key)
                        self.keyboar.release(key)

            else:
                mb.showerror("Cuidado","La entrada debe estar entre 0 y 60")
                self.close_obs()
            sleep(0.1)
            self.mous.position=(1012,520)
            self.mous.press(mouse.Button.left)
            sleep(0.1)
            self.mous.release(mouse.Button.left)

            self.mous.position = (1100,520)
            self.mous.press(mouse.Button.left)
            self.mous.release(mouse.Button.left)

            sleep(int(self.dato1.get())+0.5)
            self.ventana1.title("Closing OBS...")
            self.close_obs()
            self.ventana1.title("Grab")
            

    def acerca(self):
        mb.showinfo("Información", "Grabacion de programas con OBS.")
        
aplicacion1=Aplicacion() 