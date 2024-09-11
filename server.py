from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("register.html")

if __name__ == "__main__":
    host = "172.31.42.229"
    port = 4000
    app.run(host, port,True)
