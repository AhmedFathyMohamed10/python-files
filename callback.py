import requests

"""
Function to fetch data from a remote server.
"""
def fetch_data(url, callback):
    response = requests.get(url)
    if response.status_code == 200: # Code is successfull
        callback(response.json())

    else:
        print('Error Fetching data: ', response.status_code)

    
def do_something_else(data):
    """
    Callback function to process the fetched data.
    """
    print("Data received:", data)


if __name__ == '__main__':
    url_correct = "https://jsonplaceholder.typicode.com/posts/1"
    url_error = "https://jsonplaceholder.typicode.com/posts/1/sdhniue"
    fetch_data(url_correct, do_something_else)
