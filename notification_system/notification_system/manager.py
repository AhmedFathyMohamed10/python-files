from typing import List
from notification_system.notification import Notification

class NotificationManager:
    def __init__(self):
        pass

    def add_notification(self, notification: Notification):
        pass

    def remove_notification(self, notification_id: int):
        pass

    def mark_notification_as_read(self, notification_id: int):
        pass

    def get_all_notifications(self) -> List[Notification]:
        pass

    def get_unread_notifications(self) -> List[Notification]:
        pass

    def clear_all_notifications(self):
        pass

