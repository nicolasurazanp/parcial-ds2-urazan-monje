import os
import numpy as np 
import matplotl.pyplot as plt 
from scipy.optimize import curve_fit 



class CampanaPruebas: 
    def _init__(self, defectos ):
        lista = []
        for item in defectos:
            if isinstance(item, dict):
                lista.append(item["defectosFind"])
            else:
                lista.append(item)

        
        self.defectos = lista 
        self.acumulados = np.cumsum(lista)
        self.t = np.arange(1, len(lista) + 1)
        self.a = None
        self.b = None

    def goel(self, t, a, b):
        return a * (1- np.exp(-b * t))

    def ajustar(self):
        p0= [max(self.acumulados), 0.1]
        params, _ = curve_fit(self.goel, self.t, self.acumulados, p0=p0)
        self.a = params[0]
        self.b= params[1]

    def restantes(self):
        t_actual = self.t[-1]
        return self.a - self.goel(t_actual,self.a, self.b)

    def semana_95(self):
        return np.log(20) / self.b


    def graficar(self, ruta="graficas/resultados.png"):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        t_curva = np.linspace(0, max(self.t) + 2, 100)
        y_curva = self.goel(t_curva, self.a, self.b)

        plt.figure(figsize=(8, 5))
        plt.scatter(self.t, self.acumulados, colors="red", label="acumulados reales")
        plt.plot(t_curva, y_curva, color="blue", label="Curva Goel")
        plt.title("Evolucion del software")
        plt.xlabel("semana")
        plt.ylabel("Defectos acumulados")
        plt.legend()
        plt.grid(True)
        plt.savefig(ruta)
        plt.close()

        

    


        
