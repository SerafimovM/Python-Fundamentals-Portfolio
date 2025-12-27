import random
import string
import math
from typing import List, Dict

"""
UTILITY LIBRARY
Author: Martin Serafimov
Description: A collection of helper functions for mathematical and string operations.
"""

def is_even(number: int) -> bool:
    """Checks if a number is even."""
    return number % 2 == 0

def is_odd(number: int) -> bool:
    """Checks if a number is odd."""
    return number % 2 != 0

def calculate_percentage(part: float, whole: float) -> float:
    """Calculates what percentage 'part' is of 'whole'."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage with zero denominator")
    return (part / whole) * 100

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def get_max_value(numbers: List[float]) -> float:
    """Finds the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    return max(numbers)

def is_palindrome(text: str) -> bool:
    """Checks if a string reads the same backwards (ignoring case)."""
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

def generate_strong_password(length: int = 12) -> str:
    """Generates a random secure password including special characters."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def count_vowels(text: str) -> int:
    """Counts the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def calculate_average(numbers: List[float]) -> float:
    """Calculates the average (mean) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def reverse_string(text: str) -> str:
    """Returns the reversed version of a string."""
    return text[::-1]

def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """Merges two dictionaries into one."""
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# --- Test Execution ---
if __name__ == "__main__":
    print(f"Is 10 even? {is_even(10)}")
    print(f"Percentage: {calculate_percentage(20, 50)}%")
    print(f"Generated Password: {generate_strong_password(16)}")
    print(f"Is 17 prime? {is_prime(17)}")