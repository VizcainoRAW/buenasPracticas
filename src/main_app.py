from flask import Flask;

app= Flask(__name__)
@app.route("/")
def index():
    return "xd"

if __name__=="__main__":
    app.run()