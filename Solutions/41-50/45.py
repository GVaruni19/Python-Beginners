import numpy as np

def stddev(x):
    listy = []
    for i in x:
        listy.append(int(i))
    st = np.std(listy)
    print(st)


if __name__ == "__main__":
    k = list(map(str, input("Enter numbers in array with space: ").split(" ")))
    # print(k)
    stddev(k)