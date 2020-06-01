"""
Here is where we developed code to get inputs from users to specify river location,
and set appropriate river location and weather station variables.
Additionally significant portion of code dedicated to error handling if users input
incorrect data-types, or do not follow printed instructions.

Parker's Python Pals
OCEAN 506
"""
import sys
#Creating the prompt for the user to know which number corresponds to whcich site
print("\n\n\nHello, please specify the river location you would like to view.")
print("Please enter the number of one the following options into the prompt at the bottom of the list:\n")
print("1 = Yakima River")
print("2 = Skagit River at Marbelmount")
print("3 = Skagit River at Mount Vernon")
print("4 = Skykomish River")
print("5 = Sultan River")
print("6 = Middle Fork Snoqualmie River")
print("7 = Stehekin River\n")
#Defining Varibales
RCode=1
WCode=1
good_values=[1,2,3,4,5,6,7]
good_input=False
counter=0
#Doing some error handling to repeat the prompt if the user enters an incorrect value
while good_input==False and counter<10:
        try:
            user_input = int(input('\nPlease Type the Number of the Desired River: '))
            if user_input in good_values:
                good_input=True
                if user_input == 1: #If/when a correct value (within the given range) is given, correct variables will be set.
                    RCode = 12484500
                    WCode = 452505
                    print ("\nYou've chosen Yakima River!")
                elif user_input == 2:
                    RCode = 12181000
                    WCode = 24281 #Seattle Weather Data, see note in print statement
                    print ("\nYou've chosen Skagit River at Marbelmount")
                    print ("NOTE: Specific Weather Data Unavailable, showing weather data from Seattle, WA.")
                elif user_input == 3:
                    RCode = 12200500
                    WCode = 450986
                    print ("\nYou've chosen Skagit River at Mount Vernon! ")
                elif user_input == 4:
                    RCode = 12134500
                    WCode = 24281 #Seattle Weather Data, see note in print statement
                    print("\nYou've chosen Skykomish River!")
                    print ("NOTE: Specific Weather Data Unavailable, showing weather data from Seattle, WA.")
                elif user_input == 5:
                    RCode = 12137800
                    WCode = 24281 #Seattle Weather Data, see note in print statement
                    print("\nYou've chosen Sultan River!")
                    rint ("NOTE: Specific Weather Data Unavailable, showing weather data from Seattle, WA.")
                elif user_input == 6:
                    RCode = 12142000
                    WCode = 24281 #Seattle Weather Data, see note in print statement
                    print("\nYou've chosen Middle Fork Snoqualmie River!")
                    print ("NOTE: Specific Weather Data Unavailable, showing weather data from Seattle, WA.")
                elif user_input == 7:
                    RCode = 12451000
                    WCode = 458059
                    print("\nYou've chosen Stehekin River!")

            else:
                print("\nYour Entry Was Not Recognized\nPlease enter a single number from 1-7 corresponding to the river of interst.")
                counter +=1
#More error handling, prevents red-error if input data-type is incorrect.
        except ValueError:
                print("\nPlease enter a valid input as descibed above.")
                counter += 1
#More error handling, automatically terminates process if input was incorrect after 10 attempts
while good_input==False and counter>=10:
    print('\n\n\nYour entry was incorrect too many times. PROCESS TERMINATING.')
    RCode=None
    WCode=None
    sys.exit('Please re-run command when ready, and follow printed instructions.')



counter2=0
good_input=False
while good_input==False and counter2 < 5:
    try:
        print('\n\nPlease indicate how many past days you would like to view data for (1-60)')
        days=int(input('How many whole days record do you want to plot: '))
        if days>0 and days<61:
            good_input = True
            print('\n\nThank you for your selections, we are gathering your data!')
        else:
            print("\nYour Entry Was Not Recognized\nPlease enter a single number from 1-60.")
            counter +=1
    except ValueError:
        print('\nPlease enter a valid input, following the pinted instructions')
        counter2+=1


while good_input==False and counter2>=5:
    print('\n\n\nYour entry was incorrect too many times. PROCESS TERMINATING.')
    RCode=None
    WCode=None
    days=None
    sys.exit('Please re-run command when ready, and follow printed instructions.')


#Making the codes strings to insert into url in later section.
WCode = str(WCode)
RCode = str(RCode)
TDelta = int(days)
