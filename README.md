# extension-de-phishing
## Descripción (English Description Below)
Este proyecto consiste en una extensión de navegador de phishing hecha con mi grupo para nuestro trabajo final de Ingeniería de la Información. Funciona utilizando un API desarrollado con Flask a la vez con la extensión para navegador que requiere los archivos hello.html,manifest.json y background.js.

El API que corre en Flask solía estar alojado en una página web pero ya no funciona. Todavía es posible correrlo con la extensión cambiando las referencias de la URL al LocalHost.

El modelo ha sido entrenado con miles de páginas de phishing y legítimas, y funciona ponderando los resultados de 3 modelos: Redes Neuronales Convolucionales, XG-BOOST y Random Forest. Utilizando los datos de prueba de URLs de páginas a nivel global obtuvimos un F1-Score (A favor de páginas de Phishing) de 90.17%, mas un F1-Score de 56.47% probando el modelo en páginas web de Perú. Es por ello que su uso tras despliegue pueda dar lugar a varios falsos negativos o positivos.

![image](https://github.com/antoplh/extension-de-phishing/assets/81722618/1abc10c3-08c0-45a9-b0b9-834b19243d7a)

## English Description
This project consists of a phishing browser extension made with my group for our final Information Engineering project. It works using an API developed with Flask together with the browser extension that requires the hello.html, manifest.json and background.js files.

The API that runs in Flask used to be hosted on a web page but it no longer works. It is still possible to run it with the extension by changing the URL references to LocalHost.

The model has been trained with thousands of phishing and legitimate pages, and works by weighting the results of 3 models: Convolutional Neural Networks, XG-BOOST and Random Forest. Using test data from global page URLs we obtained an F1-Score (In Favor of Phishing Pages) of 90.17%, but an F1-Score of 56.47% testing the model on websites from Peru. This is why its use after deployment can give rise to several false negatives or positives.

