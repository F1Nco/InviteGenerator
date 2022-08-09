#приветствие
from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.CYAN )

print('Вас приветствует бот по созданию пригласительных билетов/визиток.\nЯ смогу подобрать для вас любую пригласительную\nречь по вашим предпочтения.')
print('От вас требуется всего ничего, нужно заполнить 7 вопросов\nкасательно заполнения визитки.')
decision = input('Приступаем? (начать/выход)\n')

print( Back.GREEN )

#решение
#True = decision = 'начать' 
#True = decision = 'выход'

if decision == 'начать':
    print()
    shehe = input('Кому адресовано приглашение (ей/ему)?\n')
elif decision == 'выход':
    print('Если вновь понадобятся мои услуги, приходите!\n')
    exit()
else:
    i = 'начать'
    ii = 'выход'
    while decision not in [i, ii]:
        print( Back.RED )
        print()
        print('Выбранно неправильное действие,\nвыберите (начать/выход).')
        print( Back.GREEN )
        decision = input('Приступаем? (начать/выход)\n')
        if decision == i or decision == ii:
            shehe = input('Кому адресовано приглашение (ей/ему)?\n')
#настройки
if decision == 'начать':
    if shehe == 'ей':
        print()
        name = input('Её имя? (в им. п.)\n')
    elif shehe == 'ему':
        print()
        name = input('Его имя? (в им. п.)\n')
    else:
        print( Back.RED )
        print()
        print('Выбранно неправильное действие,\nвыберите (ей/ему).')
        print( Back.GREEN )
    if decision == 'начать':     
        print()	
        appeal = input('Как мне обращаться? (на ты/на вы).\n')
    if decision == 'начать':
        print()
        measure = input('Какое мероприятие?\n')
    if decision == 'начать':
       print()
       place = input('Адрес встречи?\n')
    if decision == 'начать':
        print()        
        time = input('Время встречи?\n')
    if decision == 'начать':
        print( Back.YELLOW )
        print()
        print('Отлично, последний шаг')
        nomber = input('Контактный номер?\n')

    print( Back.RED )

    print()
    print('Если в программе возникла ошибка, то скорее всего')
    print('вы не корректно ввели данные, попробуйте ещё раз.')
    print('Учтите, что вписывать данные нужно строго как показано в вопросе.')
    print()
    print()
    
    if appeal == 'на вы':
        age = 'запомните'
    if appeal == 'на ты':
        age = 'запомнишь'    
    if appeal == 'на вы':
        age2 = 'вас'
    if appeal == 'на ты': 
    	age2 = 'тебя'
    if appeal == 'на вы': 
        age3 = 'вы'
    if appeal == 'на ты': 
        age3 = 'ты'
    if shehe == 'ей':
        pol = 'Дорогая'
    if shehe == 'ему':
    	pol = 'Дорогой'

    print( Back.MAGENTA )
#письмо
    print('           Приглашение')
    print(pol + ' ' + name + ', приглашаю ' + age2 + ' на')
    print(measure + '! Этот день ' + age3 + ' точно')
    print( age + ' на долго, в хорошем смысле;)')
    print('будет много развлекательных программ и')
    print('прочего, от ' + age2 + ' требуется только')
    print('хорошего настроения. С нетерпением жду')
    print(age2 + '.')
    print()
    print('Место встречи ' + place)
    print('Время встречи ' + time)
    print('Номер связи ' + nomber)
    print()
    print( Back.YELLOW )
    print()
    print('Спасибо за пользование! В дальнейшем мы будем выпускать\nобновления, в которых будем добавлять новые\nфункции и исправление ошибок в сиситеие;)')
    input()




    


