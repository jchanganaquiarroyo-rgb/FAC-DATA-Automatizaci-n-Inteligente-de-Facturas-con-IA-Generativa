import funciones
import pandas as pd
import os
from sqlalchemy import create_engine

# Configuración de base de datos
engine = create_engine("sqlite:///facturas.db")
df_acumulado = pd.DataFrame()

print("🚀 Iniciando Extracción con Visión Artificial (Formato: Soles)...")

ruta_facturas = "./facturas"
if not os.path.exists(ruta_facturas):
    os.makedirs(ruta_facturas)

archivos = [f for f in os.listdir(ruta_facturas) if f.lower().endswith(".pdf")]

for archivo in archivos:
    ruta = os.path.join(ruta_facturas, archivo)
    print(f"👁️  IA analizando visualmente: {archivo}...")
    
    try:
        csv_res = funciones.estructurar_texto(ruta)
        df_parcial = funciones.csv_a_dataframe(csv_res)
        
        if not df_parcial.empty:
            # Agregamos el nombre del archivo para trazabilidad
            df_parcial['archivo_origen'] = archivo
            df_acumulado = pd.concat([df_acumulado, df_parcial], ignore_index=True)
            print(f"✅ {archivo} procesado con éxito.")
    except Exception as e:
        print(f"❌ Error en {archivo}: {e}")

if not df_acumulado.empty:
    # Eliminamos la conversión a euros. Los datos se guardan en Soles (PEN).
    # Se usa 'replace' para limpiar la base de datos en cada ejecución.
    df_acumulado.to_sql("facturas", engine, if_exists="replace", index=False)
    print(f"\n✨ ¡PROCESO COMPLETADO! Datos guardados en facturas.db (Moneda Local)")
else:
    print("\n⚠️ No se procesaron datos. Revisa tus archivos PDF.")