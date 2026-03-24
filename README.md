
# 🧾 FAC-DATA – Automatización de Facturas con IA Generativa

FAC-DATA es una solución de automatización de procesos de negocio (BPA) que utiliza Inteligencia Artificial Generativa para transformar documentos no estructurados (facturas en PDF o imágenes) en información estructurada lista para análisis y toma de decisiones.

El sistema integra visión artificial, procesamiento de lenguaje natural, ingeniería de datos y visualización en un flujo automatizado end-to-end.

---
## 📸 Demo del sistema
<img width="1450" height="787" alt="Dashboard" src="https://github.com/user-attachments/assets/81f8d274-48b1-4da3-9a8c-c06ca26cf900" />
<img width="937" height="762" alt="facturas de ejemplo 3" src="https://github.com/user-attachments/assets/7d397e2f-f8c0-4b40-9bc1-8ab85274fdcb" />

## 🚨 Problema

El procesamiento manual de facturas presenta múltiples desafíos:

- Alto tiempo operativo en digitación manual
- Errores humanos en transcripción de datos
- Dificultad para procesar documentos escaneados o imágenes
- Consolidación compleja de monedas (USD, EUR → PEN)

---

## 💡 Solución

FAC-DATA automatiza todo el flujo de datos:

1. 📥 Captura de documentos (PDFs)
2. 👁️ Extracción con IA (visión + comprensión contextual)
3. 🔄 Transformación y limpieza de datos
4. 🗄️ Almacenamiento estructurado en base de datos
5. 📊 Visualización en dashboard interactivo

---

## 🧱 Arquitectura del sistema

### 1. 🧠 Inteligencia Artificial (Visión + NLP)
- Uso de IA para interpretar facturas
- Extracción de:
  - Fecha
  - Proveedor
  - Concepto
  - Importe
  - Moneda
- Procesamiento independiente del formato (layout-agnostic)

---

### 2. ⚙️ Backend en Python
- Orquestación del pipeline de datos
- Procesamiento automático de archivos
- Manejo de errores y validaciones
- Uso de variables de entorno (.env) para seguridad

---

### 3. 🔄 Data Engineering
- Conversión automática de monedas (USD / EUR → PEN)
- Estandarización de fechas (dd/mm/yyyy)
- Limpieza de texto (proveedores, conceptos)
- Preparación de datos para análisis

---

### 4. 🗄️ Base de Datos (SQLite)
- Persistencia de datos estructurados
- Historial de facturas procesadas
- Integración con herramientas BI

---

### 5. 📊 Visualización (Power BI)
- Dashboard interactivo de gastos
- KPIs:
  - Gasto total
  - Gasto promedio
  - Número de proveedores
- Análisis de gasto por proveedor
- Identificación visual de gastos críticos

---

## 🚀 Tecnologías utilizadas

- Python
- IA Generativa (Visión + NLP)
- SQLite
- Power BI
- Git & GitHub
- Procesamiento de PDFs

---

## 📈 Impacto

- ⏱️ Reducción del tiempo de procesamiento de horas a segundos
- ❌ Eliminación de errores manuales
- 📊 Visibilidad financiera en tiempo real
- 💰 Consolidación automática en moneda local (PEN)

---

## 🧪 Futuras mejoras

- ☁️ **Despliegue en la nube (AWS / Azure / GCP)**  
  Migración del sistema a una arquitectura cloud escalable, utilizando servicios como AWS Lambda, Azure Functions o Google Cloud Run para procesamiento automático.

- 🔌 **Desarrollo de API REST (FastAPI)**  
  Exposición del sistema como servicio mediante endpoints que permitan procesar facturas desde aplicaciones externas o integraciones empresariales.

- ⚡ **Automatización basada en eventos (Event-Driven)**  
  Implementación de triggers automáticos (ej: al subir un archivo a la nube) para ejecutar el pipeline sin intervención manual.

- 📊 **Pipeline de datos con arquitectura MLOps**  
  Versionado, monitoreo y mejora continua del modelo de extracción de datos para asegurar calidad y escalabilidad.

- 🧠 **Entrenamiento y fine-tuning de modelos personalizados**  
  Adaptación del modelo de IA para mejorar la precisión en facturas específicas del negocio o industria.

- 🔐 **Mejoras en seguridad y control de acceso**  
  Implementación de autenticación (JWT, OAuth) y manejo seguro de datos sensibles.

- 📈 **Dashboard en tiempo real (Streaming Analytics)**  
  Actualización automática de KPIs en Power BI o herramientas similares con datos en tiempo real.

- 📦 **Contenerización con Docker y orquestación con Kubernetes**  
  Preparación del sistema para entornos productivos con alta disponibilidad y escalabilidad.
---

## 👨‍💻 Autor

Jean Paul Changanaqui  
Ingeniero de Computación y Sistemas
