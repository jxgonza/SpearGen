# SpearGen
### About 
SpearGen is a spear phishing email generator that takes in a user email and a link payload. With the use of Selenium, it iterates through 8 websites to determine if there is an account associated with the email given. When the testing is completed, the program creates an HTML email file for the service or website that the email has an acount associated with it. These HTML files contain the payload provided and are allocated into a created folder named with the user email. 
 

### Requirements
> *Have these downloaded on your system before continuing:*

* [Python 3.10](https://www.python.org/downloads/)
* [Selenium 4.5](https://www.geeksforgeeks.org/how-to-install-selenium-in-python/)
* [MongoDB Docker container](https://www.howtogeek.com/devops/how-to-run-mongodb-in-a-docker-container/)
* [Google Chrome](https://www.google.com/chrome/) & its according [chromedriver](https://chromedriver.chromium.org/downloads)

### What to change?
`user_email = [insert email]`

`bad_link = [insert link]`

`client = pymongo.MongoClient([docker container adress])`

### Current Sites
* Facebook
* Instagram
* Snapchat
* LinkedIn
* Netflix
* Shopify
* Adobe
* Twitter

### Adding Sites
If you wish to include a website or service, follow the format on mongo-setup.py. 

### Credits
I would like to thank Dr. Plante for the guidance and direction throughout the project.
