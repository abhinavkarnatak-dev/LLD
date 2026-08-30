# Major inner implementation skipped

class PaymentService:
    def make_payment(self, accound_id, amount):
        print(f"Payment of Rs.{amount} successful for account {accound_id}")

class SeatReservationService:
    def reserve_seat(self, movie_id, seat_number):
        print(f"Seat {seat_number} reserved for movie {movie_id}")

class NotificationService:
    def send_booking_confirmation(self, user_email):
        print(f"Booking confirmation sent to {user_email}")

class LoyaltyPointsService:
    def add_points(self, account_id, points):
        print(f"{points} loyalty points added to account {account_id}")

class TicketService:
    def generate_ticket(self, movie_id, seat_number):
        print(f"Ticket generated for movie {movie_id}, Seat: {seat_number}")

class MovieBookingFacade:
    def __init__(self):
        # Initialize all the subsystem services inside the facade
        self.payment_service = PaymentService()
        self.seat_reservation_service = SeatReservationService()
        self.notification_service = NotificationService()
        self.loyalty_points_service = LoyaltyPointsService()
        self.ticket_service = TicketService()

    def book_movie_ticket(
        self,
        account_id,
        movie_id,
        seat_number,
        user_email,
        amount
    ):
        # Step 1: Make payment
        self.payment_service.make_payment(account_id, amount)

        # Step 2: Reserve seat
        self.seat_reservation_service.reserve_seat(movie_id, seat_number)

        # Step 3: Generate ticket
        self.ticket_service.generate_ticket(movie_id, seat_number)

        # Step 4: Add loyalty points
        self.loyalty_points_service.add_points(account_id, 50)

        # Step 5: Send confirmation
        self.notification_service.send_booking_confirmation(user_email)

        # Indicate successful completion of the entire booking process
        print("Movie ticket booking completed successfully!")

movie_booking_facade = MovieBookingFacade()
movie_booking_facade.book_movie_ticket("user123", "movie456", "A10", "user@example.com", 200)