import os.path
from os import path

def main():
    AskInfo();

def AskInfo():
    checkpoint="askinfo"
    whichoption= int(input("1-Create new file\n"
                           "2-Search for an existing file\n"
                           "Select an option by typing 1 or 2: "));
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich,pointcheck):
    match(pointcheck):
        case 'askinfo':
            if(ord(str(optionwhich)) < 49 or ord(str(optionwhich)) > 50):
                print("Incorrect response. Type 1 or 2")
                AskInfo();
            else:
                print("You have selected wisely");
        case default:
            print("Houston...we have a problem");

if __name__ == "__main__":
    main();

