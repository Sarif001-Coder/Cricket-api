# Cricket API 
This project is a simple Python application that fetches data from a website using an API. It primarily relies on the requests library to perform GET requests and process responses.
#

## Requirements
+ Python => 3.14.0 or any LTS version is fine
+ requests library
```
$ pip install requests 
```
#

## API Reference
https://www.allthingsdev.co/

signin here and will get a free cricket api with json as a output.

## Structure

````
├── main.py/           # main file
└── cric_api.py/      # API handling file
````

### Writing Tests
```Python
def api_info_check():
try:
         responseAPI = requests.get(authurl, headers=HEADERS, timeout=5)
         if responseAPI.status_code == 200:
             return print("API is working")
         else:
             print("API not working")
     except requests.exceptions.RequestException as e:
         return print("Wrong API details")
```



[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Made with ❤️ by [Sarif Ali](https://github.com/username)**


