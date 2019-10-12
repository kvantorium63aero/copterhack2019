# -*- coding: utf-8 -*-

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from urllib.request import urlopen
import speech_recognition

def main():
    vk_session = vk_api.VkApi(
        token='TOKEN')
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk_session, '187507235')

    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Рисуй', color=VkKeyboardColor.DEFAULT)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.object.attachments:
            if event.type == VkBotEventType.MESSAGE_NEW and event.object.attachments[0].get('type') == 'graffiti':
                print('image event', event)
                img = event.object.attachments[0].get('graffiti').get('url')
                print('2', img)
                resource = urlopen(img)
                out = open("img.png", 'wb')
                out.write(resource.read())
                out.close()
                print('loaded image to png')
                vk.messages.send(
                    peer_id=int(event.object.from_id),
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Жми "Рисуй"'
                )
            elif event.type == VkBotEventType.MESSAGE_NEW and event.object.attachments[0].get('type') == 'audio_message':
                print('audio event: ', event)
                audio_message = event.object.attachments[0].get('audio_message').get('link_ogg')
                resource = urlopen(audio_message)
                audiofile = "/home/ddombrovskii/copterhack/audio/audio.ogg"
                out = open(audiofile, 'wb')
                out.write(resource.read())
                out.close()
                vk.messages.send(
                    peer_id=int(event.object.from_id),
                    random_id=get_random_id(),
                    message=speech_recognition.speech(audiofile)
                )
                print('wrote audio')
        elif event.type == VkBotEventType.MESSAGE_NEW and event.object.text.lower() == 'рисуй':
            print('other event: ', event)
            image_new = vector3.vector()
            for i in range(len(image_new)):
                for j in range(len(image_new[i])):
                    print(image_new[i][j], end=' ')
                print('\n')
        elif event.type == VkBotEventType.MESSAGE_NEW:
            print('user {}'.format(event.object.from_id), 'smth wrote', event.object.text)
            print(event)


if __name__ == '__main__':
    main()
