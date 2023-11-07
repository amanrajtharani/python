email = input("Enter your email : ")
for i in range(0,len(email)):
    if not ( email[i] == '@' or email[i]=='.'):
        print ("Invalid Email")
        break
    else:
        break