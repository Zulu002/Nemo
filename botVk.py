# Импортируем библиотеку vk_api
import vk_api
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType
import config

# Создаём переменную для удобства в которой хранится наш токен от группы

token = config.token
# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


def chMsg(id, text):
    bh.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:

            # Для того чтобы бот читал все с маленьких букв
            message = event.text.lower()
            # Получаем id пользователя
            id = event.user_id

            # Доисторическая логика общения на ифах
            # Перед вами структура сообщений на которые бот сможет ответить, elif можно создавать сколько угодно, if и else же могут быть только 1 в данной ситуации.
            # if - если, else - иначе(значит бот получил сообщение на которое не вызвана наша функция для ответа)

            if message == 'привет':
                blasthack(id, 'Привет, я бот!')

            elif message == 'как дела?':
                blasthack(id, 'Хорошо, а твои как?')

            else:
                blasthack(id, 'Я вас не понимаю! :(')

# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:
            if event.from_chat:

                msg = event.text.lower()
                id = event.chat_id

                if msg == 'привет':
                    chMsg('ewfwf')