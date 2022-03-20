import re
class Email:
    valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    @classmethod
    def inspect(cls, email):
        return cls.valid_email.match(email)
        
class Text_Field:
    def __init__(self, min_length, max_length=255) -> None:
        self.min_length = min_length
        self.max_length = max_length
    
    def inspect(self, text_input):
        if len(text_input) < self.min_length or len(text_input) > self.max_length:
            return False
        else:
            return True