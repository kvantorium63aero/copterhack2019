# -*- coding: utf-8 -*-
# НА КОМПЕ

import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from urllib.request import urlopen


def main():
    rospy.init_node('bot')
    bridge = CvBridge()
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
                #vector_base.codi()
                image = cv2.imread('img.png', 0)
                image_pub = rospy.Publisher('/image_from_bot', Image)
                image_pub.publish(bridge.cv2_to_imgmsg(image, 'bgr8'))
                vk.messages.send(
                    peer_id=int(event.object.from_id),
                    random_id=get_random_id(),
                    message='Взлёт?'
                )
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == "да":
            takeoff_pub = rospy.Publisher('/takeoff_flag', Bool)
            takeoff_pub.publish(True)
            vk.messages.send(
                peer_id=int(event.object.from_id),
                random_id=get_random_id(),
                message='Полетели рисовать!'
            )


if __name__ == '__main__':
    main()
