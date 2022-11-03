def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """

    sum = '\n'.join(data).split()
    sum.append("Computer Vision")

    answer = []
    for i in sum:
        answer += [len(i)]

    return max(answer)


# Read data from file

data = open('txt_file/data10.txt','r').read()
print(main(data))