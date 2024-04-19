import pandas as pd

def analisis_estadistico(l):
    try:

        if type(l) != list:
            raise TypeError("El parametro recibido no es una lista")

        if len(l) == 0:
            raise ValueError("La lista está vacia")
        
        for element in l:
            if type(element) != int:
                raise TypeError("La lista contiene elementos no numericos")

        l.sort()

        fi = {}
        for i in l:
            if i in fi:
                fi[i] += 1
            else:
                fi[i] = 1

        df = pd.DataFrame({'edades':fi.keys(),'fi':fi.values()})

        df["Fi"] = df["fi"].cumsum()
        df["ri"] = df["fi"] / df["fi"].sum()
        df["Ri"] = df["ri"].cumsum()
        df["pi%"] = df["ri"] * 100
        df["Pi%"] = df["Ri"] * 100

        return df
    except ValueError as e:
        print(e)
        return None
    except TypeError as e:
        print(e)
        return None

edades = [19, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

print(analisis_estadistico(edades))