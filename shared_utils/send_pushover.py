import argparse
import http.client
import os
import urllib

from dotenv import load_dotenv

load_dotenv()


def notify_with_pushover(message: str):
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request(
        "POST",
        "/1/messages.json",
        urllib.parse.urlencode(
            {
                "token": os.getenv("PUSHOVER_TOKEN"),
                "user": os.getenv("PUSHOVER_USER"),
                "message": message,
            }
        ),
        {"Content-type": "application/x-www-form-urlencoded"},
    )
    conn.getresponse()


def main():
    parser = argparse.ArgumentParser(description="Send a message to Pushover")
    parser.add_argument("message", type=str, help="The message to send")
    args = parser.parse_args()
    notify_with_pushover(args.message)


if __name__ == "__main__":
    main()
