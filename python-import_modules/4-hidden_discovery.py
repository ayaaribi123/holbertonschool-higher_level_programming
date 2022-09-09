#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    i = dir(hidden_4)
    for a in i:
        if a[0:2] != "__":
            print(a)
