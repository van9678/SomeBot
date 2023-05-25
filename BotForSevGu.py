import telebot
from telebot import types 

bot = telebot.TeleBot('5757198842:AAEsCCUhpLuFtTmI1lbA-cJni5J1UYfEqE4')

@bot.message_handler(commands=['start'])

def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Общие вопросы')
    item2 = types.KeyboardButton('Отдельно институты')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, Этот бот создан как помощник для старост. Вы можете задать мне вопросы, которые вас интересуют. Сделать это можно с помощью кнопок в меню!)".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)    

@bot.message_handler(content_types = ['text'])
def some(message): 
    if message.chat.type == 'private': 
        if message.text == 'Общие вопросы': 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1.Материальная помощь')
            item2 = types.KeyboardButton('2.Нормативные акты и документы')
            item3 = types.KeyboardButton('3.Мудл')
            item4 = types.KeyboardButton('4.Перезачеты и индивидуальный график')
            item5 = types.KeyboardButton('5.Справки')
            item6 = types.KeyboardButton('6.Общее')
            item7 = types.KeyboardButton('7.Сессия и прогулы')
            item8 = types.KeyboardButton('8.Стипендия')
            back = types.KeyboardButton('◀️ Назад')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

            bot.send_message(message.chat.id, 'Выберете категорию, которая вас интересует', reply_markup=markup)

        elif message.text == '1.Материальная помощь':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1.1')
                item2 = types.KeyboardButton('1.2')
                item3 = types.KeyboardButton('1.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, '1.1 Какие нужно документы подавать на материальную помощь и в какие сроки?\n1.2 Как я могу подать документы на материальную помощь по п.4.5.12 за съем жилья?\n1.3 В какие сроки приходит материальная помощь?', reply_markup=markup)
        
        elif message.text == '1.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1.1')
                item2 = types.KeyboardButton('1.2')
                item3 = types.KeyboardButton('1.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Согласно положению о стипендиальном обеспечении и материальной поддержки есть более 18 пунктов, по которым у студентов есть возможность подать документы. Основной перечень: заявление, свидетельство о рождении, справка о составе семьи, копия справки о доходах за последний год (полгода). Вы можете получить консультацию у заместителя директора по воспитательной работе. Выплата осуществляется 2 раза в календарный год. Документы принимаются до 5го числа каждого месяца.', reply_markup=markup)
            
        elif message.text == '1.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1.1')
                item2 = types.KeyboardButton('1.2')
                item3 = types.KeyboardButton('1.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Если вы относитесь к категории граждан, которые согласно Положению о студенческом общежитии, подлежат поселению в первоочередном порядке, но не были поселены по причине не предоставления места, то вам следует обратиться  с этим вопросом к заместителю директора по воспитательной работе.', reply_markup=markup)
        
        elif message.text == '1.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1.1')
                item2 = types.KeyboardButton('1.2')
                item3 = types.KeyboardButton('1.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Четких сроков, регламентирующих начисление материальной помощи, нет. Обычно это происходит в 10-15 числах месяца, после заседания соответствующей Комиссии, выхода приказа и перечисления денежных средств банком. ', reply_markup=markup)    
                
        elif message.text == '◀️ Вернутся к общим вопросам':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1.Материальная помощь')
                item2 = types.KeyboardButton('2.Нормативные акты и документы')
                item3 = types.KeyboardButton('3.Мудл')
                item4 = types.KeyboardButton('4.Перезачеты и индивидуальный график')
                item5 = types.KeyboardButton('5.Справки')
                item6 = types.KeyboardButton('6.Общее')
                item7 = types.KeyboardButton('7.Сессия и прогулы')
                item8 = types.KeyboardButton('8.Стипендия')
                back = types.KeyboardButton('◀️ Назад')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, back)

                bot.send_message(message.chat.id, 'Выберете категорию, которая вас интересует', reply_markup=markup)
        
        elif message.text == '◀️ Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('Общие вопросы')
                item2 = types.KeyboardButton('Отдельно институты')
                markup.add(item1, item2)

                bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот создан для помощи с вопросами, которые вас интересуют. Что вы хотите узнать?".format(message.from_user, bot.get_me()),
                    parse_mode='html', reply_markup=markup)   

        elif message.text == '2.Нормативные акты и документы':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, '2.1 Как мне вставить на воинский учет?\n2.2 Где я могу найти все положения и нормативные акты СевГУ.\n2.3 Где мне найти расписание?\n2.4 Как мне перевесить в другой вуз? В другой Институт?\n2.5 Как мне перевыбрать дисциплину Пула? Случайно ошибся/передумал.\n2.6 Я студент ЗФО, как оформить справку вызов на сессию?\n2.7 В каких случаях положен академический отпуск?\n2.8 Я потерял пропуск, что делать?2.9 Я не получил пропуск, что мне делать?\n2.10 Как мне писать объяснительную записку?\n2.11 Мне нужно место для поселения в студенческом общежитии?', reply_markup=markup)
        
        elif message.text == '2.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'Обучающиеся, состоящие на воинском учете в военных комиссариатах г.Севастополя и Республики Крым, могут осуществить постановку на воинский учет Университета дистанционно через сайт Университета, в разделе «Обучающимся», кнопка «Постановка на воинский учет» или перейдя по ссылке https://www.sevsu.ru/uni/vu/. В форму для постановки на воинский учет вносится информация об обучающемся: состав семьи (отец, мать, жена, дети – фамилия, имя, отчество, год рождения), адрес фактического проживания обучающегося в г. Севастополе, контактный телефон, электронную почту для получения ответа, а также загружаются все заполненные страницы воинского документа. Обучающийся, направив воинские документы дистанционно, должен убедиться в получении ответа о принятии документов с электронной почты voenuchet@sevsu.ru. Обучающиеся, прибывшие с других субъектов РФ, на воинский учет становятся только лично в Мобилизационном отделе.', reply_markup=markup)
            
        elif message.text == '2.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'На сайте университета в самом конце страницы «сведения об образовательной организации», далее раздел документы, локальные нормативные акты. Внимание страница достаточно долго погружается.', reply_markup=markup)
        
        elif message.text == '2.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'На сайте университета, вкладка обучающимся, расписание – находим свой институт и курс, далее группу, внимание расписание проверяем каждый день.', reply_markup=markup)    
        
        elif message.text == '2.4':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'Обращаемся в единый деканат: В другой вуз, заказываем академическую справку (можно на сайте Университета) и направляем ее самостоятельно в другой вуз, получаем справку - ответ подтверждающую перевод, предоставляем справку в единый деканат и пишем заявление на отчисление в связи с переводом. В другой Институт: в единый деканат обращаемся за заверенной учебной карточкой и копией зачетки и идем в Дирекцию другого Института писать заявление на перевод при наличии бюджетных мест ( если есть желание учится на бюджете).', reply_markup=markup)
            
        elif message.text == '2.5':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'Никак, согласно Положению, выбор делается один раз в установленные сроки и перевыбрать дисциплину нельзя. Будьте внимательнее.', reply_markup=markup)
        
        elif message.text == '2.6':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)
                    
                bot.send_message(message.chat.id, 'Обратиться в единый деканат, Г-506а, почта: e_dekanat@sevsu.ru тел.435-150', reply_markup=markup)    
        
        elif message.text == '2.7':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'В соответствии с Положением в связи: со службой армии, рождением ребенка и уходом за ребенком в возрасте до 3х лет, болезни и наличии заключения ВКК. Заявление писать в едином деканате.', reply_markup=markup)
        
        elif message.text == '2.8':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'Писать объяснительную записку, согласовать ее с зам.директора по воспитательной работе, оплатить восстановление пропуска и обратиться в каб. В109, следовать дальнейшим инструкциям.', reply_markup=markup)    
        
        elif message.text == '2.9':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'Обращаться в дирекцию Института к заместителю директора по воспитательной работе.', reply_markup=markup)
            
        elif message.text == '2.10':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)
                    
                bot.send_message(message.chat.id, 'Объяснительная записка пишется на имя директора Института в свободной форме, образец можно взять в Дирекции Института или у заместителя директора по воспитательной работе.', reply_markup=markup)
        
        elif message.text == '2.11':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('2.1')
                item2 = types.KeyboardButton('2.2')
                item3 = types.KeyboardButton('2.3')
                item4 = types.KeyboardButton('2.4')
                item5 = types.KeyboardButton('2.5')
                item6 = types.KeyboardButton('2.6')
                item7 = types.KeyboardButton('2.7')
                item8 = types.KeyboardButton('2.8')
                item9 = types.KeyboardButton('2.9')
                item10 = types.KeyboardButton('2.10')
                item11 = types.KeyboardButton('2.11')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, popit1)

                bot.send_message(message.chat.id, 'ОСледует обратиться к заместителю директора по воспитательной работе для написания заявления на имя ректора.', reply_markup=markup)    
        
        elif message.text == '3.Мудл':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('3.1')
                item2 = types.KeyboardButton('3.2')
                item3 = types.KeyboardButton('3.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, '3.1 Где мне взять пароль от мудл? Я восстановился/перевелся из другого вуза.\n3.2 Я не могу зайти в мудл, что мне делать?\n3.3 В мудл отображаются не мои курсы/нет моих курсов, что делать?', reply_markup=markup)
        
        elif message.text == '3.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('3.1')
                item2 = types.KeyboardButton('3.2')
                item3 = types.KeyboardButton('3.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Вам следует обратиться в Дирекцию своего института для направления соответствующего запроса в ДИС.', reply_markup=markup)
            
        elif message.text == '3.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('3.1')
                item2 = types.KeyboardButton('3.2')
                item3 = types.KeyboardButton('3.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Писать в тех. поддержку: moodle_support@sevsu.ru', reply_markup=markup)
        
        elif message.text == '3.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('3.1')
                item2 = types.KeyboardButton('3.2')
                item3 = types.KeyboardButton('3.3')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, popit1)

                bot.send_message(message.chat.id, 'Писать в тех. поддержку: kis_moodle@sevsu.ru', reply_markup=markup)    
        
        elif message.text == '4.Перезачеты и индивидуальный график':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('4.1')
                item2 = types.KeyboardButton('4.2')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, popit1)

                bot.send_message(message.chat.id, '4.1 Как я могу оформить перезачёты?\n4.2 Как оформить индивидуальный график?', reply_markup=markup)
        
        elif message.text == '4.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('4.1')
                item2 = types.KeyboardButton('4.2')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, popit1)

                bot.send_message(message.chat.id, 'Для оформления перезачетов вам необходимо обратиться в единый деканат в Г506а с копией документа, который является основанием до 15 октября за осенний семестр, до 15 марта за весенний семестр. Далее Ваше заявление будет передано на рассмотрении комиссии Института. Заявление принимается только на семестр.', reply_markup=markup)
        
        elif message.text == '4.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('4.1')
                item2 = types.KeyboardButton('4.2')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, popit1)

                bot.send_message(message.chat.id, 'В соответствии с Положением у Вас должны быть основания для перехода на индивидуальный график (работаете по специальности, заболевание итд). Заявление, с приложением подтверждающих документов  Вы пишите в едином деканате, далее  заявление передается в Дирекцию Института на рассмотрение.', reply_markup=markup)    

        elif message.text == '5.Справки':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('5.1')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, popit1)

                bot.send_message(message.chat.id, '5.1 Как заказать справку о том, что я студент?', reply_markup=markup)
        
        elif message.text == '5.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('5.1')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, popit1)

                bot.send_message(message.chat.id, 'Справку подтверждающую факт обучения вы можете заказать лично в «Едином окне» в В105 или на сайте Университета: « https://www.sevsu.ru/uni/dap/obuchenie/ » Забирать лично в Едином окне.', reply_markup=markup)
        
        elif message.text == '6.Общее':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, '6.1 Как мне найти преподавателя не своей кафедры?\n6.2 Как можно найти своего куратора? В какой группе я учусь?\n6.3 Что такое аттестация? И зачем она нужна?\n6.4 Я иностранный гражданин, что мне нужно обязательно знать?\n6.5 А мне обязательно проходить эти анкетирования в СевГУ?\n6.6 Где я могу найти последние новости обо всех мероприятиях в СевГУ?\n6.7 Где находится единый деканат?', reply_markup=markup)

        elif message.text == '6.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Пользуемся сайтом, первая задача: выяснить преподаватель с какой кафедры (обычно это вычисляется по предмету), потом ищем соответствующий Институт на сайте Университета в разделе образование, смотрим где находится кафедра/деканат и обращаемся по месту.', reply_markup=markup)
            
        elif message.text == '6.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Вам следует обратиться в Дирекцию Института к заместителю директора по воспитательной работе.', reply_markup=markup)
        
        elif message.text == '6.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Вас будут оценивать насколько вы выполняете учебный план: сколько сдали лабораторных, рефератов, эссе и тд. И может дадут контрольную или тест написать, чтобы посмотреть усвоение теоретического материала. Все сложат и получат процент освоения учебной программы. Чтобы сразу выявить возможных проблемных студентов на сессии. Полезно для студентов и преподавателей.', reply_markup=markup)    
        
        elif message.text == '6.4':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'По законам РФ у вас должна быть пройдена дактилоскопическая регистрация и оформлен полиса ДМС (с репатриацией). Обращаться в дирекцию международного сотрудничества (В305)/заместителю директора по воспитательной работе.', reply_markup=markup)
            
        elif message.text == '6.5':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Да, обязательно.  Они делают твою жизнь лучше. Особенно анкетирование, которое проводит студ. совет Института и Минообрнауки.', reply_markup=markup)
        
        elif message.text == '6.6':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Подпишись на группу студ.офиса в контакте: https://vk.com/studofsevsu', reply_markup=markup)    
        
        elif message.text == '6.7':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('6.1')
                item2 = types.KeyboardButton('6.2')
                item3 = types.KeyboardButton('6.3')
                item4 = types.KeyboardButton('6.4')
                item5 = types.KeyboardButton('6.5')
                item6 = types.KeyboardButton('6.6')
                item7 = types.KeyboardButton('6.7')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, item5, item6, item7, popit1)

                bot.send_message(message.chat.id, 'Г-506а ( Университетская, 33), почта: e_dekanat@sevsu.ru тел.435-150', reply_markup=markup)

        elif message.text == '7.Сессия и прогулы':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('7.1')
                item2 = types.KeyboardButton('7.2')
                item3 = types.KeyboardButton('7.3')
                item4 = types.KeyboardButton('7.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, '7.1 Что мне делать, если мне надо уехать? И я пропускаю пары?\n7.2 Я пропустил пары по болезни, куда мне нести справку?\n7.3 Я не сдал сессию, когда отчисляют, как это все происходит?\n7.4 Когда сессия? Как пользоваться графиком учебного процесса?', reply_markup=markup)
               
        elif message.text == '7.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('7.1')
                item2 = types.KeyboardButton('7.2')
                item3 = types.KeyboardButton('7.3')
                item4 = types.KeyboardButton('7.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Вам необходимо поставить в известность Дирекцию института (деканат), написав соответствующее заявление на имя директора Института, с приложением подтверждающих документов.', reply_markup=markup)
            
        elif message.text == '7.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('7.1')
                item2 = types.KeyboardButton('7.2')
                item3 = types.KeyboardButton('7.3')
                item4 = types.KeyboardButton('7.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Вам необходимо показать справку на физкультуру своему ведущему преподавателю, показать старосте группы для отметке в журнале, копию справки сдать в единый деканат (через старосту группы/ лично).', reply_markup=markup)
        
        elif message.text == '7.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('7.1')
                item2 = types.KeyboardButton('7.2')
                item3 = types.KeyboardButton('7.3')
                item4 = types.KeyboardButton('7.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'После сессии Вам дается еще две попытки: ведущему преподавателю и комиссии согласно расписанию ликвидации. Сроки после летней сессии устанавливает ректор приказом: обычно до 1 ноября, после зимней сессии директор Института распоряжением, для выпускных курсов до 1 марта, для младших курсов до 1 апреля. Если студент не закроет свои долги по сессии к этому времени студента отчисляют.', reply_markup=markup)    
        
        elif message.text == '7.4':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('7.1')
                item2 = types.KeyboardButton('7.2')
                item3 = types.KeyboardButton('7.3')
                item4 = types.KeyboardButton('7.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'График учебного процесса размещен на информационном стенде Института, находим свою группу в нужном столбце и смотрим соответствующею условное обозначение/ примечание, верхней части графика указаны месяца/дни/недели на этот учебный год.', reply_markup=markup)
               
        elif message.text == '8.Стипендия':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('8.1')
                item2 = types.KeyboardButton('8.2')
                item3 = types.KeyboardButton('8.3')
                item4 = types.KeyboardButton('8.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, '8.1 Когда  и какие документы я должен подавать на повышенную стипендию?\n8.2 Я снова получаю стипендию, мне для того чтобы получить выплату нужно что-то делать?\n8.3 Как мне оформить социальную стипендию? Где писать заявление?\n8.4 У меня изменились реквизиты банковской карты для начисления стипендии, что мне делать?', reply_markup=markup)
               
        elif message.text == '8.1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('8.1')
                item2 = types.KeyboardButton('8.2')
                item3 = types.KeyboardButton('8.3')
                item4 = types.KeyboardButton('8.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Документы на повышенную стипендию принимаются сразу после зимней сессии до 10 февраля, летней сессии до 10 августа. Комплект подтверждающих документов вы приносите заместителю директора по воспитательной работе для написания заявления: заверенная копия зачетной книжки, ходатайство тренера/научного руководителя, копии грамот/сертификатов итд. Подробнее вы можете ознакомиться в Положении о стипендиальном обеспечении и мат. поддержке.', reply_markup=markup)
            
        elif message.text == '8.2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('8.1')
                item2 = types.KeyboardButton('8.2')
                item3 = types.KeyboardButton('8.3')
                item4 = types.KeyboardButton('8.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Нет, если вы ранее писали заявление на перечисление денежных средств в Г-306 и ничего не поменялось, то весь процесс будет происходить автоматически без вашего участия.', reply_markup=markup)
        
        elif message.text == '8.3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('8.1')
                item2 = types.KeyboardButton('8.2')
                item3 = types.KeyboardButton('8.3')
                item4 = types.KeyboardButton('8.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Вам следует обратиться в дирекцию своего Института.', reply_markup=markup)    
        
        elif message.text == '8.4':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('8.1')
                item2 = types.KeyboardButton('8.2')
                item3 = types.KeyboardButton('8.3')
                item4 = types.KeyboardButton('8.4')
                popit1 = types.KeyboardButton('◀️ Вернутся к общим вопросам')

                markup.add(item1, item2, item3, item4, popit1)

                bot.send_message(message.chat.id, 'Идти в кабинет Г-306 на Университетской, 33 писать соответствующие заявление.', reply_markup=markup)

        elif message.text == 'Отдельно институты':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1. ИИТ')
                item2 = types.KeyboardButton('2. ПИ')
                item3 = types.KeyboardButton('3. МИ')
                item4 = types.KeyboardButton('4. ИФЭУ')
                item5 = types.KeyboardButton('5. ГПИ')
                item6 = types.KeyboardButton('6. ИЯЭиП')
                item7 = types.KeyboardButton('7. ЮИ')
                item8 = types.KeyboardButton('8. ИРИТС')
                item9 = types.KeyboardButton('9. ИОНМО')
                item10 = types.KeyboardButton('10. ИРГ')
                item11 = types.KeyboardButton('11. ИПИ')
                item12 = types.KeyboardButton('12. ИДПО')
                item13 = types.KeyboardButton('13. МК')
                item14 = types.KeyboardButton('14. Лицей')
                popit1 = types.KeyboardButton('◀️ Назад')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, popit1)

                bot.send_message(message.chat.id, '1. Институт информационных технологий\n2. Политехнический институт\n3. Морской институт\n4. Институт финансов, экономики и управления\n5. Гуманитарно-педагогический институт\n6. Институт ядерной энергии и промышленности\n7. Юридический институт\n8. Институт радиоэлектроники и управления в технических системах\n9. Институт общественных наук и международных отношений\n10. Институт развития города\n11. Институт перспективных исследований\n12. Институт дополнительного профессионального образования\n13. Морской колледж\n14. Лицей-предуниверсарий', reply_markup=markup)

        elif message.text == '1. ИИТ':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, '1. Где в Институте ИТ находится кабинет для самостоятельной работе для студентов?\n2. Где я могу получить кампусную карту?\n3. Могу ли я оформить досрочную сдачу сессии?\n4. Мне исполнилось 20 лет, куда мне нужно отнести копию паспорта в связи с его заменой?\n5. У меня возникла конфликтная ситуация с преподавателем, что мне делать?\n6. Хочешь вступить в рабочую группу IT-котиков?\n7. Ты инициативный и хочешь заниматься грандиозными IT проектами?\n8. В каком корпусе мы будем учиться?\n9. Я расстроил Лолиту Михайловну, что теперь будет?', reply_markup=markup)
        
        elif message.text == '1':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Кабинет для практических занятий и самостоятельной работы находится в каб.   В-515, ключи находятся в Г-509, т. + 7978 727 69 00.', reply_markup=markup)

        elif message.text == '2':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Можно получить в офисе банка Россия по адресу, Ленина,15, часы работы пн-пт 09:00 до 19:00, сб 09:00 до 15:00.', reply_markup=markup)

        elif message.text == '3':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Индивидуальные сроки сдачи промежуточной аттестации –возможны, для этого Вам нужно обратиться с единый деканат в Г506а, написать заявление и приложить документы основания, не позднее чем за месяц до начала сессии.', reply_markup=markup)

        elif message.text == '4':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Копию паспорта Вам следует отнести в единый деканат в Г506а и студенческий отдел кадров в Б210.', reply_markup=markup)

        elif message.text == '5':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Вы можете обратиться с этим вопросом в дирекцию Института ИТ.', reply_markup=markup)

        elif message.text == '6':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Обращайся к заместителю директора по воспитательной работе @zlolen.', reply_markup=markup)

        elif message.text == '7':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Тогда тебе к Дымченко Ирине Вячеславовне: https://vk.com/ivdymchenko.', reply_markup=markup)

        elif message.text == '8':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'По расписанию, но обычно 09 группа учится на Университетской, 33, 10-ка в корпусе на Курчатова,7.', reply_markup=markup)
            
        elif message.text == '9':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1')
                item2 = types.KeyboardButton('2')
                item3 = types.KeyboardButton('3')
                item4 = types.KeyboardButton('4')
                item5 = types.KeyboardButton('5')
                item6 = types.KeyboardButton('6')
                item7 = types.KeyboardButton('7')
                item8 = types.KeyboardButton('8')
                item9 = types.KeyboardButton('9')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, popit1)

                bot.send_message(message.chat.id, 'Лолиту Михайловну лучше не расстраивать :)', reply_markup=markup)
                    
        elif message.text == '2. ПИ':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)
         
        elif message.text == '3. МИ':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, '1) В каких числах приходит стипендия?\n2) Где узнать расписание занятий?\n3) Где узнать расписание сессии?\n4) В каких числах приходит материальная помощь?\n5) Куда обратиться для получения материальной помощи?', reply_markup=markup)
           
        elif message.text == '1)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Стипендия приходит до 2 числа следующего месяца.', reply_markup=markup)

        elif message.text == '2)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'https://www.sevsu.ru/univers/shedule/.', reply_markup=markup)

        elif message.text == '3)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'https://www.sevsu.ru/univers/shedule/.', reply_markup=markup)

        elif message.text == '4)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Материальная помощь может прийти в любой день.', reply_markup=markup)

        elif message.text == '5)':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1)')
                item2 = types.KeyboardButton('2)')
                item3 = types.KeyboardButton('3)')
                item4 = types.KeyboardButton('4)')
                item5 = types.KeyboardButton('5)')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Ул. Гоголя,23, кабинет 39.', reply_markup=markup)

        elif message.text == '4. ИФЭУ':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)
        
        elif message.text == '5. ГПИ':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, '1-> Где можно подать на материальную помощь студентам ГПИ?\n2-> Где можно найти заместителя директора по воспитательной работе ГПИ?\n3-> Я хочу участвовать ...?\n4-> Как получить повышенную стипендию?\n5-> Как поселиться в общежитие? Как получить социальную стипендию?', reply_markup=markup)
       
        elif message.text == '1->':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Гоголя 14 кабинет 218 а.', reply_markup=markup)
        
        elif message.text == '2->':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Гоголя, 14 каб. 103 или Университетская, 33 каб. В-306.', reply_markup=markup)
        
        elif message.text == '3->':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Обращайся к председателю совета обучающихся ГПИ Алине Таран https://vk.com/im?sel=282824097.', reply_markup=markup)

        elif message.text == '4->':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Обращайся к председателю совета обучающихся ГПИ Алине Таран https://vk.com/im?sel=282824097.', reply_markup=markup)

        elif message.text == '5->':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1->')
                item2 = types.KeyboardButton('2->')
                item3 = types.KeyboardButton('3->')
                item4 = types.KeyboardButton('4->')
                item5 = types.KeyboardButton('5->')
                popit1 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                markup.add(item1, item2, item3, item4, item5, popit1)

                bot.send_message(message.chat.id, 'Обращайся к замдиректора по воспитательной работе ГПИ Долгополовой Лилии Валерьевне https://vk.com/dream_001.', reply_markup=markup)

        elif message.text == '6. ИЯЭиП':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '7. ЮИ':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)
        
        elif message.text == '8. ИРИТС':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '9. ИОНМО':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '10. ИРГ':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '11. ИПИ':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '12. ИДПО':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному институту :(', reply_markup=markup)

        elif message.text == '13. МК':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному колледжу :(', reply_markup=markup)

        elif message.text == '14. Лицей':  
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    popit2 = types.KeyboardButton('◀️ Вернутся к списку институтов')

                    markup.add(popit2)

                    bot.send_message(message.chat.id, 'К сожалению, нам не предоставили список вопросов по данному лицею :(', reply_markup=markup)

        elif message.text == '◀️ Вернутся к списку институтов':  
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton('1. ИИТ')
                item2 = types.KeyboardButton('2. ПИ')
                item3 = types.KeyboardButton('3. МИ')
                item4 = types.KeyboardButton('4. ИФЭУ')
                item5 = types.KeyboardButton('5. ГПИ')
                item6 = types.KeyboardButton('6. ИЯЭиП')
                item7 = types.KeyboardButton('7. ЮИ')
                item8 = types.KeyboardButton('8. ИРИТС')
                item9 = types.KeyboardButton('9. ИОНМО')
                item10 = types.KeyboardButton('10. ИРГ')
                item11 = types.KeyboardButton('11. ИПИ')
                item12 = types.KeyboardButton('12. ИДПО')
                item13 = types.KeyboardButton('13. МК')
                item14 = types.KeyboardButton('14. Лицей')
                popit1 = types.KeyboardButton('◀️ Назад')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, popit1)

                bot.send_message(message.chat.id, '1. Институт информационных технологий\n2. Политехнический институт\n3. Морской институт\n4. Институт финансов, экономики и управления\n5. Гуманитарно-педагогический институт\n6. Институт ядерной энергии и промышленности\n7. Юридический институт\n8. Институт радиоэлектроники и управления в технических системах\n9. Институт общественных наук и международных отношений\n10. Институт развития города\n11. Институт перспективных исследований\n12. Институт дополнительного профессионального образования\n13. Морской колледж\n14. Лицей-предуниверсарий', reply_markup=markup)
                
bot.polling(none_stop=True)