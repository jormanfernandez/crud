import falcon 
from utils.logger import Log 

class EngineError(Exception):
    """
    It handles falcon Errrors when the helpers can't

    Args:
        Exception (Exception)
    """

    @staticmethod
    def handle(ex, req, resp, params):
        """
        Helper to handle the error when the route helpers can't

        Args:
            ex (any): No info
            req (Falcon HTTP Request): Request received by the server
            resp (Falcon HTTP Response): Response constructed by the server
            params (any): Other params
        
        Returns:
            None
        """
        desc = f"""
        An error has occurred. Your request failed.
        {ex}
        """

        Log(desc, level=3, file="engine")

        raise falcon.HTTPError(falcon.HTTP_725, 'Request Error', desc)