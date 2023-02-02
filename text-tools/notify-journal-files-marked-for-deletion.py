# A thin Python wrapper around ripgrep to return a list of files in a particular format and notify them to the user using Pushover

import os
import subprocess
import sys

from dotenv import load_dotenv

from shared_utils.send_pushover import notify_with_pushover

load_dotenv()

sys.path.append(os.getenv("PYTHONPATH"))


def search_with_ripgrep(pattern, path):
    result = subprocess.run(["rg", pattern, path], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout


def main():
    search_results = search_with_ripgrep("#delete", os.getenv("JOURNALS_PATH"))
    notify_with_pushover(search_results)


if __name__ == "__main__":
    main()
