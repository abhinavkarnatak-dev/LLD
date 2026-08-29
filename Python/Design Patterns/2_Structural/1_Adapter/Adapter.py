from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, orderId, amount):
        pass

class PayUGateway(PaymentGateway):
    def pay(self, orderId, amount):
       print(f"Paid Rs.{amount} using PayU for order: {orderId}") 

class RazorpayAPI:
    def make_payment(self, invoice_id, amount_in_rupees):
        print(f"Paid Rs.{amount_in_rupees} using Razorpay for invoice: {invoice_id}")

# Adapter
class RazorpayAdapter(PaymentGateway):
    def __init__(self):
        self.razorpay_api = RazorpayAPI()

    def pay(self, order_id, amount):
        self.razorpay_api.make_payment(order_id, amount)

class CheckoutService():
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def checkout(self, orderId, amount):
        self.payment_gateway.pay(orderId, amount)

checkout_service = CheckoutService(PayUGateway())
checkout_service.checkout("12", 178)

checkout_service1 = CheckoutService(RazorpayAdapter())
checkout_service1.checkout("10", 200)