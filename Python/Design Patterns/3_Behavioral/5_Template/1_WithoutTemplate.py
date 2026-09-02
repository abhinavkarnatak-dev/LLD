class EmailNotification:
    def send(self, to, message):
        print(f"Checking rate limits for: {to}")
        print(f"Validating email recipient: {to}")
        formatted = message.strip()
        print(f"Logging before send: '{formatted}' to {to}")

        # Compose Email
        composed_message = f"<html><body><p>{formatted}</p></body></html>"

        # Send Email
        print(f"Sending Email to: {to}\nContent: {composed_message}")

        # Analytics
        print(f"Analytics updated for: {to}")

class SMSNotification:
    def send(self, to, message):
        print(f"Checking rate limits for: {to}")
        print(f"Validating email recipient: {to}")
        formatted = message.strip()
        print(f"Logging before send: '{formatted}' to {to}")

        # Compose Email
        composed_message = f"[SMS] {formatted}"

        # Send Email
        print(f"Sending SMS to: {to}\nMessage: {composed_message}")

        # Analytics (Custom)
        print(f"Custom SMS analytics updated for: {to}")

email = EmailNotification()
email.send("abhinav@example.com", "Hello test message")
print("-"*40)
sms = SMSNotification()
sms.send("Abhinav", "Hello sms message")