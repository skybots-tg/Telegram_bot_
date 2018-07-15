import telepot,time #Подключаем модули для управления ботом
from telepot.loop import MessageLoop #Подключаем класс управления автообновлений сообщений
from telepot.namedtuple import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

def handle(msg): #Создаем функцию, которая будет принимать сообщения от пользователей, и отвечать на них
    content_type, chat_type, chat_id = telepot.glance(msg) #Достаем из сообщений сами сообщения, тип чата и ай ди чата
    if (content_type == 'text'): #Если контент сообщения в формате текста
        command = msg['text'] 
        print ('Got command: %s' % command)
        if '/start' in command: #Если команда /start
            bot.sendMessage(chat_id, text="Приветствую тебя, новый пользователь!", #Бот отправляет такое сообщение пользователю
                                    reply_markup = ReplyKeyboardMarkup(
                                    keyboard = [
                                    
                                [KeyboardButton(text="Привет!"), KeyboardButton(text="Пока!")] #Это кнопки
                                    ]
            
            )) 
            
            
bot = telepot.Bot('Сюда_вставляем_Ваш_HTTP_API') #Привязываем нашего бота к программе
bot.message_loop(handle) #Делаем автообновление сообщений

while 1:
    time.sleep(10)
