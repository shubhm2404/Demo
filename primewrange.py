"""
Functions to check for prime numbers and find prime numbers in a given range.
"""


def is_prime(num):

    """
    Function to check if a number is prime.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers_in_range(start, end):
    """
    Function to find prime numbers in a given range and append them to a list.

    Args:
    start (int): The starting number of the range.
    end (int): The ending number of the range.

    Returns:
    list: A list of prime numbers in the specified range.
    """
    prime_numbers = []  # List to store prime numbers
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)  # Append prime number to the list
    return prime_numbers
