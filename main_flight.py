# -*- coding: utf-8 -*-
# НА КОМПЕ

import rospy
import cv2
import math
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from urllib.request import urlopen
import time
from clever import srv
from std_srvs.srv import Trigger
from clever.srv import SetLEDEffect
import decode_from_txt2points
import flight
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


def main():
    rospy.init_node('bot')
    vk_session = vk_api.VkApi(token='TOKEN')
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, '187507235')

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == "начать":
            vk.messages.send(
                peer_id=int(event.object.from_id),
                random_id=get_random_id(),
                message='Привет! Давай рисовать!'
            )
        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.attachments:
            if event.object.attachments[0].get('type') == 'graffiti':
                image_url = event.object.attachments[0].get('graffiti').get('url')
                resource = urlopen(image_url)
                out = open('img.png', 'wb')
                out.write(resource.read())
                out.close()
                vk.messages.send(
                    peer_id=int(event.object.from_id),
                    random_id=get_random_id(),
                    message='Взлёт?'
                )
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == "да":
            vk.messages.send(
                peer_id=int(event.object.from_id),
                random_id=get_random_id(),
                message='Полетели рисовать!'
                flight.polet()
            )


if __name__ == '__main__':
    main()
