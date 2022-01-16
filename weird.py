def weird(n):
    if n % 2 != 0 or n in range(6, 21):
        return "Weird"
    elif n in range(2,6) or n >20 :
        return "Not Weird"


if __name__ == "__main__":
    assert weird(1) == "Weird"
    assert weird(4) == "Not Weird"
    assert weird(10) == "Weird"
    assert weird(24) == "Not Weird"

    #n = int(input().strip())
