import pymongo, os, shutil
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Connection to docker image of mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["projdb"]
websites = db["websites"]
users = db["users"]

# Change this to your email.
user_email = ""

# Declaring dictionary used for results
user_results = {}

def check_loop():
    #This is for headless testing. For some reason Twitter doesn't work with this.
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    # driver = webdriver.Chrome(executable_path=r"./chromedriver", options=op)
    
    # This allows Selenium to interact with the browser
    driver = webdriver.Chrome(executable_path=r"./chromedriver")

    for site in websites.find():
        url = site['url']
        driver.get(url)
        sleep(5)
        # Tries finding the element by XPATH. If that doesn't work, it finds by name.
        try:
            driver.find_element(By.XPATH, site['email_element']).send_keys(user_email)
        except NoSuchElementException:
            driver.find_element(By.NAME, site['email_element']).send_keys(user_email)
        sleep(3)
        driver.find_element(By.XPATH, site['button_element']).click()
        sleep(5)

        if site['verification_method'] == 'url':
            current_url = driver.current_url
            if current_url == url:
                user_results.update({site['title'] : "No"})
            else:
                user_results.update({site['title'] : "Yes"})
            sleep(2)
        elif site['verification_method'] == 'error':
            try:
                driver.find_element(By.XPATH, site['error_element'])
                user_results.update({site['title'] : "No"})
            except NoSuchElementException:
                user_results.update({site['title'] : "Yes"})
            sleep(2)
    driver.quit()             

def email_template():
    # Declaring string variables 
    user_name = user_email.split("@")
    user_name = user_name[0]
    dir_name = user_name + "_EmailTemplates"

    # Change this to your desired payload
    bad_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    # Checks if directory already exists. If it does, it deletes and creates it again.
    if os.path.exists("./"+dir_name):
        shutil.rmtree("./"+dir_name)
        os.mkdir("./"+dir_name)
    else:
        os.mkdir("./"+dir_name)

    # Finds the user_email's results on MongoDB server.
    users_result = users.find_one({"user_email":user_email}, {'_id':0, 'results':1})

    # Iterates through the results
    for name, result in users_result.items():
        # For loop that checks if the results was a 'Yes' or 'No'.
        # If 'Yes', create a tailored email template and save it to the created directory.
        # If 'No', move along.
        for site_title, site_result in result.items():
            if site_result == 'No':
                pass
            else:
                with open('email_templates/'+site_title+'.html', 'r') as temp:
                    tempdata = temp.read()

                tempdata = tempdata.replace('{user_email}', user_email)
                tempdata = tempdata.replace('{user_name}', user_name)
                tempdata = tempdata.replace('{bad_link}', bad_link)

                with open(dir_name+'/'+site_title+'_new.html', 'w') as temp:
                    temp.write(tempdata)
                    # print(tempdata)
        

def main():
    # Checks if there are already results on MongoDB.
    test = users.find_one({"user_email": user_email})

    # If the find returns null, start a new test.
    if test == None:
        print("\n\nThere's no test for this user.\nStarting a new one right now.\n\n")
        check_loop()
        users.insert_many([{"user_email": user_email, "results" : user_results}])
        print('\n--- '+user_email, "had the following results:")
        print('\t', users.find_one({'user_email': user_email}, {'_id': 0, 'results': 1}), '\n')

    # If the find returns True, it gives the user the option to print old results and create new templates
    # or to run a new test.
    else:
        cont = True
        while cont:
            repeat = input("\n--- This email already has a test in our database. \n--- Would you like to print the previous results ('p') or run the check again ('r')?\n\n").lower().replace(" ", "")
            
            if repeat == "p":
                print('\n--- '+user_email, "had the following results:")
                print('\t', users.find_one({'user_email': user_email}, {'_id': 0, 'results': 1}), '\n')
                cont = False
            elif repeat == "r":
                check_loop()
                users.find_one_and_update({"user_email" : user_email}, {'$set': {"results" : user_results}})
                print('\n--- '+user_email, "had the following results:")
                print('\t', users.find_one({'user_email': user_email}, {'_id': 0, 'results': 1}), '\n')
                cont = False
            else:
                print("\n--- Please input 'p' for printing previous results or 'r' to run check again")

    email_template()

   
main()

