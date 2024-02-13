
def generate_fibonacci(max):
    fibonacci_sequence = [0, 1] 
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  
        if next_number <= max:
            fibonacci_sequence.append(next_number) 
        else:
            break  
    return fibonacci_sequence

fibonacci_sequence_up_to_100 = generate_fibonacci(100)

print("Fibonacci sequence up to 100:")
print(fibonacci_sequence_up_to_100)
