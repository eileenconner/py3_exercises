import re
import requests

# Basic url validator

def check_url_formatting(url):
    """
    Determine if url is properly formatted w/ https protocol.
    Host may be 2-4 sections to accommodate subdomains, top and second-level domains, etc.
    Match: scheme://host/path?query
    """
    return re.match('(https:\/\/)\S+\.\S+(\.\S+)*(\.\S+)*(\/\S+)*(\?\S+)*', url)

def check_request_status(url):
    """Send request to determine validity of request response."""
    request = requests.get(url)
    return request.status_code

def check_url_validity(url):
    """Accept url and pass through steps to determine validity."""
    match = check_url_formatting(url)
    if match:
        response = check_request_status(url)
        if response == 200:
            print("Your url is formatted correctly and returned a 200 status code.")
        else:
            print("Your url is formatted correctly but returned status code {}.".format(response))
        return response
    else:
        print("Please enter a valid url.")
        return None
