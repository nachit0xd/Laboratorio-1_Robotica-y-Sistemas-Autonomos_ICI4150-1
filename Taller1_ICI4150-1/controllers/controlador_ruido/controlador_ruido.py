import random
from controller import Robot

# Inicializar el robot
robot = Robot()
TIME_STEP = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28 

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Ajustar el nivel de ruido
# Entre más alto el valor, mayor será la perturbación 
NOISE = 0.5

while robot.step(TIME_STEP) != -1:
    current_time = robot.getTime()
    
    if current_time < 4.0:
        v_l_ideal = 0.5 * MAX_SPEED
        v_r_ideal = 0.5 * MAX_SPEED
    elif current_time < 8.0:
        v_l_ideal = 0.2 * MAX_SPEED
        v_r_ideal = 0.8 * MAX_SPEED
    else:
        v_l_ideal = 0.0
        v_r_ideal = 0.0

    # Simular la perturbación en los actuadores con la función raandom.gauss(media, desviaci[on estándar)
    v_l_ruidosa = v_l_ideal + random.gauss(0, NOISE)
    v_r_ruidosa = v_r_ideal + random.gauss(0, NOISE)

    # Nos aseguramos de no exceder los límites físicos del motor
    v_l_ruidosa = max(min(v_l_ruidosa, MAX_SPEED), -MAX_SPEED)
    v_r_ruidosa = max(min(v_r_ruidosa, MAX_SPEED), -MAX_SPEED)

    # Aplicamos las velocidades con ruido o perturbadas
    left_motor.setVelocity(v_l_ruidosa)
    right_motor.setVelocity(v_r_ruidosa)