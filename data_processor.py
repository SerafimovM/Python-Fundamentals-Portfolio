"""
DATA PROCESSOR
Author: Martin Serafimov
Description: Demonstrates usage of Lists, Dictionaries, and Loops for data manipulation.
"""

from typing import Dict, List, Any

def analyze_grades(students_scores: Dict[str, List[float]]) -> None:
    """Analyzes and displays student grades with pass/fail status."""
    if not students_scores:
        raise ValueError("Student scores dictionary cannot be empty")
    
    print("--- Student Grade Analysis ---")
    
    for name, scores in students_scores.items():
        if not scores:
            raise ValueError(f"No scores provided for {name}")
        
        average = sum(scores) / len(scores)
        status = "PASSED" if average >= 70 else "FAILED"
        
        print(f"Student: {name} | Average: {average:.2f} | Status: {status}")

def filter_inventory(inventory: List[Dict[str, Any]]) -> None:
    """Analyzes inventory and alerts for low or out-of-stock items."""
    if not inventory:
        raise ValueError("Inventory list cannot be empty")
    
    print("\n--- Low Stock Alert (Below 3 items) ---")
    
    for product in inventory:
        stock = product.get("stock", 0)
        item_name = product.get("item", "Unknown")
        
        if stock < 3 and stock > 0:
            print(f"WARNING: Low stock on {item_name} (Only {stock} left!)")
        elif stock == 0:
            print(f"CRITICAL: {item_name} is OUT OF STOCK.")

def find_common_elements(list_a: List[int], list_b: List[int]) -> List[int]:
    """Finds and returns common elements between two lists."""
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise TypeError("Both arguments must be lists")
    
    common = [num for num in list_a if num in list_b]
    print(f"\nCommon elements between lists: {common}")
    return common

if __name__ == "__main__":
    students_scores = {
        "Alice": [85, 90, 88],
        "Bob": [70, 75, 72],
        "Charlie": [95, 92, 98],
        "Diana": [60, 65, 58]
    }
    
    inventory = [
        {"item": "Laptop", "price": 1200, "stock": 5},
        {"item": "Mouse", "price": 20, "stock": 0},
        {"item": "Keyboard", "price": 50, "stock": 12},
        {"item": "Monitor", "price": 300, "stock": 2}
    ]
    
    analyze_grades(students_scores)
    filter_inventory(inventory)
    find_common_elements([1, 2, 3, 4, 5, 10], [4, 5, 6, 7, 8, 10])