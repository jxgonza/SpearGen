import pymongo

# Connection to MongoDB docker container.
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["projdb"]
websites = db["websites"]


# Each website follows the following format.
  # 'title' : '[Name of the Website'
  # 'url' : '[url of the forgot password section]'
  # 'email_element' : '[XPATH of the email input on the site]'
  # 'button_element' : '[XPATH of the submit or search button on the site]'
  # 'verification_method' : '[url or error]'
  # If you go with error, you have to include:
  #   'error_element': '[XPATH of error element]'

websites_list = [
  { "title": "Facebook",
   "url": "https://www.facebook.com/login/identify/?ctx=recover&from_login_screen=0",
   "email_element": '//*[@id="identify_email"]',
   "button_element": '//*[@id="did_submit"]',
   "verification_method": "url"
   },
  { "title": "Instagram",
   "url": "https://www.instagram.com/accounts/password/reset/",
   "email_element": 'cppEmailOrUsername',
   "button_element": "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[2]/div/div/div/div/div[5]/button",
   "verification_method": "url"
   },
  { "title": "Snapchat",
   "url": "https://accounts.snapchat.com/accounts/password_reset_request",
   "email_element": '//*[@id="emailaddress"]',
   "button_element": "//button[contains(text(), 'Submit')]",
   "verification_method": "error",
   "error_element": '//*[@id="error_message"]'
   },
  { "title": "LinkedIn",
   "url": "https://www.linkedin.com/uas/request-password-reset?trk=homepage-basic_signin-form_forgot-password-link",
   "email_element": '//*[@id="username"]',
   "button_element": '//*[@id="reset-password-submit-button"]',
   "verification_method": "error",
   "error_element" : "/html/body/div[1]/main/div[1]/div[1]/span"
   },
  { "title": "Netflix",
   "url": "https://www.netflix.com/LoginHelp",
   "email_element": '//*[@id="forgot_password_input"]',
   "button_element": "//button[contains(text(), 'Email Me')]",
   "verification_method": "error",
   "error_element": '//*[@id="appMountPoint"]/div/div[3]/div[1]/div/div[1]/div[2]'
   },
  { "title": "Shopify",
   "url": "https://accounts.shopify.com/lookup?rid=5775c5f5-838d-467c-b548-49f2986d5335",
   "email_element": '//*[@id="account_email"]',
   "button_element": '//*[@id="body-content"]/div[2]/div/div[2]/div/div/div[2]/div/form/button',
   "verification_method": "error",
   "error_element": "//h1[contains(text(), 'Create a Shopify ID')]"
   },
  { "title": "Adobe",
   "url": "https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fadobedotcom2%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523old_hash%253D%2526from_ims%253Dtrue%253Fclient_id%253Dadobedotcom2%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cgnav%252Cread_organizations%252Cadditional_info.projectedProductContext%252Cadditional_info.roles%26state%3D%257B%2522ac%2522%253A%2522%2522%252C%2522jslibver%2522%253A%2522v2-v0.36.0-1-g835e663%2522%252C%2522nonce%2522%253A%25223393511258278481%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=adobedotcom2&scope=AdobeID%2Copenid%2Cgnav%2Cread_organizations%2Cadditional_info.projectedProductContext%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2Fadobedotcom2%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.adobe.com%252F%2523old_hash%253D%2526from_ims%253Dtrue%253Fclient_id%253Dadobedotcom2%2526api%253Dauthorize%2526scope%253DAdobeID%252Copenid%252Cgnav%252Cread_organizations%252Cadditional_info.projectedProductContext%252Cadditional_info.roles%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522%2522%252C%2522jslibver%2522%253A%2522v2-v0.36.0-1-g835e663%2522%252C%2522nonce%2522%253A%25223393511258278481%2522%257D&state=%7B%22ac%22%3A%22%22%2C%22jslibver%22%3A%22v2-v0.36.0-1-g835e663%22%2C%22nonce%22%3A%223393511258278481%22%7D&relay=7fda9398-b42b-41fa-855b-33913d5a6f7f&locale=en_US&flow_type=token&idp_flow_type=login&ab_test=signin-get-help&s_p=apple%2Cgoogle%2Cfacebook#/",
   "email_element": '//*[@id="EmailPage-EmailField"]',
   "button_element": '//*[@id="EmailForm"]/section[2]/div[2]/button',
   "verification_method": "error",
   "error_element": '//*[@id="EmailForm"]/section[1]/label'
   },
  { "title": "Twitter",
   "url": "https://twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D",
   "email_element": 'username',
   "button_element": "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div",
   "verification_method": "error",
   "error_element": '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
   }
]

websites.insert_many(websites_list)
