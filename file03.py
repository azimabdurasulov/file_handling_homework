def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    sum = []
    for i in data:
        if i.isdigit():
            sum += [i]
    return sum
# Read data from file

data=open('txt_file/data03.txt','r').read()
print(main(data))