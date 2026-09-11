from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World - Jenkins CI/CD</title>
    </head>
    <body>
        <h1>Hello World!</h1>
        <h2>Jenkins CI/CD is Working!</h2>
        <p>Application deployed using Docker on AWS EC2.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
