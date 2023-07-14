dict={'Name':'Kathir','Age':20,'Gender':'Male'}
print("\nYou Want Add a Element Please Press\t:1")
print("\nYou Want Edit a Element Please Press\t:2")
print("\nYou Want Delete a Element Please Press\t:3")
print("\nYou Want Print a Dictionary Please Press:4")
print("\nYou Want Stop Execution Please Press\t:5")
print("\nWhich Option You Will Be Performed Please Select Above Options:-")
user=int(input("\nEnter Your Option:"))

if user==1:
    key_name=input("Enter Your Adding Key Name in Dictionary:")
    value=input("Enter Your adding Value in Dictionary:")
    dict.update({key_name: value})
    print(dict)
    print("The Element Will Be Added Successfuly")
elif user==2:
    key_name=input("Enter Your Exist Key Name in Dictionary:")
    Value=input("Enter Your Exist Value in Dictionary:")
    for key in dict.items():
        if key==key_name:
            del dict[key]
            new_key_name=input("Enter Your New Key Name in Dictionary:")
            new_value=input("Enter Your New Value in Dictionary:")
            dict.update({new_key_name: new_value})
            print(dict)
            print("The Element Will Be Edit Successfuly")
    if key!=key_name:
        print("Please Enter The Valid Key Name and Values")
elif user==3:
    key_name=input("Which Element You Want Delete in The Dictionary:")
    if key_name in dict:
        del dict[key_name]
        print(dict)
         print("The Element Will Be Deleted Successfuly")
    else:
        key_name!=dict
        print("No Element Found in The Dictionary")
elif user==4:
    print(dict)
elif user==5:
    print("The Program Will Be Terminated Or Execution Will Be Stop")
