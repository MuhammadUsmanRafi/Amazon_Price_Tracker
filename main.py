import requests
from bs4 import BeautifulSoup
import smtplib

def get_user_input(message):
    return input(message)

def send_email(subject, message, to_addrs, sender_email, sender_password):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=to_addrs,
            msg=f"Subject:{subject}\n\n{message}"
        )

def main():
    URL = get_user_input("Enter the URL of the Amazon product you want to track the price of: ")

    MY_EMAIL = "your_email@gmail.com"
    MY_PASSWORD = "your_email_password"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url=URL, headers=header)
    content = response.text

    soup = BeautifulSoup(content, "lxml")

    title = soup.find(id="productTitle").get_text().strip()
    price = float(soup.select_one("span.a-offscreen").getText().split("$")[1])

    user_price = float(input(f"The current price of the product is ${price}. Enter the price you want to get an alert on email: "))
    user_email = get_user_input("\nEnter your Email Address (abc@gmail.com): ")

    if user_price <= price:
        message = f"{title} is now ${price}"
        subject = "Amazon Price Alert!"
        body = f"\n\n{message}\n{URL}"
        send_email(subject, body, user_email, MY_EMAIL, MY_PASSWORD)

if __name__ == "__main__":
    main()
