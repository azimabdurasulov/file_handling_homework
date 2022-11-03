def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s = []
    for i in data:
        if i.isdigit():
            s.append(int(i))
    return s
# Read data from file

data=open('txt_file/data01.txt','r').read()
print(main(data))