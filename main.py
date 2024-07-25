from typing import Union
from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"NO TE OLVIDES DE AGREGAR /docs"}


@app.get("/{Mes}")

def cantidad_filmaciones_mes( Mes ):

    #Importamos el csv final
    movies_credits_final = pd.read_csv('dataset_final.csv')

    #Nos aseguramos que la columna "release_date" este en formato datetime
    movies_credits_final['release_date'] = pd.to_datetime(movies_credits_final['release_date'])

    #Convertimos el nombre del mes en español a número
    meses = {
        'enero': 1,
        'febrero': 2,
        'marzo': 3,
        'abril': 4,
        'mayo': 5,
        'junio': 6,
        'julio': 7,
        'agosto': 8,
        'septiembre': 9,
        'octubre': 10,
        'noviembre': 11,
        'diciembre': 12
    }
    mes_a_numero = meses.get(Mes.lower())
    
    #Si no se ha ingresado un mes valido en español retornaremos el mensaje de advertencia
    if mes_a_numero not in [1,2,3,4,5,6,7,8,9,10,11,12] :
        return f"El mes '{Mes}' no es válido. Por favor ingresa un mes en español."
    
    #Si se ha ingresado un mes valido en español retornaremos la cantidad de filmaciones aplicando el siguiente filtro
    cantidad_pelis = movies_credits_final[movies_credits_final['release_date'].dt.month == mes_a_numero].shape[0]
    
    return f"En {Mes} fueron estrenadas {cantidad_pelis} películas."