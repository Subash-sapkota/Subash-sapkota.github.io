import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "SapkotaSubash"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'subashsapkota213@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")  # Use environment variable
app.config['MAIL_DEFAULT_SENDER'] = 'subashsapkota213@gmail.com'

mail = Mail(app)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form

        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        if name and email and message:
            msg = Message("Message from the Portfolio Website", sender=app.config["MAIL_DEFAULT_SENDER"],
                          recipients=["subashsapkota213@gmail.com"])

            msg.body = f"Message from: {name}\n Email: {email}\n Message:{message}"
            mail.send(msg)

            auto_reply = Message("Thank you for Your message", sender=app.config["MAIL_DEFAULT_SENDER"],
                                 recipients=[email])
            auto_reply.body = ("This is an automated response to confirm that I have received your message. I will get "
                               f"back to you as soon as possible.\n\n Your Message:\n {message}")
            mail.send(auto_reply)

            return render_template("contact.html", smsg="Your message has been sent. Thank you for reaching out!")
        else:
            return render_template("contact.html", error="Something went Wrong!")

    return render_template("contact.html")


@app.route("/projects")
def projekts():
    return render_template("projects.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


if __name__ == '__main__':
    app.run()
