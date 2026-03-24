import openai
import fitz  # PyMuPDF
import base64
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
from prompt import prompt

load_dotenv(".env")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def pdf_a_base64(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    pagina = doc[0] 
    pix = pagina.get_pixmap(matrix=fitz.Matrix(2, 2))
    imagen_bytes = pix.tobytes("png")
    doc.close()
    return base64.b64encode(imagen_bytes).decode('utf-8')

def estructurar_texto(ruta_pdf):
    base64_image = pdf_a_base64(ruta_pdf)
    
    respuesta = client.chat.completions.create(
        model="gpt-4o", # Usamos el modelo con visión
        messages=[
            {
                "role": "system",
                "content": "Eres un experto contable. Extrae los datos de la IMAGEN y devuelve SOLO el CSV con ';' como separador.",
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{base64_image}"}
                    },
                ],
            }
        ],
        max_tokens=500,
    )
    return respuesta.choices[0].message.content.strip()

def csv_a_dataframe(csv_texto):
    csv_limpio = csv_texto.replace("```csv", "").replace("```", "").strip()
    if csv_limpio.lower() == "error" or not csv_limpio:
        return pd.DataFrame()
    
    df_temp = pd.read_csv(StringIO(csv_limpio), delimiter=";", dtype=str)

    if "importe" in df_temp.columns:
        # Limpieza para asegurar que Power BI reciba números
        df_temp["importe"] = df_temp["importe"].str.replace(r'[^\d,.-]', '', regex=True)
        df_temp["importe"] = df_temp["importe"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False)
        df_temp["importe"] = pd.to_numeric(df_temp["importe"], errors="coerce")
    
    return df_temp