from notification_system.manager import NotificationManager
from interface.console import ConsoleInterface

def main():
    manager = NotificationManager()
    interface = ConsoleInterface(manager)
    interface.display_menu()

if __name__ == "__main__":
    main()

