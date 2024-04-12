from datetime import datetime

class Notification:
    def __init__(self, title: str='', message: str='', timestamp: datetime = datetime.now(), read_status: bool = False):
        self.title = title
        self.message = message
        self.timestamp = timestamp
        self.read_status = read_status

    def mark_as_read(self):
        if self.read_status == False:
            return f'The message hasnot read!'
        else:
            return self.message[:10]

    def __str__(self):
        return str(self.title) 
    
    def return_title(self):
        return self.title
    
    def return_msg(self):
        return self.message

