import pandas as pd
import matplotlib.pyplot as plt
## Axel Guzman NC 0070

# 1. Crear diccionario con datos de empleados
empleados = {
    'id_empleado': [101, 102, 103, 104, 105, 106],
    'nombre': ['Carlos', 'Maria', 'Jose', 'Ana', 'Luis', 'Sofia'],
    'edad': [25, 32, 28, 40, 35, 29],
    'departamento': ['Produccion', 'Calidad', 'Mantenimiento', 'Produccion', 'Calidad', 'Mantenimiento'],
    'puesto': ['Operador', 'Inspector', 'Tecnico', 'Supervisor', 'Inspector', 'Tecnico'],
    'salario': [12000, 15000, 13500, 22000, 16000, 14500],
    'antiguedad': [2, 6, 4, 12, 8, 3],
    'horas_trabajadas': [48, 40, 45, 40, 42, 48],
    'capacitaciones': [2, 5, 3, 8, 6, 4],
    'desempeno': [80, 95, 85, 98, 90, 88]
}

print("Analisis exploratorio de datos EDA")
print("Exploratory data nalysis por Axel Guzman NC 0070")
print("5. crear el diccionario con 10 listas y 6 elementos")
# 2 convertir diccionario en DataFARAME
df = pd.DataFrame(empleados)
print("Tabla original de empleados")
print(df)
# 3. Exportar los datos a CSV
df.to_csv(
    'empleados_industria.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")