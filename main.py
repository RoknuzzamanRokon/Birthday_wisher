import smtplib


email = "roko.ron017@gmail.com"
password = "Rokoron559445689"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email,password=password)
connection.sendmail(
    from_addr=email,
    to_addrs="rokon.raz@gmail.com",
    msg="Subject:Hello\n\nThis is the body of the mail"
)

connection.close()
