from borrowing.serializers import book
from notifications.tasks import send_notification, send_reminder
from datetime import datetime

def update_book_inventory(book):
    if book.inventory < 1:
        raise ValueError("This book is not available")
    book.inventory -= 1
    book.save()


#
# def send_telegram_notification(borrowing):
#     book = borrowing.book
#     message = (
#         f"New borrowing created:\n"
#         f"User: {borrowing.user.username}\n"
#         f"Book: {borrowing.book.title}\n"
#         f"Date of borrowing: {borrowing.borrow_date}\n"
#         f"Date to return: {borrowing.expected_return}"
#     )
#     send_notification.delay(message)
#
# def generate_reminder_message(borrowing):
#     today = datetime.today().date()
#
#     reminder_one = (
#         f"You have new reminder:\n"
#         f"You borrowed book '{book.title}' on {borrowing.borrow_date}\n"
#         f"You must return it by {borrowing.expected_return}\n"
#         f"Daily fee for this book: {book.daily_fee}"
#     )
#
#     reminder_two = (
#         f"OVERDUE!\n"
#         f"You borrowed '{book.title}' on {borrowing.borrow_date}\n"
#         f"You missed return date {borrowing.expected_return}\n"
#         f"Daily fee: {book.daily_fee + 15}"
#     )
#
#     if today < borrowing.expected_return:
#         return reminder_one
#     else:
#         return reminder_two
#
#
# def send_reminder_messages(borrowing):
#     book = borrowing.book
#     today = datetime.today().date()
#
#     reminder_one = (
#         f"You have new reminder:\n"
#         f"You borrowed book '{book.title}' on {borrowing.borrow_date}\n"
#         f"You must return it by {borrowing.expected_return}\n"
#         f"Daily fee for this book: {book.daily_fee}"
#     )
#
#     reminder_two = (
#         f"OVERDUE!\n"
#         f"You borrowed '{book.title}' on {borrowing.borrow_date}\n"
#         f"You missed return date {borrowing.expected_return}\n"
#         f"Daily fee: {book.daily_fee + 15}"
#     )
#
#
#     if today < borrowing.expected_return:
#         return reminder_one
#     else:
#         return reminder_two
#
#     send_reminder.delay(reminder)


