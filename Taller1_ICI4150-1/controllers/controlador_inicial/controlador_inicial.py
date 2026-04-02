from controller import Robot

# Inicializar el robot
robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28 # Velocidad máxima del e-puck

# Configurar los motores
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Modo de velocidad (rotación continua)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Bucle principal de la simulación
while robot.step(TIME_STEP) != -1:
    # Obtener el tiempo actual de la simulación (en segundos)
    current_time = robot.getTime()
    
    # Inicializar las velocidades objetivo
    v_l = 0.0
    v_r = 0.0
    
    # Lógica de movimientos
    if current_time < 4.0:
        # Movimiento recto (v_r = v_l), ambas ruedas giran a la misma velocidad hacia adelante
        v_l = 0.5 * MAX_SPEED
        v_r = 0.5 * MAX_SPEED
        
    elif current_time < 8.0:
        # Trayectoria curva (v_r != v_l), una rueda gira más rápido que la otra. Aquí gira hacia la izquierda.
        v_l = 0.2 * MAX_SPEED
        v_r = 0.8 * MAX_SPEED
        
    elif current_time < 12.0:
        # Rotación en el lugar (v_l = -v_r), velocidades opuestas de igual magnitud lo hacen girar sobre su propio centro.
        v_l = -0.5 * MAX_SPEED
        v_r =  0.5 * MAX_SPEED
        
    else:
        # El robot se detiene al finalizar la secuencia
        v_l = 0.0
        v_r = 0.0

    # Aplicar las velocidades a los motores 
    left_motor.setVelocity(v_l)
    right_motor.setVelocity(v_r)