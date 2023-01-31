
def collatz(num):
    n = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            n += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            n += 1
            if n > 500:
                return -1
    return n
collatz(6)  # => 8

# collatz(16)  # => 4
# collatz(27)  # => 111
# collatz(626331)  # => -1