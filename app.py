from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Wellcome to theramya10_World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
