#!/usr/bin/python3
if __name__ == "__main__":
    import sys
i = len(sys.argv)
if i <= 1:
    print("0 arguments.")
elif i == 2:
    print(i - 1, "arguments:".format(i))
else:
    print(i - 1, "arguments:".format(i))
    for a in range(1, i):
        print("{a}:{sys.argv[i]}".format(i + 1))
