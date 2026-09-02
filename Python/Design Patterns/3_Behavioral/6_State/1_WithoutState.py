class Order:
    def __init__(self):
        self.state = "ORDER_PLACED"
    def cancel_order(self):
        if self.state == "ORDER_PLACED" or self.state == "ORDER_BEING_PREPARED":
            self.state = "CANCELED"
            print("Order has been canceled")
        else:
            print("Cannot cancel the order now")

    def next_state(self):
        match self.state:
            case "ORDER_PLACED":
                self.state = "ORDER_BEING_PREPARED"
            case "ORDER_BEING_PREPARED":
                self.state = "ORDER_ON_THE_WAY"
            case "ORDER_ON_THE_WAY":
                self.state = "ORDER_DELIVERED"
            case _:
                print(f"No next state from: {self.state}")
        return print(f"Order moved to: {self.state}")

    def get_state(self):
        return self.state

order = Order()
# Display initial state
print("Initial State:", order.get_state())
# Moving through states
order.next_state()  # ORDER_PLACED -> PREPARING
order.next_state()  # PREPARING -> OUT_FOR_DELIVERY
order.next_state()  # OUT_FOR_DELIVERY -> DELIVERED
# Attempting to cancel an order after it is out for delivery
order.cancel_order()  # Should not allow cancellation
# Display final state
print("Final State:", order.get_state())

order2 = Order()
# Display initial state
print("Initial State:", order2.get_state())
# Moving through states
order2.next_state()  # ORDER_PLACED -> PREPARING
# Attempting to cancel an order when it is being prepared
order2.cancel_order()  # Should allow cancellation
order2.next_state()  # PREPARING -> OUT_FOR_DELIVERY
# Display final state
print("Final State:", order2.get_state())