
import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
import threading
import time

class GestorTareas:
    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Gestor de Tareas")
        self.ventana.geometry("500x600")

        self.tareas = []
        self.archivo_tareas = "mis_tareas.json"
        

        self.crear_interfaz()

        self.cargar_tareas()

    def crear_interfaz(self):

        tk.Label(self.ventana, text="Mi Gestor de Tareas", font=("Arial", 18, "bold")).pack(pady=10)

        self.busqueda_entry = tk.Entry(self.ventana, width=50)
        self.busqueda_entry.pack(pady=10)
        self.busqueda_entry.bind("<KeyRelease>", self.buscar_tarea) 


        self.lista_tareas = tk.Listbox(self.ventana, width=50, height=15)
        self.lista_tareas.pack(pady=10)

   
        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=10)

     
        botones = [
            ("Añadir Tarea", self.añadir_tarea),
            ("Editar Tarea", self.editar_tarea),
            ("Eliminar Tarea", self.eliminar_tarea),
            ("Marcar Completada", self.completar_tarea),
            ("Guardar Tareas", self.guardar_tareas)
        ]


        for (texto, comando) in botones:
            tk.Button(marco_botones, text=texto, command=comando).pack(side=tk.LEFT, padx=5)

    def añadir_tarea(self):

        tarea = simpledialog.askstring("Nueva Tarea", "Introduce la descripción de la tarea:")
        if tarea:

            categoria = simpledialog.askstring("Categoría", "Introduce la categoría de la tarea (Trabajo, Personal, etc.):")
            if not categoria:
                categoria = "Sin Categoría" 

 
            recordatorio = simpledialog.askstring("Recordatorio", "¿En cuántos segundos quieres un recordatorio? (Deja en blanco si no deseas):")
            
            if recordatorio == "":
                recordatorio = None  
                messagebox.showinfo("Recordatorio", "Tarea Agregada")
            else:
                try:
                    recordatorio = int(recordatorio)  
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingresa un número válido para el recordatorio.")
                    return

          
            tarea_obj = {"descripcion": tarea, "categoria": categoria, "completada": False, "recordatorio": recordatorio}
            self.tareas.append(tarea_obj)
            self.actualizar_lista_tareas()

          
            if recordatorio:
                threading.Thread(target=self.enviar_recordatorio, args=(tarea, recordatorio)).start()

    def editar_tarea(self):
       
        try:
            indice = self.lista_tareas.curselection()[0]
            tarea_actual = self.tareas[indice]["descripcion"]
            
     
            nueva_tarea = simpledialog.askstring("Editar Tarea", "Edita la tarea:", initialvalue=tarea_actual)
            if nueva_tarea:
                self.tareas[indice]["descripcion"] = nueva_tarea
                self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea para editar")

    def eliminar_tarea(self):
    
        try:
            indice = self.lista_tareas.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea para eliminar")

    def completar_tarea(self):

        try:
            indice = self.lista_tareas.curselection()[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista_tareas()
        except IndexError:
            messagebox.showwarning("Error", "Por favor, selecciona una tarea para marcar como completada")

    def actualizar_lista_tareas(self):
     
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "✓" if tarea["completada"] else "○"
            self.lista_tareas.insert(tk.END, f"{estado} {tarea['descripcion']} [{tarea['categoria']}]")

    def buscar_tarea(self, event=None):
  
        texto_busqueda = self.busqueda_entry.get().lower()
        tareas_filtradas = [tarea for tarea in self.tareas if texto_busqueda in tarea['descripcion'].lower()]

        self.lista_tareas.delete(0, tk.END)
        for tarea in tareas_filtradas:
            estado = "✓" if tarea["completada"] else "○"
            self.lista_tareas.insert(tk.END, f"{estado} {tarea['descripcion']} [{tarea['categoria']}]")

    def guardar_tareas(self):
     
        with open(self.archivo_tareas, "w") as archivo:
            json.dump(self.tareas, archivo)
        messagebox.showinfo("Guardado", "¡Tareas guardadas exitosamente!")

    def cargar_tareas(self):
        
        if os.path.exists(self.archivo_tareas):
            with open(self.archivo_tareas, "r") as archivo:
                self.tareas = json.load(archivo)
                self.actualizar_lista_tareas()

    def enviar_recordatorio(self, tarea, tiempo):
       
        time.sleep(tiempo)
        messagebox.showinfo("Recordatorio", f"¡Recuerda: {tarea}!")

    def ejecutar(self):
      
        self.ventana.mainloop()

if __name__ == "__main__":
    app = GestorTareas()
    app.ejecutar()
