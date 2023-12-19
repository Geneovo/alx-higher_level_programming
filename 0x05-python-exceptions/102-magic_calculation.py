#!/usr/bin/python3
def magic_calculation(a, b):
    total = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                total = (a ** b) / i

        except Exception:
            total = b + a
            break

        return total
