import smtplib    # standard Python library which create an email client session
import ssl

# Стандартные данные для входа в Gmail аккаунт через Python код:
host = 'smtp.gmail.com'
port = 465
# Реквизиты для входа в нашу почту через Python код:
username = 'cozyinua2021@gmail.com'             # Почта, с которой будет отправлено письмо.
password = "uygkfdjxavevngkm"
receiver = 'nikolja191278@gmail.com'            # Почта получателя (куда будет отправлено письмо)
#  Create a variable, which holds the secure context for sending emails securely:
context = ssl.create_default_context()

# \ -> обратная косая - обязательный атрибут для сепарации ТЕМЫ письма (после обратной косой НЕ должно быть пробелов):
message = """\
Subject: Another letter.
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
