# 🐼 Exploración y Análisis de Datos con Pandas

> **Python · Pandas · Data Analysis · Business Intelligence · ETL**

Este repositorio contiene una colección de **ejercicios, prácticas y análisis de datos desarrollados con Python y Pandas**, realizados como parte de mi formación en **Inteligencia de Negocios**.

El objetivo principal es explorar el proceso de transformación de **datos crudos en información estructurada y analizable**, utilizando herramientas de programación para comprender de manera práctica los fundamentos detrás de las soluciones de Business Intelligence.

---

## 🧠 ¿Qué tiene que ver Pandas con la Inteligencia de Negocios?

En **Inteligencia de Negocios (BI)**, uno de los procesos fundamentales consiste en transformar grandes cantidades de datos en información que pueda utilizarse para **analizar situaciones, identificar patrones y apoyar la toma de decisiones**.

Pandas permite trabajar directamente con los datos mediante Python, facilitando tareas como:

* 🧹 Limpieza y depuración de datos
* 🔎 Filtrado y selección de información
* 🔄 Transformación y estructuración de datos
* 📊 Análisis estadístico
* ➕ Agregación y agrupación de información
* 🔗 Integración de diferentes conjuntos de datos
* 📈 Preparación de datos para visualizaciones y reportes

De esta manera, Pandas permite comprender desde el código la lógica que existe detrás de muchas herramientas utilizadas en Business Intelligence.

### 🔗 Flujo de trabajo

```text
📥 Datos
   ↓
🧹 Limpieza
   ↓
⚙️ Transformación
   ↓
🔎 Análisis
   ↓
📊 Visualización
   ↓
💡 Toma de decisiones
```

Trabajar directamente con **DataFrames y código Python** me permitió comprender con mayor profundidad cómo se preparan y procesan los datos antes de convertirse en dashboards, reportes e indicadores.

Esta experiencia también me ayudó a comprender mejor el funcionamiento de herramientas de análisis visual como **Power BI** y **Tableau**, al entender qué sucede con los datos antes de llegar a una visualización.

---

## 🔄 Pandas y el proceso ETL

La preparación y transformación de datos está estrechamente relacionada con el proceso **ETL (Extract, Transform, Load)**, uno de los conceptos fundamentales dentro de la Inteligencia de Negocios.

| Etapa            | Descripción                                            |
| ---------------- | ------------------------------------------------------ |
| 📥 **Extract**   | Obtener datos desde diferentes fuentes.                |
| ⚙️ **Transform** | Limpiar, organizar, modificar y estructurar los datos. |
| 📤 **Load**      | Cargar los datos preparados en su destino final.       |

### 🐼 ¿Dónde entra Pandas?

Pandas es especialmente útil durante la etapa de **Transform**, ya que proporciona herramientas para manipular y preparar los datos antes de utilizarlos en procesos de análisis, visualización o generación de reportes.

Por ejemplo:

```python
import pandas as pd

datos = pd.read_csv("datos.csv")

# Limpieza
datos = datos.dropna()

# Agrupación
resultado = datos.groupby("categoria")["ventas"].sum()

print(resultado)
```

Este tipo de operaciones permite pasar de información sin procesar a datos estructurados que posteriormente pueden utilizarse para generar **indicadores, gráficas y dashboards**.

---

## 🎯 Objetivo del repositorio

Este proyecto representa una parte de mi aprendizaje en **Python, análisis de datos e Inteligencia de Negocios**, aplicando conceptos de programación para comprender el ciclo de vida de los datos.

Más que realizar únicamente ejercicios de programación, el propósito es entender **cómo los datos pueden transformarse en información útil para el análisis y la toma de decisiones**.

---

## 🛠️ Tecnologías utilizadas

* 🐍 **Python**
* 🐼 **Pandas**
* 📊 **Análisis de datos**
* 🔄 **Procesos ETL**
* 💼 **Business Intelligence**

---

## 👩🏻‍💻 Autora

**Mónica Olvera**

Estudiante de **Ingeniería en Tecnologías de la Información y Comunicaciones**, interesada en el desarrollo de software, análisis de datos, Inteligencia de Negocios y soluciones tecnológicas orientadas a resultados.

---

⭐ *Este repositorio forma parte de mi proceso de aprendizaje y construcción de mi portafolio profesional.*
