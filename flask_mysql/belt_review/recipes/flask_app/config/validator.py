import re
class Email:
    valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    @classmethod
    def inspect(cls, email):
        return cls.valid_email.match(email)