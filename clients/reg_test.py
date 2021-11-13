import requests
from pprint import pprint

def client():
    credentials = {
        'username':'rest_test_userxx',
        'email':'rest_test_user@test.co',
        'password1':'test123.',
        'password2':'test123.'
    }
    response=requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials,
        )
    
    print('Status Code:', response.status_code)
    
    response_data = response.json()
    
    pprint(response_data)
    
if __name__ == '__main__':
    client()
        