import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from tkinter import Tk, Button, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Descargar y cargar el archivo
url = "https://github.com/zamu134/PARCIAL-2-PRACTICO/raw/main/Datos%20salarios.xlsx"
response = requests.get(url)
data = pd.read_excel(BytesIO(response.content))

# Limpiar nombres de columnas
data.columns = data.columns.str.replace(" ", "")

# Crear las figuras con los tres gráficos
figures = []

# Gráfico 1: Histograma
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.histplot(data['Salario'], binwidth=1000, color='blue', edgecolor='black', ax=ax1)
ax1.set_title("Histograma de Salarios")
ax1.set_xlabel("Salario")
ax1.set_ylabel("Frecuencia")
figures.append(fig1)

# Gráfico 2: Barras por facultad
promedio_salario = data.groupby('Facultad')['Salario'].mean().reset_index()
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.barplot(data=promedio_salario, x='Facultad', y='Salario', palette='viridis', ax=ax2)
ax2.set_title("Promedio de Salarios por Facultad")
ax2.set_xlabel("Facultad")
ax2.set_ylabel("Promedio de Salario")
ax2.tick_params(axis='x', rotation=45)
figures.append(fig2)

# Gráfico 3: Dispersión
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=data, x='edad', y='Salario', color='red', ax=ax3)
ax3.set_title("Edad vs Salario")
ax3.set_xlabel("Edad")
ax3.set_ylabel("Salario")
figures.append(fig3)

# Interfaz gráfica con botones
class GraphNavigator:
    def __init__(self, root, figures):
        self.root = root
        self.figures = figures
        self.index = 0

        self.frame = Frame(root)
        self.frame.pack()

        self.canvas = FigureCanvasTkAgg(self.figures[self.index], master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.btn_prev = Button(root, text="← Anterior", command=self.prev_graph)
        self.btn_prev.pack(side="left", padx=10, pady=10)

        self.btn_next = Button(root, text="Siguiente →", command=self.next_graph)
        self.btn_next.pack(side="right", padx=10, pady=10)

    def show_graph(self):
        self.canvas.get_tk_widget().pack_forget()
        self.canvas = FigureCanvasTkAgg(self.figures[self.index], master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def next_graph(self):
        self.index = (self.index + 1) % len(self.figures)
        self.show_graph()

    def prev_graph(self):
        self.index = (self.index - 1) % len(self.figures)
        self.show_graph()

# Lanzar la interfaz
root = Tk()
root.title("Visualizador de Gráficas")
app = GraphNavigator(root, figures)
root.mainloop()
