# SupportService handles different types of support requests
class SupportService:
    # Method to handle the support request based on the type of issue
    def handle_request(self, type):
        if type == "general":
            print("Handled by General Support")
        elif type == "refund":
            print("Handled by Billing Team")
        elif type == "technical":
            print("Handled by Technical Support")
        elif type == "delivery":
            print("Handled by Delivery Team")
        else:
            print("No handler available")

support_service = SupportService()

support_service.handle_request("general")
support_service.handle_request("refund")
support_service.handle_request("technical")
support_service.handle_request("delivery")
support_service.handle_request("unknown")