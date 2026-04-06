# Laboratorio 1 ICI4150-1: Controlador de un Robot Móvil Diferencial

# Resumen introductorio
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

>Se puede visualizar esta prueba inicial en el archivo `demo_inicial.mp4` en la carpeta `media`.

La segunda prueba es similar a la primera, pero ahora se introduce el factor del ruido. El ruido sistématico, o sesgo, se introduce para simular las variaciones impredecibles, como errores en los sensores, desgaste del sistema o **condiciones del entorno**. 

El controlador `controlador_ruido` es similar a `controlador_inicial`, pero omitiendo el movimiento del giro sobre el eje final y añadiendo la variable `NOISE = 0.5`, que se puede ajustar según convenga (entre más alto el valor, mayor será la perturbación en el robot). 

La perturbación del ruido se aplica a las ruedas izquierda y derecha en las líneas de código `v_l_ruidosa = v_l_ideal + random.gauss(0, NOISE)` y `v_r_ruidosa = v_r_ideal + random.gauss(0, NOISE)`, provocando que el robot móvil pareciera "temblar" mientras realiza el trayecto, incluso cuando se mantiene quieto. Esto, comparándolo con la prueba inicial, provoca que la trayectoria del robot sea menos directa pero más realista, desviándose de lo que podría ser una trayectoria ideal teórica, pero es lo que necesitamos si deseamos implementar un robot así en la vida real.

>Se puede visualizar esta prueba con ruido en el archivo `demo_ruido.mp4` en la carpeta `media`.

La última prueba tuvo como objetivo manipular las velocidades de las ruedas del robot para replicar distintas figuras, como un círculo e incluso un cuadrado. 

Para ello, en el `controlador_desafío` se puede modificar la variable `FIGURA` para visualizar los diferentes movimientos que puede realizar el robot con este controlador (como una recta, curva, círculo, ocho o cuadrado). El caso más complejo correspondería al cuadrado, el cual requiere de ciertas variables (`tiempo_transcurrido`, `estado_cuadrado` y `ultimo_cambio_tiempo`) para realizar la figura:
- Si el estado es un número par, avanza en línea recta por 2.5 segundos, después cambia de estado.
- Si el estado es un número impar, gira aproximadamente 90 grados sobre su propio eje y vuelve a cambiar de estado.

Esto provoca un ciclo entre estados que permite trazar la figura del cuadrado.

>Se puede visualizar esta prueba del cuadrado en el archivo `demo_cuadrado.mp4` o las otras figuras en la carpeta `media`.

## Preguntas de análisis
- ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
  
R: Cuando la velocidad de la rueda izquierda es la misma que la rueda derecha (o viceversa) y ambas giran en el mismo sentido, esto provoca que el robot experimente un movimiento de traslación en línea recta, es decir, se moverá hacia adelante o hacia atrás, dependiendo del signo de las velocidades.

- ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?

R: Cuando las velocidades de la rueda izquierda y derecha son diferentes, el movimiento del robot se realiza en una trayectoria curva. Siempre girará en dirección hacia la rueda más lenta y mientras mayor sea la diferencia de velocidades entre ruedas, más cerrado será el giro.

- ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?

R: Cuando las ruedas giran en sentido opuesto a la otra y con la misma magnitud se produce una rotación en el lugar, con centro en el punto medio del eje que une ambas ruedas, alterando la orientación del robot sin moverlo de su lugar.

- ¿Qué tipo de movimiento permite dibujar un círculo?

R: Para poder dibujar un círculo, ambas ruedas deben girar en el mismo sentido pero con velocidades constantes y diferentes entre sí. La trayectoria del robot será curva, y que dado cierto periodo de tiempo formará un círculo de 360 grados (el radio del círculo dependerá de la magnitud de la diferencia entre velocidades de las ruedas).

## Conclusión
En este repositorio se incluye todo lo necesario para probar un robot móvil diferencial en un entorno simulado (Webots), y en este documento se evidenció el análisis y explicación de las pruebas básicas realizadas sobre este robot en relación a trayectoria, movimiento y condiciones del entorno (ruido), adjuntando material visual (vídeos) que apoyan la explicación dada.
