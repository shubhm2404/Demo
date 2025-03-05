# Function to check if a number is prime


def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to find prime numbers in a given range and append them to a list

def prime_numbers_in_range(start, end):
    prime_numbers = []  # List to store prime numbers
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)  # Append prime number to the list
    return prime_numbers


# Take user input for the range


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


# Get the list of prime numbers in the specified range

prime_list = prime_numbers_in_range(start, end)

# Print the prime numbers list

print(f"Prime numbers between {start} and {end} are: {prime_list}")
