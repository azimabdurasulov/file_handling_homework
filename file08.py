def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sum = ''.join(data).split()
    max=0
    
    for i in sum:
        if i.isdigit():
            if max < int(i):
                max = int(i)
    return max

# Read data from file

data = open('txt_file/data08.txt','r').read()
print(main(data))
