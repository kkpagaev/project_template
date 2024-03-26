
def puts(text : str):
    """
    Prints text to console

    Args:
        text: text to print
    """
    print(text)


def write_to_file(filepath : str, text : str):
    """
    Writes text to file

    Args:
        filepath: path to file
        text: text to write
    """
    with open(filepath, 'w') as f:
        f.write(text)


