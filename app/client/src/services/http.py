import http.client as request
import json

class HTTP:
    """
    Library to handle HTTP Request based on a RESTful approach
    """

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.headers = {
            "Content-type": "application/json"
        }
    
    def parse(self, rsp):
        """
        It parses the data property to return an object from the json response

        Args:
            rsp (dict): {status: (dict), data: (string)}
        
        Returns:
            dict: {status: (dict), data: (dict, list)}
        """
        
        try:
            rsp["data"] = json.loads(rsp["data"])
        except:
            rsp["data"] = {}

        return rsp
    
    def get(self, route):
        """
        Process a GET request to a route in the endpoint

        Args:
            route (str): Route to append in the endpoint
        
        Returns:
            dict: The result of the HTTP Request
        """
        rsp = {
            "res": None,
            "data": []
        }

        conn = request.HTTPConnection(self.endpoint)
        try:
            conn.request("GET", route)
            res = conn.getresponse()
            rsp["data"] = res.read()
            rsp["status"] = {
                "code": res.status,
                "desc": res.reason
            }
        except:
            rsp["status"] = {
                "code": 503,
                "desc": "Service Unavailable"
            }

        conn.close()
        return self.parse(rsp)
    
    def post(self, route, params={}, headers={}):
        """
        Process a POST request to a route

        Args:
            route (str): Route to append in the endpoint
            params (dict): Data to be send in the post as a JSON
            headers (dict): Hearders as a key<value> pair
        
        Returns:
            dict: The result of the HTTP Request
        """
        reqHeaders = self.headers.copy()
        reqHeaders.update(headers)
        conn = request.HTTPConnection(self.endpoint)
        rsp = {
            "status": None,
            "data": None
        }

        try:
            conn.request("POST", route, json.dumps(params), reqHeaders)
            res = conn.getresponse()
            rsp["data"] = res.read()
            rsp["status"] = {
                "code": res.status,
                "desc": res.reason
            }
        except:
            rsp["status"] = {
                "code": 503,
                "desc": "Service Unavailable"
            }

        conn.close()
        return self.parse(rsp)
    
    def put(self, route, params={}, headers={}):
        """
        Process a PUT request to a route

        Args:
            route (str): Route to append in the endpoint
            params (dict): Data to be send in the post as a JSON
            headers (dict): Hearders as a key<value> pair
        
        Returns:
            dict: The result of the HTTP Request
        """
        reqHeaders = self.headers.copy()
        reqHeaders.update(headers)
        conn = request.HTTPConnection(self.endpoint)
        rsp = {
            "status": None,
            "data": None
        }

        try:
            conn.request("PUT", route, json.dumps(params))
            res = conn.getresponse()
            rsp["data"] = res.read()
            rsp["status"] = {
                "code": res.status,
                "desc": res.reason
            }
        except:
            rsp["status"] = {
                "code": 503,
                "desc": "Service Unavailable"
            }
        
        conn.close()

        return self.parse(rsp)
    
    def delete(self, route):
        """
        Process a DELETE request to a route in the endpoint

        Args:
            route (str): Route to append in the endpoint
        
        Returns:
            dict: The result of the HTTP Request
        """
        rsp = {
            "res": None,
            "data": None
        } 

        conn = request.HTTPConnection(self.endpoint)
        try:
            conn.request("DELETE", route)
            res = conn.getresponse()
            rsp["data"] = res.read()
            rsp["status"] = {
                "code": res.status,
                "desc": res.reason
            }
        except:
            rsp["status"] = {
                "code": 503,
                "desc": "Service Unavailable"
            }

        conn.close()
        return self.parse(rsp)
