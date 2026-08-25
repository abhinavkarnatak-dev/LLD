from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class RazorpayGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Razorpay: Rs. {amount}")

class PayUGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"PayU: Rs. {amount}")

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Stripe: ${amount}")

class PaypalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"PayPal: ${amount}")

class Invoice(ABC):
    @abstractmethod
    def generate_invoice(self):
        pass

class GstInvoice(Invoice):
    def generate_invoice(self):
        print("GST Invoice")

class GlobalInvoice(Invoice):
    def generate_invoice(self):
        print("Global Invoice")

class PaymentFactory(ABC):

    @abstractmethod
    def create_gateway(self):
        pass

    @abstractmethod
    def create_invoice(self):
        pass

class RazorpayFactory(PaymentFactory):
    def create_gateway(self):
        return RazorpayGateway()

    def create_invoice(self):
        return GstInvoice()

class PayUFactory(PaymentFactory):
    def create_gateway(self):
        return PayUGateway()

    def create_invoice(self):
        return GstInvoice()

class StripeFactory(PaymentFactory):
    def create_gateway(self):
        return StripeGateway()

    def create_invoice(self):
        return GlobalInvoice()

class PaypalFactory(PaymentFactory):
    def create_gateway(self):
        return PaypalGateway()

    def create_invoice(self):
        return GlobalInvoice()

class CheckoutService:
    def __init__(self, factory: PaymentFactory, amount):
        self.factory = factory
        self.amount = amount

    def checkout(self):
        gateway = self.factory.create_gateway()
        invoice = self.factory.create_invoice()
        gateway.process_payment(self.amount)
        invoice.generate_invoice()

payment = input("Enter the desired service: ")
payment = payment.lower()
amount = input("Enter the amount: ")
if payment == "razorpay": CheckoutService(RazorpayFactory(), amount).checkout()
elif payment == "payu": CheckoutService(PayUFactory(), amount).checkout()
elif payment == "paypal": CheckoutService(PaypalFactory(), amount).checkout()
elif payment == "stripe": CheckoutService(StripeFactory(), amount).checkout()
else: print("Invalid payment service")