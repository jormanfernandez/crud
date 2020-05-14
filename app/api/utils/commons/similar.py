from difflib import SequenceMatcher

def similar(a, b):
    """
    It returns the ratio of similitud between one thing to the other
    
    Args:
        a (Iterable): Any iterable object
        b (Iterable): Any iterable object
    
    Returns:
        int: The ratio of similitud between a and b
    """
    return SequenceMatcher(None, a, b).ratio()
