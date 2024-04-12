# This file can include utility functions like date formatting, serialization/deserialization helpers, etc.
from notification_system.notification import Notification
import data
import json
def serialize_notification(notification):
    title = Notification.return_title()
    msg = Notification.return_msg()

    j = json.dumps([title, msg])

    return j


def deserialize_notification(serialized_data):
    pass

