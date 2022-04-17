# Proyecyo_ML

Clasificación de imágenes - Bootcamp The Bridge

**Introducción:**

Este proyecto dará respuesta a un problema de clasificación basado en el aprendizaje supervisado. Las imágenes contienen una etiqueta que indica su malignidad, si la imagen contiene un lunar benigno se le asigna el 0 y si, por el contrario, el lunar es maligno, se le asigna el 1.

Para este proyecto se utilizará un Dataset obtenido de Kaggle: [Skin cancer Malignant vs. Benign](https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign?resource=download). El Dataset contiene un conjunto de datos equilibrados con imágenes de lunares cutáneos benignos y malignos. Todas las imágenes tienen las mismas dimensiones (224 x 224).

**Contenido:**
- ***Train***: Benignos (1440 registros) y Malignos (1197 registros).
- ***Test***: Benignos (360 registros) y Malignos (300 registros).

**Objetivo:**

Este proyecto pretende clasificar imágenes de lunares cutáneos para identificar los lunares malignos.

**Procesamiento de imágenes:**
1. Eliminación del vello.
2. Segemntación del lunar.
3. Normalización de las imágenes.

**Nota**
> Los datasets procesados de imágenes pesan demasiado para subirlos.
