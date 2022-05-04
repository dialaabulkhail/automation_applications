import smtplib
import ssl
from email.message import EmailMessage

"""
This is a basic project that is going to allow you send emails using python
To make this work:
fill up the subject and body with the message you want to send.
run the file and type the password
check your email!
"""

# first we identified some variables required in any email message
subject = "Email from Python"
body = "This is a test email"
# to be able to access the email: less security is required from the gmail account
sender_email = "hala.bk418@gmail.com"
receiver_email = "hala.bk418@gmail.com"
password = input("Enter password: ")


# to send the email
message = EmailMessage()
message["Form"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)

                              ### HTML: was added lastly
                              # html is used to format the the email, **see the pictures
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
# rather than sending the content above:
message.add_alternative(html, subtype= "html")

# to secure the connection when using the libraries and connecting them to the gmail
context = ssl.create_default_context()


print("Sending Email.")

# connecting to the gmail server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
    # use server to log into the account
    server.login(sender_email, password)
    #here we convert the objects above that we want to send to be sent as strings
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent!")