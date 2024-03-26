import pandas

def read_prompt():
    """
    Reads input from user

    Returns:
        str: user input
    """
    return input()

def read_file_builtin(path : str):
    """
    Reads file using built-in function

    Returns:
        str: file content
    """
    with open(path, 'r') as f:
        result = f.read()
        
        return result

def read_file_pandas(path : str):
    """
    Reads file using pandas

    Returns:
        str: file content
    """
    df = pandas.read_csv(path)

    return df.to_csv()
