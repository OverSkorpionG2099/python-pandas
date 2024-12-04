#instalancion pandas : pip install pandas
#ejecutar código : python peru_poblacion.py

import pandas as pd

#datos :

#CIUDAD      HABITANTES

#Lima       10,292,408
#Cusco      1,205,527
#Arequipa   1,382,730
#Trujillo    970,016 
#Piura      2,138,443

data = {
    "Ciudad": ["Lima", "Cusco", "Arequipa", "Trujillo", "Piura"],
    "Habitantes": [10292408, 1205527, 1382730, 970016, 2138443]
}
df = pd.DataFrame(data)

print("Datos de Población de Ciudades en Perú:")
print(df)
print("\nTipos de datos:")
print(df.dtypes)
print("\nSerie de Ciudades:")
print(df["Ciudad"])
print("\nSerie de Habitantes:")
print(df["Habitantes"])