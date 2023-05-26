import smtplib


email = "roko.ron018@yahoo.com"
password = "Rokoron559445689"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="rokon.raz@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the mail"
    )