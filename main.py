from grabAccessToken import grab_access_token
from GuiHandler import gui


def main():
    #Assign the access_token 
    access_token = grab_access_token()
    
    #If there is an access token
    if access_token:
         #Create the GUI!
         gui(access_token)
    else:
         print("Token aquire failed")

if __name__ == '__main__':
    main()