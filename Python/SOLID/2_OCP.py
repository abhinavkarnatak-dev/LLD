# Without OCP

class Notification:
    def send(self, type):
        if type == "Email":
            print("Sending Email")

        elif type == "SMS":
            print("Sending SMS")

        elif type == "WhatsApp":
            print("Sending WhatsApp")


print("-------------------- Without OCP --------------------")

notification = Notification()

notification.send("Email")
notification.send("SMS")
notification.send("WhatsApp")


# With OCP

class Email:
    def send(self):
        print("Sending Email")


class SMS:
    def send(self):
        print("Sending SMS")


class WhatsApp:
    def send(self):
        print("Sending WhatsApp")


class Notification:
    def send(self, notification):
        notification.send()


print("-------------------- With OCP --------------------")

notification = Notification()

email = Email()
notification.send(email)

sms = SMS()
notification.send(sms)

whatsapp = WhatsApp()
notification.send(whatsapp)