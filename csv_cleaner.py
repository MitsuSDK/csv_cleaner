import csv
from pathlib import Path
import argparse

def clean_field(value: str) -> str:
    """
    Return the input string with leading and trailing spaces removed.
    """
    start = 0
    end = len(value) - 1

    #moves start forward while it points to a space
    while start <= end and value[start] == ' ':
        start = start + 1

    #move end backward while it points to a space
    while end >= start and value[end] == ' ':
        end = end -1
        
    return value[start:end+1]

def clean_row(row: list[str]) -> list[str]:
    """
    Return the input row with each field cleaned.
   
    :param row: A list of string values from a csv file
    :return: A list of cleaned string values
    """
    cleaned_row = []

    #clean every field contained in a row
    for field in row:
        cleaned_row.append(clean_field(field))
    return cleaned_row

def is_empty_row(row: list[str]) -> bool:
    """
    Return True if the input row is empty(all fields are empty or the row contains no field).
    """ 
    return (all(field == "" for field in row))

def deduplicate_rows(rows: list[list[str]]) -> list[list[str]]:
    """
    Return a list of unique rows.
    
    :param rows: A list of raws
    """
    seen = set()
    cleaned = []

    for row in rows:
        #use tuples because only hashable and immuable objects can be put in a set()
        row_key = tuple(row)

        if row_key not in seen:
            seen.add(row_key)
            cleaned.append(row)

    return cleaned

def process_rows(rows: list[list[str]], dedupe: bool = 0) -> list[list[str]]:
    """
    Return a list of cleaned rows
    """
    cleaned = []
    for row in rows:
        cleaned_row = clean_row(row)
        if not is_empty_row(cleaned_row):
            cleaned.append(cleaned_row)
    if dedupe:
        cleaned = deduplicate_rows(cleaned)
    return cleaned

def read_csv(filepath: str) -> list[list[str]]:
    """
    Read a csv file and return its rows
    """
    rows=[]
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows

def write_csv(filepath: str, rows: list[list[str]]) -> None:
    """
    Write rows to a CSV file, creating parent directories if needed.
    """
    path = Path(filepath)

    # create parent directories if they don't exist
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clean a CSV file by normalizing fields, removing empty raws, and deduplicating if precised."
    )

    parser.add_argument(
        "input",
        help="Path to the input CSV file"
    )

    parser.add_argument(
        "output",
        help="Path to the output CSV file"
    )

    parser.add_argument(
        "--no-dedupe",
        action="store_true",
        help="Disable row deduplication"
    )

    args = parser.parse_args()

    rows = read_csv(args.input)
    cleaned = process_rows(rows, dedupe=not args.no_dedupe)
    write_csv(args.output, cleaned)

if __name__ == "__main__":
    main()