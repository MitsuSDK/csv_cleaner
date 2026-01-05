def clean_field(value: str) -> str:
    """
    return the input string with leading and trailing spaces removed.
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