from pathlib import Path
import os
import random
import csv
from datetime import datetime
import pandas as pds

from django.conf import settings
from django.core.files import File
from django.conf import settings


def get_random_string(length=1):
    rand_str = ""
    for c in random.choices(settings.CHOICES, k=length):
        rand_str += c

    return rand_str


def get_file_path(file=None, file_name=None, force=False):
    """
    Builds file path from given file or name,
    optionally creates file if it doesn't exist
    if force is true.

    If file name already exists in system,
    appends a string of 7 chars to name.
    """
    if not file and not file_name:
        raise Exception("A file object or file name should be given.")
    if file and file_name:
        raise Exception("Only one of file object or file name should be given")
    if file:
        if isinstance(file, File):
            name = file.name
        else:
            raise Exception(f"File should be of type {File.__name__}")
    elif file_name:
        name = file_name
    path = Path(os.path.join(settings.FILE_ROOT, name))

    if force:
        while path.exists():
            rand_str = get_random_string(7)
            file_name_splits = name.split(".")
            name = (
                ".".join(file_name_splits[:-1])
                + "_"
                + rand_str
                + "."
                + file_name_splits[-1]
            )
            path = Path(os.path.join(settings.FILE_ROOT, name))
        path.touch()

    return path


def file_exists(name):
    path = Path(os.path.join(settings.FILE_ROOT, name))
    if path.exists():
        return True
    return False


# file is pathlib Path
def get_rows_from_csv_file(file_path):
    """
    Returns list of rows, all rows are adjusted
    to the row with highest cols by adding None elements to rows
    """
    file_type = file_path.split(".")[-1]
    if file_type == "csv":
        data = []
        max_len = 0

        with open(file_path, "r") as csvfile:
            rows = pds.read_csv(csvfile, sep=",", header=None)
            data = rows.values.tolist()

        return data
    else:
        raise Exception("Not a file of type csv.")


def get_rows_from_xlsx_file(file_path):
    file_type = file_path.split(".")[-1]
    if file_type == "xlsx" or file_type == "xls":
        with open(file_path, "rb") as xlsxfile:
            rows = pds.read_excel(xlsxfile.read())
            data = rows.values.tolist()
        # convert all types to string for template
        for row in data:
            for j in range(len(row)):
                if not isinstance(row[j], str):
                    try:
                        row[j] = str(row[j])
                    except:
                        raise Exception('Your File consists of fields that cannot be parsed')
        return data
    else:
        raise Exception("Not a file of type xlsx.")
