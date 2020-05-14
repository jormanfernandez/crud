from utils.commons.similar import similar

def search(data, params = {}, ratio = 0.7):
    """
    It looks in the data parameter the keys that are send in the params parameter using the SequenceMatcher.
    This uses the approximation in order to simulate a "LIKE" option in a SQL database.

    Args:
        data (dict): data to be looked
        params (dict): Parameters to be search with key<value>
        ratio (int): The exactitud in which the data shouldd be allowed to match
    
    Returns:
        dict: If the data match, it will be returned
        boolean: If the data does not match, it will return False
    """
    itMatch = 0.0

    for key in params.keys():
        try:
            itMatch = itMatch + similar(data[key], params[key])
        except:
            itMatch = itMatch + 0.0

    itMatch = itMatch / len(params.keys())

    if itMatch >= ratio:
        return data
    else:
        return False