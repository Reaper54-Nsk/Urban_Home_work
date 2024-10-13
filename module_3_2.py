
def send_mail(message, recipient, sender = 'university.help@gmail.com.'):
    if ('@' and ('.com' or '.ru' or '.net')) not in (recipient and sender) or  ('@' or ('.com' or '.ru' or '.net')) not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса, {sender}, на адрес, {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com.':
        print('Письмо успешно отправлено с адреса', sender, ' на адрес', recipient)
    elif sender != 'university.help@gmail.com.':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Писмьмо отправлено с адреса ', sender, 'на адрес', recipient)

send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'teacher@gmail.com', 'teacher@gmail.com')