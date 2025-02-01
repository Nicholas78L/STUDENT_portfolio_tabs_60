import smtplib    # standard Python library which create an email client session
import ssl      # библиотека отвечающая за секретность пароля доступа к нашему почтовому ящику
import os       # библиотека дающая доступ к Операционной Системе нашего компа


def send_email(message):
    # Стандартные данные для входа в Gmail аккаунт через Python код:
    host = 'smtp.gmail.com'
    port = 465
    # Реквизиты для входа в нашу почту через Python код:
    username = 'cozyinua2021@gmail.com'  # Почта, с которой будет отправлено письмо.
    password = os.getenv("PASSWORD_cozy") # этот код получает доступ к операционной системе os нашего компьютера
    # и получает значение переменной окружающей среды PASSWORD, созданной исключительно для этого компьютера (ноутбука)
    receiver = 'nikolja191278@gmail.com'  # Почта получателя (куда будет отправлено письмо)
    #  Create a variable, which holds the secure context for sending emails securely:
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
