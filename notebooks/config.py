import os

# Twitter API access tokens go here:
API_Key = ""
API_Key_Secret = ""
Access_Token = ""
Access_Token_Secret = ""
Bearer_Token = ""

# Botometer access token goes here:
RapidAPI_Key = ""

def auth_setup():
    # Twitter API access tokens, same as above:
    auth = {
        'consumer_key': "",
        'consumer_secret': "",
        "access_token" : "",
        "access_token_secret" : "",
        "bearer_token" : "",    
    }

    for key in auth.keys():
        os.environ[key] = auth[key]
        
    return auth