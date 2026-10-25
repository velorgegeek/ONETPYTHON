@staticmethod
def do(x: float) -> int:
    if(x >=100.7):
        return 1000
    elif x > 0:
        return int(x)
    elif x == 0:
        raise ValueError("X EQUAL 0")
    elif x>= -30.4:
        return int(x) -5
    else:
        return 2000
