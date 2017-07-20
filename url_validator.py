import re
import requests

# Basic url validator
# to do: specify url validation regex further and/or handle errors better

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
        return check_request_status(url)
    else:
        return None

def validation_message(response):
    if response == None:
        return "Your URL is invalid. Please enter a valid url."
    elif response == 200:
        return "Your URL is formatted correctly and returned a 200 status code."
    else:
        return "Your URL is formatted correctly but returned status code {}.".format(response)

def run_url_checker():
    """Get user input url and check validity"""
    print("Welcome to the URL validator.")
    url_input = input("Please enter a URL: ")
    print("Checking URL validity.")
    response = check_url_validity(url_input)
    print(validation_message(response))


run_url_checker()
