def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    sum = []
    for i in data:
        if not i.isdigit():
            sum += [i]
    return sum
# Read data from file

data=open('txt_file/data04.txt','r').read()
print(main(data))