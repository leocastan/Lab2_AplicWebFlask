#Importar la biblioteca de flask y librerias necesarias
from tkinter import messagebox
from flask import Flask, redirect, render_template, request, url_for, flash
import pickle

#Instanciar la aplicación
#Nombre por defecto y ruta donde están los modelos
app = Flask(__name__)


#Arreglo para almacenar las tareas
lista_tareas = []

#1. Funcion controlador que muestra lista actual de tareas pendientes y un formulario para ingresar un nuevo elemento
#Definicion de la ruta por defecto,
@app.route('/')
#Lamar a principal
def home():
    return render_template('index.html', lista_tareas = lista_tareas)

#####
#####



# Metodo main del programa
if __name__ == '__main__':
     #debug = True, para reiniciar automatica el servidor
    app.run(debug=True)






