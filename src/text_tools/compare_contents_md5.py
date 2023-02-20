"""
compare_contents_md5.py - Check the contents of a folder for files with the same content based on the md5 hash of the file contents and print out either the duplicates or the non-duplicates, depending on the command line arguments. The script can be run from the command line with the following arguments:

positional arguments:
  folder                folder containing the input files

optional arguments:
  -h, --help            show this help message and exit
  -d, --duplicates      log files that are duplicates
  -n, --nonduplicates   log files that are not duplicates

By default, the script creates a CSV file named "compare-contents-md5.csv" in a subdirectory named "output" in the input folder, unless an environment variable named WORKING_OUTPUT_DIR is defined, in which case the file will be written to that directory. The CSV file contains the following columns:

- Hash: the MD5 hash of the file contents
- File #01: the first file with the matching content
- File #02: the second file with the matching content (only for duplicates)

If no files are found in the input folder, the script will exit with an error message. If the --duplicates or --nonduplicates flag is not specified, the script will exit with an error message.
"""


import argparse
import csv
import hashlib
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def parse_args():
    arg_parser = argparse.ArgumentParser(
        description="Check the contents of a folder for files with the same content based on the md5 hash of the file contents and print out the duplicates."
    )
    arg_parser.add_argument(
        "folder", nargs="?", type=str, help="folder containing the input files"
    )
    arg_parser.add_argument(
        "-d", "--duplicates", help="log files that are duplicates", action="store_true"
    )
    arg_parser.add_argument(
        "-n",
        "--nonduplicates",
        help="log files that are not duplicates",
        action="store_true",
    )
    return arg_parser.parse_args()


def get_folder_from_env():
    folder_path = os.getenv("WORKING_INPUT_DIR")
    if folder_path is None:
        print("Environment variable WORKING_INPUT_DIR is not set.")
        exit(1)
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"{folder} is not a valid directory")
        exit(1)
    return folder


def check_folder_for_duplicates(folder):
    # Determine output folder
    output_dir = os.getenv("WORKING_OUTPUT_DIR")
    if output_dir is not None:
        output_folder = Path(output_dir)
    else:
        output_folder = folder / "output"
    output_folder.mkdir(parents=True, exist_ok=True)
    log_file = output_folder / "compare-contents-md5.csv"

    # Use a csv formatter
    formatter = logging.Formatter("%(message)s")
    file_handler = logging.FileHandler(log_file, mode="w")
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().setLevel(logging.INFO)

    hashes = {}
    for file in folder.iterdir():
        if file.is_file():
            with open(file, "rb") as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in hashes:
                    hashes[file_hash].append(file)
                else:
                    hashes[file_hash] = [file]

    if args.duplicates:
        with open(log_file, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(["Hash", "File #01", "File #02"])
        for hash, files in hashes.items():
            if len(files) > 1:
                with open(log_file, mode="a", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=",")
                    csv_writer.writerow([hash] + [str(file) for file in files])
    elif args.nonduplicates:
        with open(log_file, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(["Hash", "File"])
        for hash, files in hashes.items():
            if len(files) == 1:
                with open(log_file, mode="a", newline="") as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=",")
                    csv_writer.writerow([hash, str(files[0])])
    else:
        print("You must specify either --duplicates or --nonduplicates")
        exit(1)


if __name__ == "__main__":
    args = parse_args()
    if args.folder is not None:
        folder = Path(args.folder)
    else:
        folder = get_folder_from_env()
    check_folder_for_duplicates(folder)
