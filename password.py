str_password=input("enter password....")
small_letters="abcdefghijklmnopqrstuvwxyz"
capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters="@&#"
numbers="0123456789"
i=0
while i<len(str_password):
    if small_letters[i] in str_password:
        if capital_letters[i] in str_password:
            if special_characters[i] in str_password:
                if numbers[i] in str_password:
                    print(str_password,"strpng password")
                else:
                    print(str_password,"not str_password")
            else:
                print("enter special character")
        else:
            print("enter any capital letter")
    else:
        print("please enter any small letter")
    i=i+1