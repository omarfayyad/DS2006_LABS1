import random

def rollD4():
    """Roll a 4-sided dice."""
    return random.randint(1, 4)

def rollD6():
    """Roll a standard 6-sided dice."""
    return random.randint(1, 6)

def rollD8():
    """Roll an 8-sided dice."""
    return random.randint(1, 8)

def rollD12():
    """Roll a 12-sided dice."""
    return random.randint(1, 12)

def rollD20():
    """Roll a 20-sided dice."""
    return random.randint(1, 20)

def rollD100():
    """Roll a 100-sided dice."""
    return random.randint(1, 100)

# Example usage:
if __name__ == "__main__":
    input("Press Enter to roll a d4...")
    print("You rolled a", rollD4())
    
    input("Press Enter to roll a d6...")
    print("You rolled a", rollD6())
    
    input("Press Enter to roll a d8...")
    print("You rolled a", rollD8())
    
    input("Press Enter to roll a d100...")
    print("You rolled a", rollD100())
    
    input("Press Enter to roll a d12...")
    print("You rolled a", rollD12())
