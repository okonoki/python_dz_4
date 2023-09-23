# Task 33

# n = int(input('Input count marks: '))
# marks = [int(i) for i in input('Input marks: ').split()[:n]]
#
# print(*[min(marks) if i == max(marks) else i for i in marks])

# Task 35

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Task 37
