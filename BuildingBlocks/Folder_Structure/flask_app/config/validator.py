import re
from flask import session, redirect, flash
class Email:
    valid_email = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    
    @classmethod
    def inspect(cls, email):
        return cls.valid_email.match(email)

class Password:
    valid_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%^&*<>])[A-Za-z\d!#$%^&*<>]{8,}$')
    
    @classmethod
    def inspect(cls, password):
        return cls.valid_password.match(password)

class Text_Field:
    def __init__(self, min_length, max_length=255) -> None:
        self.valid_text_field = re.compile(r'^[A-Za-z]{' + str(min_length) + ',' + str(max_length) + '}$')

    def inspect(self, text_input):
        return self.valid_text_field.match(text_input)

class Logged_in:
    def log_in_checker():
        if 'user_id' not in session:
            flash("Access Denied!\nYou must log in!")
            return redirect('/')