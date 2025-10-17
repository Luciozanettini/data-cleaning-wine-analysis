import pandas as pd

# Leer archivo Excel
df = pd.read_excel('../data/wines.xlsx')

# Ver las primeras filas
print("📊 Primeras filas del dataset:")
print(df.head())

# 1. Eliminar filas duplicadas
df.drop_duplicates(inplace=True)

# 2. Eliminar columnas completamente vacías
df.dropna(axis=1, how='all', inplace=True)

# 3. Mostrar valores nulos por columna
print("\n🕳️ Cantidad de valores nulos por columna:")
print(df.isnull().sum())

# 4. Guardar dataset limpio
df.to_csv('../data/wines_cleaned.csv', index=False)
print("\n✅ Archivo limpio guardado como wines_cleaned.csv")
