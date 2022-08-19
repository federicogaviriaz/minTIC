
import pandas as pd
# ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'


def listaPeliculas(rutaFileCsv: str) -> str:
    dfPelis = pd.read_csv(rutaFileCsv)
    dfPelis.to_csv('archivo.csv')
    if rutaFileCsv.endswith('.csv?raw=true'):
        try:
            dfPelis = pd.read_csv(rutaFileCsv)
            loQuePideEstaGente = dfPelis[[
                'Country', 'Language', 'Gross Earnings']]
            loQuePideEstaGente2 = loQuePideEstaGente.pivot_table(loQuePideEstaGente,
                                                                 index=['Country', 'Language'])
            return (loQuePideEstaGente2.head(10))

        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")


print(listaPeliculas(rutaFileCsv))
