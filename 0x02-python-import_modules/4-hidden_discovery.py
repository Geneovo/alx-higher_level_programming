#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    name = dir(hidden_4)
    for z in name:
        if z[:2] != "__":
            print(z)
