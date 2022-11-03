def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    sum = "".join(data).split()

    answer = []
    for i in sum:
        answer.append(len(i))

    return answer
# Read data from file

data = open("txt_file/data06.txt", "r").read()
print(main(data))