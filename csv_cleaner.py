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