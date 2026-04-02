from controller import Robot

# Inicializar el robot
robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# --- Configuración ---
# Cambiar esta variable a "RECTA", "CURVA", "CIRCULO", "OCHO" o "CUADRADO", para ver el movimiento del robot
FIGURA = "CIRCULO" 

# Variables de control de estado para el "Cuadrado"
estado_cuadrado = 0
ultimo_cambio_tiempo = 0.0

# Bucle principal
while robot.step(TIME_STEP) != -1:
    tiempo_actual = robot.getTime()
    v_l = 0.0
    v_r = 0.0
    
    # ----------------------------------------------------
    if FIGURA == "RECTA":
        v_l = MAX_SPEED * 0.5
        v_r = MAX_SPEED * 0.5
        
    # ----------------------------------------------------
    elif FIGURA == "CIRCULO":
        v_l = MAX_SPEED * 0.3
        v_r = MAX_SPEED * 0.8  
    # ----------------------------------------------------
    elif FIGURA == "CURVA":
        # Se dibuja una curva suave durante los primeros 4 segundos
        if tiempo_actual < 4.0:
            v_l = MAX_SPEED * 0.4
            v_r = MAX_SPEED * 0.6  
        # Después de 4 segundos, endereza el rumbo y va en línea recta
        else:
            v_l = MAX_SPEED * 0.5
            v_r = MAX_SPEED * 0.5   
    # ----------------------------------------------------
    elif FIGURA == "OCHO":
        # Se usa el operador módulo (%) para alternar cada 6 segundos
        if (tiempo_actual % 12.0) < 6.0:
            v_l = MAX_SPEED * 0.8
            v_r = MAX_SPEED * 0.3  # Medio círculo a la derecha
        else:
            v_l = MAX_SPEED * 0.3
            v_r = MAX_SPEED * 0.8  # Medio círculo a la izquierda
            
    # ----------------------------------------------------
    elif FIGURA == "CUADRADO":
        tiempo_transcurrido = tiempo_actual - ultimo_cambio_tiempo
        
        # Si el estado es un número par, avanza en línea recta
        if estado_cuadrado % 2 == 0:
            v_l = MAX_SPEED * 0.5
            v_r = MAX_SPEED * 0.5
            
            # Después de 2 segundos, cambia de estado (comienza a girar)
            if tiempo_transcurrido > 2.0:
                estado_cuadrado += 1
                ultimo_cambio_tiempo = tiempo_actual
                
        # Si el estado es un número impar, gira en el lugar
        else:
            v_l = -MAX_SPEED * 0.2
            v_r =  MAX_SPEED * 0.2
            
            if tiempo_transcurrido > 1.25:
                estado_cuadrado += 1
                ultimo_cambio_tiempo = tiempo_actual

    # Aplicar velocidades
    left_motor.setVelocity(v_l)
    right_motor.setVelocity(v_r)