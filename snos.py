import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import colorama 

senders = {
'newartlog1@mail.ru': '7nateskaasd',
}
receivers = ['newartlog@gmail.com']

banner = """
   
                                  ┏━━━┳━━━┳━┓┏━┳━━━━┓┏━━━┳┓╋┏┳━━━┳━━━┳━━━┳━━━┓
                                  ┃┏━┓┃┏━┓┃┃┗┛┃┃┏┓┏┓┃┃┏━┓┃┃╋┃┃┏━┓┃┏━┓┃┏━━┫┏━┓┃
                                  ┃┃╋┃┃┃╋┗┫┏┓┏┓┣┛┃┃┗┛┃┃╋┗┫┗━┛┃┃╋┃┃┃╋┗┫┗━━┫┗━┛┃
                                  ┃┃╋┃┃┃╋┏┫┃┃┃┃┃╋┃┃╋╋┃┃╋┏┫┏━┓┃┃╋┃┃┃╋┏┫┏━━┫┏━━┛
                                  ┃┗━┛┃┗━┛┃┃┃┃┃┃╋┃┃╋╋┃┗━┛┃┃╋┃┃┗━┛┃┗━┛┃┗━━┫┃
                                  ┗━━━┻━━━┻┛┗┛┗┛╋┗┛╋╋┗━━━┻┛╋┗┻━━━┻━━━┻━━━┻┛
слил ебаный гений @BlockSimCards

                               [1] Снос аккаунта  [2] Снос канала  [3] Снос сессии                                               
                                      
"""

colorama.init()

def logo():
    print(colorama.Fore.GREEN + banner)
    print(colorama.Fore.RESET)

def menu():


    return input("Выбирай номер: ")
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
    if choice in ["4", "5", "6"]:
        print("в процессе")
        time.sleep(6)
        return
    
    print("1. CHOC.")
    comp_choice = input("выбирай: ")
    if comp_choice in ["1", "2"]:
        print("повторяй за мной")
        username = input("юзер: ")
        id = input("айди: ")
        chat_link = input("ссылку на чат (если сносите акк ставьте -) : ")
        violation_link = input("ссылку на нарушение (сделайте скрин, зайдите в имгур и сделайте из скрина ссылку и вставьте сюда) : ")
        print("жди")
        comp_texts = {
            "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
            "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
            "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
        }
        for sender_email, sender_password in senders.items():
            for receiver in receivers:
                comp_text = comp_texts[comp_choice]
                comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                            violation_link=violation_link.strip())
                send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                print(f"Отправлено на {receiver} от {sender_email}!")
                sent_emails += 14888
                time.sleep(5)
    elif comp_choice == "4":
        print("повторяй за мной")
        username = input("юзернейм: ")
        id = input("айди: ")
        print("жди")
        comp_texts = {
            "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
        }
        for sender_email, sender_password in senders.items():
            for receiver in receivers:
                comp_text = comp_texts[comp_choice]
                comp_body = comp_text.format(username=username.strip(), id=id.strip())
                send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                print(f"Отправлено на {receiver} от {sender_email}!")
                sent_emails += 1488
                time.sleep(5)
        for sender_email, sender_password in senders.items():
            for receiver in receivers:
                comp_text = comp_texts[comp_choice]
                comp_body = comp_text.format(username=username.strip(), id=id.strip())
                send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                print(f"Отправлено на {receiver} от {sender_email}!")
                sent_emails += 10000
                time.sleep(5)
    elif choice == "2":
        print("1. с личными данными")
        print("2. с живодерством (как катекс) ")
        print("3. с цп")
        print("4. для каналов типа прайсов.")
        ch_choice = input("выбор: ")
        
        if ch_choice in ["1", "2", "3"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("жди")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)
        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("жди")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)


if __name__ == "__main__":
    main()