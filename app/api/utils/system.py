def isSQL():
    """
    Determine if the program should run with the SQL or NoSQL database.

    Args:
        None
    
    Returns:
        boolean: True if is SQL false with NoSQL
    """
    import sys
    return False if len(sys.argv) > 1 and "nosql" in sys.argv else True