import rospy
import time
from clever import srv
from std_srvs.srv import Trigger
from clever.srv import SetLEDEffect
import math
import decode_from_txt2points

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)  # define proxy to ROS-service


mas = decode_from_txt2points.decoderOK()


def navigate_wait(x, y, z, speed, frame_id, tolerance=0.3):
    navigate(x=x, y=y, z=z, speed=speed, frame_id=frame_id, yaw=float('nan'))
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
set_effect(r=0, g=0, b=0)
navigate(x=0, y=0, z=2.5, speed=1, frame_id='body', auto_arm=True)
time.sleep(5)
s = 0.5 #speed
set_effect(r = 255, g = 0, b = 255)
for i in range(len(mas)):
	navigate_wait(x=mas[i], y=mas[i], z=1.5, speed=s, frame_id='aruco_map')

set_effect(r=0, g=0, b=0)
res = land()
