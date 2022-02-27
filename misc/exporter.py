import subprocess
import os


def generate_in_out(tracker):
    # Working directory
    cwd = os.getcwd() + "/"

    # Output directory
    od = cwd + "Results/"

    # input file
    input_file = cwd + "*" + tracker.month + ".ipynb"

    # output
    output_file = od + tracker.month

    return input_file, output_file


def export_to_html(tracker, silent=True):
    #  Get file names
    input_file, output_file = generate_in_out(tracker)

    # Add extension
    output_file += ".html"

    # generate process to call
    export_html = ["jupyter-nbconvert", "--to", "html", "--no-input", input_file, "--output", output_file]

    # call it
    if silent:
        subprocess.call(export_html, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    else:
        subprocess.call(export_html)


def export_to_pdf(tracker, silent=True):
    #  Get file names
    input_file, output_file = generate_in_out(tracker)

    # Add extension
    output_file += ".pdf"

    # generate process to call
    export_pdf = ["jupyter-nbconvert", "--to", "PDFviaHTML", "--no-input", input_file, "--output", output_file]

    # call it
    if silent:
        subprocess.call(export_pdf, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    else:
        subprocess.call(export_pdf)
