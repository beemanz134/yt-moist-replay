import os

from src.browser_sel import check_url, sel_take
from panda_worker import get_datap

def main() -> None:
    user_url = input("Enter YouTube URL:\n")
    if check_url(user_url):
        sel_take(user_url)
    get_datap()


if __name__ == "__main__":
    main()
