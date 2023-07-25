# Amazon_Price_Tracker  
## Amazon Price Tracker  ![Python version](https://img.shields.io/badge/python-3.x-blue.svg)     
  
  The Amazon Price Tracker is a Python script that allows you to track the price of a specific product on Amazon and get email alerts when the price drops below your desired value. This tool is designed to help you stay informed about price changes and make informed purchasing decisions.    ### Features  -  Track the price of any Amazon product using its URL.  Receive email alerts when the product price drops to the specified value.  Easy-to-use interface with user-friendly prompts.    

### How It Works   

1. Run the script, and it will prompt you to enter the URL of the Amazon product you want to track.
2. Next, provide your email address and password (for Gmail users, an app password may be required).
3. The script will fetch the product's current price from Amazon and display it to you.
4. Enter the price at which you want to be alerted via email.
5. If the product's price drops below or equals your specified price, you will receive an email notification with the product details and URL.


### Installation and Setup   

1. Clone the repository to your local machine using Git.
2. Install the required Python libraries by running: `pip install requests beautifulsoup4 lxml`.
3. Navigate to the project directory and run the script: `python amazon_price_tracker.py`.

### Note on Security    

Please avoid hardcoding your email password directly in the script for security reasons. Instead, consider using environment variables or other secure methods to store and retrieve sensitive information.    

### Compatibility   

The Amazon Price Tracker script is written in Python 3.x and should work on any platform supporting Python.  

### Dependencies    

[requests](https://pypi.org/project/requests/): A library for sending HTTP requests.  
[beautifulsoup4](https://pypi.org/project/beautifulsoup4/): A library for parsing HTML and XML documents.  
[lxml](https://pypi.org/project/lxml/): A library for processing XML and HTML.    

### License  

This project is licensed under the [MIT License](LICENSE).    

### Contributions    

Contributions to this project are welcome. Feel free to open issues or pull requests if you find any bugs or have suggestions for improvements.   

### Disclaimer    

This script is intended for personal use only and should not be used for any commercial purposes or violate Amazon's terms of service.  Happy price tracking!
