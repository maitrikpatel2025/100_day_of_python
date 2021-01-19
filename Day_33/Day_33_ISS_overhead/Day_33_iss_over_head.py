
import requests
import datetime
import smtplib
import time

MY_LAT = 43.731548
MY_LONG = -79.762421
my_email = "maitrik.patel3011@gmail.com"
password = "30112025"
to_email = "maitrik.patel2025@gmail.com"


def iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_data = response.json()
    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_long = float(iss_data['iss_position']['longitude'])
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now()
    hour_now = time_now.hour
    if hour_now >= sunset or hour_now <= sunrise:
        return True


while True:
    time.sleep(60000)
    if is_night() and iss_over_head():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_email,
                                msg="Subject: ISS is overhead \n\n check you can find iss on your head")
