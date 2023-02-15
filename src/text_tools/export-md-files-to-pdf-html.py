import argparse
import logging
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from markdown import Markdown

load_dotenv()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_folder",
        metavar="input_folder",
        type=str,
        help="The input folder containing markdown files to convert",
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        metavar="output_folder",
        type=str,
        help="The output folder for the converted files",
    )
    parser.add_argument(
        "-f",
        "--format",
        metavar="format",
        type=str,
        choices=["html", "pdf"],
        default="html",
        help="The format of the output files",
    )
    return parser.parse_args()


def validate_input(input_folder):
    if not input_folder:
        raise ValueError("You must provide an input folder")
    else:
        input_folder = Path(input_folder)
        if not input_folder.exists():
            raise ValueError(f"Input folder does not exist: {input_folder}")
    return input_folder


def validate_output(output_folder):
    if not output_folder:
        output_dir = os.environ.get("WORKING_OUTPUT_DIR")
        if not output_dir:
            raise ValueError(
                "You must provide an output folder or set a `WORKING_OUTPUT_DIR` env"
            )
        else:
            output_folder = Path(output_dir)
    else:
        output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True)
    return output_folder


def convert_files(input_folder, output_folder, format_):
    for filepath in input_folder.glob("*.md"):
        # Open the file and check if it contains "#exclude"
        with filepath.open() as f:
            if "#exclude" in f.read():
                # Skip the file if it contains "#exclude"
                continue
        converted_content = convert_wikilinks(filepath)
        # Use pandoc to convert the markdown file to HTML and PDF
        if format_ == "html":
            html_file = output_folder / filepath.with_suffix(".html").name
            with open(html_file, "w") as f:
                f.write(converted_content)
            logging.info(f"{filepath} converted to {html_file}")
        elif format_ == "pdf":
            pdf_file = output_folder / filepath.with_suffix(".pdf").name
            with open(pdf_file, "w") as f:
                f.write(converted_content)
            pandoc_convert(pdf_file, pdf_file, "html")
            logging.info(f"{filepath} converted to {pdf_file}")


def convert_wikilinks(filepath):
    with filepath.open() as f:
        content = f.read()
    md = Markdown(extensions=["mdx_wikilink_plus"])
    content = md.convert(content)
    return content


def pandoc_convert(filepath, output_path, format_):
    subprocess.run(
        [
            "pandoc",
            str(filepath),
            "-s",
            "--pdf-engine=xelatex",
            "-V",
            "mainfont=Arial Unicode MS",
            "pandocinput=" + str(filepath),
            "--template=template.tex",
            "-o",
            output_path,
            f"-f{format_}",
        ]
    )


def main():
    # Parse command-line arguments
    args = parse_args()

    # Validate inputs and outputs
    input_folder = validate_input(args.input_folder)
    output_folder = validate_output(args.output_folder)

    # Configure logging
    logging.basicConfig(filename=output_folder / "conversion.log", level=logging.INFO)

    # Convert files
    convert_files(input_folder, output_folder, args.format)


if __name__ == "__main__":
    main()


# Usage: python src/text_tools/export-md-files-to-pdf-html.py -i "/Users/alexclaydon/Journals/Master/\!Journal/"
