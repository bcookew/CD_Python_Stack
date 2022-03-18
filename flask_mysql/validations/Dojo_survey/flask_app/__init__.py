from flask import Flask, session

app = Flask(__name__)
app.secret_key = "skdflaiudbvlialvsdfvb82772fr982h89yfrh"

user_session = session