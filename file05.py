def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    intejer = 0
    string = 0
    for i in data:
        if i.isdigit():
            intejer += 1

        else:
            string += 1

    return [intejer, string]
# Read data from file

data = open("txt_file/data05.txt", "r").read()
print(main(data))