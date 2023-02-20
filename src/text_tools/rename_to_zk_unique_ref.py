import argparse
import logging
import os
from pathlib import Path

from dateutil import parser as date_parser
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

load_dotenv()


def get_input_folder():
    parser = argparse.ArgumentParser(description="Rename files based on their date")
    parser.add_argument(
        "folder", nargs="?", type=str, help="folder containing the input files"
    )
    parser.add_argument("--output", "-o", type=str, help="output folder path")
    args = parser.parse_args()

    if args.folder is not None:
        folder = Path(args.folder)
    elif os.environ.get("WORKING_INPUT_DIR") is not None:
        folder = Path(os.environ.get("WORKING_INPUT_DIR"))
    else:
        print(
            "Please provide a folder path or set the WORKING_INPUT_DIR environment variable."
        )
        exit(1)

    if not folder.is_dir():
        logging.error(f"{folder} is not a valid directory")
        exit(1)

    if args.output is not None:
        output_folder = Path(args.output)
    elif os.environ.get("WORKING_OUTPUT_DIR") is not None:
        output_folder = Path(os.environ.get("WORKING_OUTPUT_DIR"))
    else:
        print(
            "Please provide an output folder path or set the WORKING_OUTPUT_DIR environment variable."
        )
        exit(1)

    return folder, output_folder


def rename_files(folder, output_folder):
    output_folder.mkdir(parents=True, exist_ok=True)
    log_file = output_folder / "rename.log"
    logging.basicConfig(filename=log_file, level=logging.DEBUG)

    console = Console()

    for file in folder.iterdir():
        if file.is_file() and file.suffix == ".md":
            success = rename_file(file, output_folder)
            if success:
                console.print(Panel(file.name, style="green"))
            else:
                console.print(Panel(file.name, style="red"))


def rename_file(file, output_folder):
    date = file.stem
    try:
        new_date = date_parser.parse(date).strftime("%Y%m%d")
    except ValueError:
        new_date = input(
            f"Please enter the date for the file '{file.name}' in the format YYYY-MM-DD: "
        )
        try:
            new_date = date_parser.parse(new_date).strftime("%Y%m%d")
        except ValueError:
            logging.error(f"Unable to convert the date in the file {file}")
            return False
    new_file_name = get_new_file_name(output_folder, new_date)
    new_file = output_folder / new_file_name
    i = 1
    while new_file.exists():
        new_file_name = f"{new_date}-dup({i}).md"
        new_file = output_folder / new_file_name
        i += 1
    with open(file, "r") as f:
        with open(new_file, "w") as f1:
            f1.write(f.read())
    logging.info(f"{file} was successfully copied to {new_file_name}")
    return True


def get_new_file_name(output_folder, new_date):
    return f"{new_date}.md"


def main():
    folder, output_folder = get_input_folder()
    rename_files(folder, output_folder)


if __name__ == "__main__":
    main()
