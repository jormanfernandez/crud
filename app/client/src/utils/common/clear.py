import os
"""
It clears the console in case the program is running in a CLI

Args:
    None

Returns:
    None
"""
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')