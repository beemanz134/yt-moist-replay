import os
import pandas as pd
from src.browser_sel import check_url, sel_take
from panda_worker import get_datap

def main() -> None:
    duration = 0
    user_url = input("Enter YouTube URL:\n")
    if check_url(user_url):
        duration = sel_take(user_url)
        get_datap(duration)



if __name__ == "__main__":
    main()
