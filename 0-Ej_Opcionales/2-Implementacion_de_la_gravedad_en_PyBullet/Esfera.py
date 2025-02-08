import pybullet as p
import pybullet_data
import time

#Variables iniciales
Y_inicial=3.0
V_Inicial=0
g=-9.81

t_Fragment=1./240.

r_esfera=0.2

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,0) #La ponemos a 0 para poder calcularla a mano


startOrientation = p.getQuaternionFromEuler([0, 0, 0])
startPosition = [0, 0, Y_inicial]

gravitySphereId = p.loadURDF("urdf/Esfera.urdf", startPosition, startOrientation)

for i in range(10000):

    t=t_Fragment*i
    Y=Y_inicial+V_Inicial*t+0.5*g*t**2

    if(Y <= r_esfera):
        Y=r_esfera

    p.resetBasePositionAndOrientation(gravitySphereId, [0, 0, Y], [0, 0, 0, 1])
    time.sleep(t_Fragment)

p.disconnect()