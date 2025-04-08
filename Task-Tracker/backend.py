import json
import os
from datetime import datetime

def mainmenu():
    while True:
        print("************************************")
        print("************ 1)Add task ************")
        print("*********** 2)Update task **********")
        print("*********** 3)Remove task **********")
        print("********** 4)Change status *********")
        print("*********** 5)List tasks ***********")
        print("************   6)Exit   ************")
        print("************************************")

        mminput = input("Please enter a number between 1-6: ")

        try:
            mminput = int(mminput)
            if mminput in [1, 2, 3, 4, 5]:
                print('Choice accepted')
                return mminput
            else:
                print("Invalid input, please enter a number between 1-6")
        except ValueError:
            print("Invalid input, please enter a number")

def addtask():
    with open("file.json",'r') as file:
        data = json.load(file)
    
    userinput = input("Please enter a task to add: ")
    id = 1
    realid = []
    for item in data:
        realid.append(item['ID'])
    while id in realid:
        id += 1
    createdat = datetime.now().strftime("%H:%M:%S")

    data.append(
        {
            "ID": id,
            "Description": userinput,
            "Status": None,
            "Created at": createdat,
            "Updated at": None
        }
    )
    with open("file.json",'w') as file:
        json.dump(data, file, indent=4)

def statuschange():
    while True:
        try:
            idcheck = int(input("Enter ID: "))
        except ValueError:
            print("Invalid input, please enter a number")

        print("************************************")
        print("************* 1)To Do **************")
        print("*********** 2)In-Progress **********")
        print("*************** 3)Done *************")
        print("************************************")

        try:
            choice = input("Choose a number between 1-3: ")

            choice = int(choice)

            with open("file.json",'r') as file:
                data = json.load(file)
            
            
                for item in data:
                    if idcheck == item['ID']:
                        if choice == 1:
                            item["Status"] = "To Do"
                        elif choice == 2:
                            item["Status"] = "In-Progress"
                        elif choice == 3:
                            item["Status"] = "Done"
                with open("file.json",'w') as file:
                    json.dump(data, file, indent=4)
        except ValueError:
            print("Invalid input, please enter a number")



def updatetask():
    try:
        updatedat = datetime.now().strftime("%H:%M:%S")
        idcheck = int(input("Enter ID: "))
    except ValueError:
        print("Invalid input, please enter a number")
    change = input("What would you like to change the description to: ")
    with open("file.json",'r') as file:
        data = json.load(file)
    for item in data:
        if idcheck == item['ID']:
            item["Description"] = change
            item["Updated at"] = updatedat
    with open("file.json", 'w') as file:
        json.dump(data, file, indent=4)

def removetask():
    try:
        idremove = int(input("Input an ID you would like to remove: "))
    except ValueError:
        print("Invalid input, please enter a number")
    emptyarray = []
    with open("file.json",'r') as file:
        data = json.load(file)
    for item in data:
        if item["ID"] != idremove:
            emptyarray.append(item)
    with open("file.json", 'w') as file:
        json.dump(emptyarray, file, indent=4)

def viewtask():
    print("************************************")
    print("********* 1)View all tasks *********")
    print("***** 2)View all complete tasks ****")
    print("*** 3)View all not complete tasks **")
    print("*** 4)View all in-progress tasks ***")
    print("************************************")

    try:
        choice = input("Enter a number between 1-4: ")
        choice = int(choice)
        with open("file.json",'r') as file:
            data = json.load(file)
        
        for item in data:
            if choice == 1:
                print (item ["Description"])
            elif choice == 2:
                if item ["Status"] == "Done":
                    print (item ["Description"])
            elif choice == 3:
                if item ["Status"] == "To Do" or "In-Progress":
                    print (item ["Description"])
            elif choice == 4:
                if item ["Status"] == "In-Progress":
                    print (item ["Description"])
    except ValueError:
        print ("Invalid input, please enter a number")

def main():
    if not os.path.exists('file.json'):
        with open("file.json","w") as file:
            data = json.dump([],file)

    while True:
        mainmenu_choice = mainmenu()
        if mainmenu_choice == 1:
            addtask()
        elif mainmenu_choice == 2:
            updatetask()
        elif mainmenu_choice == 3:
            removetask()
        elif mainmenu_choice == 4:
            statuschange()
        elif mainmenu_choice == 5:
            viewtask()
        elif mainmenu_choice == 6:
            break

if __name__ == "__main__":
    main()