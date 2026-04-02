# Laboratorio 1 ICI4150-1: Controlador de un Robot Móvil Diferencial
Este repositorio contiene el desarrollo y los resultados del laboratorio 1 de Robótica y Sistemas Autónomos, enfocado en el control de un robot móvil diferencial (e-puck). 

El entorno de simulación se realizó en Webots, plataforma que permitió la codificación de un controlador en lenguaje Python para manipular las velocidades y el ruido de las ruedas izquierda y derecha del robot móvil.

El objetivo principal de este laboratorio fue aplicar los conceptos de robótica móvil y observar el comportamiento del modelo al realizar diferentes patrones de movimiento, permitiendo responder diferentes preguntar teóricas respecto al tema tratado.

## ¿Cómo ejecutar la simulación en Webots?
Para probar los controladores de forma local, siga los siguientes pasos:

1. **Clonar el repositorio** a su computadora.
2. Iniciar la plataforma de simulación **Webots**. Si no la tiene descargada, haga click en el link de la página oficial, descargue la aplicación y siga los pasos de instalación (https://cyberbotics.com/).
3. En la esquina superior izquierda, seleccione `File`>`Open World...` y seleccione la carpeta `worlds/` de la carpeta del repositorio, luego seleccione el archivo `.wbt` del laboratorio.
4. Asigne el controlador que desee (prueba inicial, con ruido o desafío) en el panel izquierdo (Scene Tree) al seleccionar el nodo principal del robot e-puck (en el campo `controller` puede asignar un controlador).
5. Para el controlador de desafío, abra el editor integrado de Webots para editar el código del controlador y modificar la variable `FIGURA` según la trayectoria que desee ver, como se indica en el comentario del controlador. **Recuerde guardar los cambios**.
6. Presione el botón de Play en la barra superior de Webots. Rebobine la simulación si desea empezar la simulación desde el principio.

## Resultados obtenidos
