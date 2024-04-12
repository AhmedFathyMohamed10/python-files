import time
import random
import string

class Notification:
    def __init__(self, message):
        self.message = message
        self.timestamp = time.time()

class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        notification = Notification(message)
        self.notifications.append(notification)

    def display_notifications(self):
        for notification in self.notifications:
            print(f"[{time.ctime(notification.timestamp)}] {notification.message}")

def generate_random_string(length=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

if __name__ == "__main__":
    # Create a notification system
    notification_system = NotificationSystem()

    try:
        while True:
            # Generate a random message
            message = generate_random_string()
            
            # Add the message as a notification
            notification_system.add_notification(message)

            # Display notifications
            print("New Notification:")
            notification_system.display_notifications()

            # Wait for 3 seconds
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nNotification system terminated.")
