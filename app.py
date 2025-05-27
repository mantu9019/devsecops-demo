from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f4f8;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #007ACC;
                font-size: 48px;
            }
            p {
                font-size: 20px;
                margin-top: 20px;
            }
            .container {
                background: white;
                padding: 40px;
                margin: auto;
                border-radius: 15px;
                max-width: 600px;
                box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, DevSecOps!</h1>
            <p>This is a simple web app secured and deployed using DevSecOps practices.</p>
            <p>CI/CD ✔️  |  Security Scan ✔️  |  Docker ✔️</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
