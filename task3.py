import random

def email_validation(email,domain):
    if email.count("@")==1:
        if len(email[:email.index("@")])>2:
            if email[email.index("@")+1:]==domain:
                return True
    
    return False
def name(email):
    return email[:email.index("@")]

def is_in_word(sent,word):
    if word.lower() not in sent.lower():
        return False
    else:
        return True

error=[False,False,False,False,False,True,False,False,False,False]
names=["john","harry","james"]
exit_statements=["bye","exit","see you later"] 
no_reply=["hmm","Tell me more","I didn't get you","sorry","can u elaborate"]
print("Welcome to Pop Chat \nOne of our operators will be pleased to help you today.\n")
email=input("Please enter your Poppleton email address:")
end=False
if(email_validation(email,"pop.ac.uk")):
    print("Hi, {}! Thank you, and Welcome to PopChat!".format(name(email)))
    print(f"My name is {random.choice(names)}, and it will be my pleasure to help you.")
    while True:
        sent=input("Enter string:")
       
        if (random.choice(error)):
            print("Network error")
            end=True
        for  word in exit_statements:
            if word in sent.lower():
                end=True
        if end==True:
            break
        if(is_in_word(sent,"library")):
            print("The library is closed today.")
        elif(is_in_word(sent,"WiFi")):
            print("WiFi is excellent across the campus.")
        elif is_in_word(sent,"deadline"):
            print( "Your deadline has been extended by two working days.")
        else:
            print(random.choice(no_reply))
            
else:
    print("This email is not valid")