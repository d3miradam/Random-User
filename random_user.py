import requests

url = "https://randomuser.me/api/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(" ")
    print("RANDOM USER CREATER")
    print("="*36)
    print(" ")
    print("NAME : "+data["results"][0]["name"]["title"] + " " + data["results"][0]["name"]["first"] + " " + data["results"][0]["name"]["last"]) # name
    print(" ")

    birthdayText = data["results"][0]["dob"]["date"]                                    #
    letter = "T"                                                                        #
    birthdayclear = birthdayText.partition(letter)[0]                                   #    birthday
    birthdayList = birthdayclear.split("-")                                             # 
    birthday = birthdayList[2] +"/"+ birthdayList[1] +"/"+ birthdayList[0]              #
    print("BIRTHDAY : " + birthday)           
    print(" ")                                            

    print("EMAIL : "+data["results"][0]["email"]) # email
    print(" ")
    print("USERNAME : "+data["results"][0]["login"]["username"])       #username
    print(" ")
    print("PASSWORD : "+data["results"][0]["login"]["salt"])           #password
    print(" ")
    print("PROFIL IMAGE : "+data["results"][0]["picture"]["large"])         #image
    print(" ")


else:
    print("Something went wrong please try again later")

