# -*- coding: utf-8 -*-
# НА КОМПЕ

import rospy
import cv2
import math
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from urllib.request import urlopen
import time
import decode_from_txt2points
import flight

def main():
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
