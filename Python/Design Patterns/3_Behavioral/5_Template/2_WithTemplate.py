from abc import ABC, abstractmethod

class NotificationSender(ABC):
    def send(self, to, raw_message):
        self.rate_limit_check(to)
        self.validate_recipient(to)
        formatted = self.format_message(raw_message)
        self.pre_send_audit_log(to, formatted)
        composed_message = self.compose_message(formatted)
        self.send_message(to, composed_message)
        self.post_send_analytics(to)

    # Common step 1
    def rate_limit_check(self, to):
        print(f"Checking rate limits for: {to}")

    # Common step 2
    def validate_recipient(self, to):
        print(f"Validating recipient: {to}")

    # Common step 3
    def format_message(self, message):
        return message.strip()

    # Common step 4
    def pre_send_audit_log(self, to, message):
        print(f"Logging before send: '{message}' to {to}")

    # Hooks for subclasses 
    @abstractmethod
    def compose_message(self, message):
        pass
    
    @abstractmethod
    def send_message(self, to, message):
        pass
    
    # Common step 5 (overrideable)
    def post_send_analytics(self, to):
        print(f"Analytics updated for: {to}")

class EmailNotification(NotificationSender):
    def compose_message(self, message):
        return f"<html><body><p>{message}</p></body></html>"

    def send_message(self, to, message):
        print(f"Sending Email to: {to}\nContent: {message}")

class SMSNotification(NotificationSender):
    def compose_message(self, message):
        return f"[SMS] {message}"

    def send_message(self, to, message):
        print(f"Sending SMS to: {to}\nMessage: {message}")

    def post_send_analytics(self, to):
        print(f"Custom SMS analytics updated for: {to}")

email = EmailNotification()
email.send("abhinav@example.com", "Hello test message")
print("-"*40)
sms = SMSNotification()
sms.send("Abhinav", "Hello sms message")