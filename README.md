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
La primera prueba era lograr que el robot móvil pudiera realizar una serie de movimientos básicos sobre la plataforma, mediante las instrucciones de un controlador sobre sus ruedas izquierda y derecha. Los movimientos eran: 
- Movimiento recto ($v_r = v_l$)
- Movimiento curvo ($v_r \neq v_l$)
- Rotación en el lugar o sobre su propio eje ($v_r = -v_l$)

Estos movimientos se logran realizar en serie gracias a las instrucciones del `controlador_inicial`, donde el robot móvil inicia con una trayectoria recta durante 4 segundos (`v_l = 0.5 * MAX_SPEED` y `v_r = 0.5 * MAX_SPEED`, con `MAX_SPEED = 6.28` siendo la velocidad máxima del e-puck), luego hace un giro curvo durante otros 4 segundos (`v_l = 0.2 * MAX_SPEED` y `v_r = 0.8 * MAX_SPEED`, notar la diferencia de velocidades entre ruedas) y finalmente hace un giro sobre su propio eje (`v_l = -0.5 * MAX_SPEED` y `v_r =  0.5 * MAX_SPEED`). 

Se puede visualizar esta prueba inicial en el archivo `demo_inicial.mp4` de la carpeta `media`.

La segunda prueba es similar a la primera, pero ahora se introduce el factor del ruido.
