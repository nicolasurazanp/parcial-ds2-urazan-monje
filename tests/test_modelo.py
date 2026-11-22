import os
import sys

# para importar el modelo sin errores
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from CampanaPruebas import CampanaPruebas

def test_goel_cero():
    campana = CampanaPruebas([28, 23, 22, 17, 16, 12, 12, 9])
    assert campana.goel(0, 190, 0.16) == 0



def test_acumulados_y_restantes():
    datos_mongo_simulados = [
        {"semana":1 , "defectosFind": 28},
        {"semana":2 , "defectosFind": 23},
        {"semana":3 , "defectosFind": 22},
        {"semana":4 , "defectosFind": 17},
        {"semana":5 , "defectosFind": 16},
        {"semana":6 , "defectosFind": 12},
        {"semana":7 , "defectosFind": 12},
        {"semana":8 , "defectosFind": 9},
    ]
    campana = CampanaPruebas(datos_mongo_simulados)
    campana.ajustar()

    assert campana.acumulados[-1] == 139
    assert campana.restantes() > 0

if __name__ == "__main__":
    test_goel_cero()
    test_acumulados_y_restantes()
    print("pruebas salieron bien")




