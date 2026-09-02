# Order context class manages the current state of the order
class OrderContext:
    def __init__(self):
        self.current_state = OrderPlacedState() # Default state

    def set_state(self, state):
        self.current_state = state

    def next(self):
        self.current_state.next(self)

    def cancel(self):
        self.current_state.cancel(self)

    def get_current_state(self):
        return self.current_state.get_state_name()

class OrderState:
    def next(self, context):
        pass

    def cancel(self, context):
        pass

    def get_state_name(self):
        pass


# Concrete states for each stage of the order

# OrderPlacedState handles the behavior when the order is placed
class OrderPlacedState(OrderState):
    def next(self, context):
        context.set_state(PreparingState())
        print("Order is now being prepared.")

    def cancel(self, context):
        context.set_state(CancelledState())
        print("Order has been cancelled.")

    def get_state_name(self):
        return "ORDER_PLACED"


# PreparingState handles the behavior when the order is being prepared
class PreparingState(OrderState):
    def next(self, context):
        context.set_state(OutForDeliveryState())
        print("Order is out for delivery.")

    def cancel(self, context):
        context.set_state(CancelledState())
        print("Order has been cancelled.")

    def get_state_name(self):
        return "PREPARING"


# OutForDeliveryState handles the behavior when the order is out for delivery
class OutForDeliveryState(OrderState):
    def next(self, context):
        context.set_state(DeliveredState())
        print("Order has been delivered.")

    def cancel(self, context):
        print("Cannot cancel. Order is out for delivery.")

    def get_state_name(self):
        return "OUT_FOR_DELIVERY"


# DeliveredState handles the behavior when the order is delivered
class DeliveredState(OrderState):
    def next(self, context):
        print("Order is already delivered.")

    def cancel(self, context):
        print("Cannot cancel a delivered order.")

    def get_state_name(self):
        return "DELIVERED"


# CancelledState handles the behavior when the order is cancelled
class CancelledState(OrderState):
    def next(self, context):
        print("Cancelled order cannot move to next state.")

    def cancel(self, context):
        print("Order is already cancelled.")

    def get_state_name(self):
        return "CANCELLED"

order = OrderContext()
# Display initial state
print("Current State:", order.get_current_state())
# Moving through states
order.next()  # ORDER_PLACED -> PREPARING
order.next()  # PREPARING -> OUT_FOR_DELIVERY
order.cancel()  # Should fail, as order is out for delivery
order.next()  # OUT_FOR_DELIVERY -> DELIVERED
order.cancel()  # Should fail, as order is delivered
# Display final state
print("Final State:", order.get_current_state())

order2 = OrderContext()
# Display initial state
print("Current State:", order2.get_current_state())
# Moving through states2
order2.next()  # ORDER_PLACED 2-> PREPARING
order2.cancel()  # Should fail2, as order is out for delivery
order2.next()  # PREPARING -> Cancelled
order2.cancel()  # Should fail, as order is delivered
# Display final state
print("Final State:", order2.get_current_state())