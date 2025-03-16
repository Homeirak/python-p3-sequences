#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = [0, 1]
    if length == 0:
        print([])
        return
    elif length == 1:
        print ([0])
        return
    elif length == 2:
        print ([0, 1])
        return
    else:
        for i in range(2, length):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(fibonacci_sequence)

print_fibonacci(0)  # Output: []
print_fibonacci(1)  # Output: [0]
print_fibonacci(2)  # Output: [0, 1]
print_fibonacci(5)  # Output: [0, 1, 1, 2, 3]
