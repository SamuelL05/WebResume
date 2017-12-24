#Program created by Samuel R Leach
#Program release date:
#DOODAD MANUFACTURING COMPANY JUNE PAYROLL
#Gathers employee information such as name, hours worked,
#and payrate. Will then display calculated totals.

#inputData function referred to as function "1".
#computeData function referred to as function "2".
#displayPay function referred to as function "3".
#exitProg function referred to as function "4".



#Module will be used to support the closing of program in function "4"
import os


#Primary employee information list. All info gathered from function "1" will
#go here. emp_name, pay_rate, hours_worked. 
WORKER = []

#Secondary list created in function "2" to assist with the completion of
#employee computations. Will only hold "name" 
NAME_LIST = []

#Secondary list created in function "2" to assist with the completion of
#employee computations. Will only hold "emp_rate" 
RATE_LIST = []

#Secondary list created in function "2" to assist with the completion of
#employee computations. Will only hold "hours" 
HOURS_LIST = []

#Secondary list created in function "2" to assist with the completion of
#employee computations. Will only hold "emp_pay and total". depending on
#employee's over time status. 
GROSS_LIST = []

#Accumulator used in calculations of function "2". Function "1" add's to
#This value every time an employee is appended to WORKER.
TOTAL_WORKER = 0

#Sentinel used to reset computations of function "2" to help eliminate
#The possibility of double information. 
RUN_CHECK = 0

#Sentinel used to bypass input instructions attached to main menu" used to
#shorten the amount of print displayed after each run of the main function. 
MAIN_RUN = 0


def main():
    
    #Calling global sentinel 
    global MAIN_RUN

    #Sentinel "if" check to determine is instructions should be displayed.
    if MAIN_RUN >= 1:

        print()
        print('What would you like to accomplish?')
        print()
        print(' 1. Input employee information.', '\n',
                '2. Compute pay for all employees.', '\n',
                '3. Display payroll report.', '\n',
                '4. Exit Program.')
        print()

    else:
        
        print()
        print('What would you like to accomplish?')
        print()
        print(' 1. Input employee information.', '\n',
                '2. Compute pay for all employees.', '\n',
                '3. Display payroll report.', '\n',
                '4. Exit Program.')
        print()

        print('Please use the numeric characters' 
                ' infront', '\n', 'of the options to make a' 
                ' selection', '\n',
                "(ex: '1' means 'Input employee information')", sep='')
        print()

        #Sentinel value will be changed to + 1 later in menu code.
        #No other function will change this value again.



    #Get user selection
    user_selection = input('Enter selection here: ')

    #Series of loops to determine validity of input
    try:
        
        if str(user_selection) == '' or str(user_selection.isdigit()) == False:
            
            print()
            print("Please use numeric character's.")
            print()
        
            while user_selection == '' or user_selection.isdigit() == False:
                user_selection = str(input("Please re-enter selection: "))
        
        elif int(user_selection) > 4:
            
            print()
            print("Please use 1 - 4 in numeric form.")
            print()
        
            while int(user_selection) >= 5:
                user_selection = input("Please re-enter selection: ")

        else:

            user_selection = str(user_selection)

    #Used to control loop failure. Will call main function if fails
    except:

        main()

    #Setting selection as a string value to ensure the next "if" statement
    #is able to read input properly.
    user_selection = str(user_selection)        


    #Sentinel is changed
    MAIN_RUN += 1


    #Ensures user is sent to the correct function.   
    if user_selection == '1':
        #Will send to function "1"
        inputData()

    elif user_selection == '2':
        #Will send to function "2"
        computePay()

    elif user_selection == '3':
        #WIll send to function "3"
        displayPay()

    elif user_selection == '4':
        #Will send to function "4"
        exitProg()

    else:
          #If all else fails. Recall main function.      
        main()



def inputData():

    #Calling global WORKER list and TOTAL_WORKER accumulator.
    global TOTAL_WORKER
    global WORKER


    #used to control multiplier 
    time_and_half = 1.5

    #local variables will later be turned into numerical values by program
    #to determine over time rate and hours over 40.
    over_time_rate = 0
    pay_rate = 0
    hours_worked = 0

    #Extra line in prog
    print()
    
    
    #Acquire employee name and check that something was entered.
    #Did not use any other validity check due to some names containing
    #special characters. Also, for instances of double names, that ability
    #To distinguish between the two.
    emp_name = input("Please enter the employee's name: ")

    if emp_name == '':

        print()

        while emp_name == '':

            emp_name = input("Please re-enter the employee's name: ")

        else:

            emp_name = emp_name

    print()
  


    #Hourly pay rate loop used to determine the validity of the input.
    pay_rate = str(input("Please enter " + emp_name + "'s" +
                        " pay rate: "))

    #Will proct if "pay_rate" is equal to nothing to is not a digit.        
    if pay_rate == '' or pay_rate.isdigit() == False:
            
        print()
        print("Please use numeric character's.")
        print()

        #User will remain in loop until program is given correct input        
        while pay_rate == '' or pay_rate.isdigit() == False:
            pay_rate = str(input("Please re-enter " + emp_name + "'s" +
                        " pay rate: "))

    #Checks to see if pay rate is higher then 0.         
    elif int(pay_rate) < 0:
            
        print()
        print("Please use a value higher then or equal to 0.")
        print()

        #User will remain in loop until "pay_rate" is higher then 0. 
        while int(pay_rate) < 0:
            pay_rate = input("Please re-enter " + emp_name + "'s" +
                        " pay rate: ")

    else:

        #After input passes both loops, then "pay_rate" is defined as a integer
        #For later checks.
        pay_rate = int(pay_rate)

    #Incase the first input circumvents both loops. "pay_rate" is defined as
        #integer.
    pay_rate = int(pay_rate)
    print()
    



    #Acquire user input for the amount of hours worked by employee     
    hours_worked = str(input("Please enter " + emp_name + "'s" +
                        " hours worked: "))

     #If input is equal to nothing or is not a digit. User will enter validation
    #loop to acquire correct value. 
    if hours_worked == '' or hours_worked.isdigit() == False:
            
        print()
        print("Please use numeric character's.")
        print()
        
        while hours_worked == '' or hours_worked.isdigit() == False:
            hours_worked = str(input("Please re-enter " + emp_name + "'s" +
                        " hours worked: "))

    #Will check to ensure input is greater then 0. If not user will enter loop.        
    elif int(hours_worked) < 0:
            
        print()
        print("Please use a value higher then or equal to 0.")
        print()
        
        while int(hours_worked) < 0:
            hours_worked = input("Please re-enter " + emp_name + "'s" +
                        " hours worked: ")
    else:

        #Assigns "hours_worked" as an integer value.
        hours_worked = int(hours_worked)

    #incase the first input was correct, it is also assigned as an integer
        #for later calculations.
    hours_worked = int(hours_worked)
    print()


    #Check to see if employee is accumulating over time hours and the pay rate
    #for those hours
    if hours_worked > 40:

        over_time_hours = hours_worked - 40

        over_time_rate = pay_rate * time_and_half

        over_time_pay = over_time_hours * over_time_rate

    #If "hours_worked" is less then 40, value will remain unchanged. It is also
    #set as an integer value for later calculations
    else:

        pay_rate = int(pay_rate)


    #Display message prior to check to determine if information gathered by user
    #was entirely correct.
    #First message will only display if "hours_worked" is greater then 40. 
    if hours_worked > 40:
    
        print('!This employee is recieving over time pay!')
        print()
        print('Is this information correct?')
        print('The employee is: ',emp_name,'\n',
              "Employee's standard hourly rate is: ",pay_rate,'\n',
              "The over time rate is: ",over_time_rate,'\n',
              "Total hour's worked is: ",hours_worked,'\n',
              "Hour's worked during over time rate: ",
              over_time_hours,sep='')

    else:
        
        print('Is this information correct?')
        print('The employee is: ',emp_name,'\n',
              'The pay rate is: ',pay_rate,'\n',
              "Total hour's worked is: ",hours_worked, sep='')

    print()




    #Program will then ask user if information displayed last was correct.
    #Input will then be passed through a potential loop if it is not equal to
    #"y" or "n".
    check = str(input("(y = yes / n = no): "))

    #input is changed to a lowercase for loop check purposes. Just incase user
    #provided the program with a capital "y" or "n".
    check = check.lower()

    while check != 'y' or check != 'n' or check.isalpha() == False:

        #If check is "y" or correct, information gathered previously will be
        #added to the global list WORKER.
        if check == 'y':
                
            print()
            print('Employee information saved.')
            TOTAL_WORKER += 1
            WORKER.append(emp_name)
            WORKER.append(pay_rate)
            WORKER.append(hours_worked)
            main()

        #If check is "n" or incorrect, information is not added to WORKER and
        #main function is called to reset fields and allow for re-entry.
        elif check == 'n':
                
            print()
            print('Program will restart: Information discarded')
            main()

        else:

            check = input("Please re-enter: ")



def computePay():

    #Calling global Lists and sentinels prior to computations
    global NAME_LIST
    global RATE_LIST
    global HOURS_LIST
    global GROSS_LIST
    global RUN_CHECK

    #Local accumulators used to assist in computations
    name_index = 0
    pay_index = 1
    hours_index = 2
    gross_index = 0

    
    


    #if global sentinel "RUN_CHECK" is != to 0, program will enter a loop that
    #removes information that was previously stored in associated global lists.
    #information stored in these lists will only be changed by this particular
    #function. 
    if RUN_CHECK == 1:
   
        loop_index = 0

       #Multiple loops used to remove information in each list.          
        while loop_index < len(NAME_LIST):
            del NAME_LIST[loop_index]
            loop_index += 1

        #loops use the samue "loop_index" so it must be reset after each use.
        loop_index = 0

        while loop_index < len(RATE_LIST):
            del RATE_LIST[loop_index]
            loop_index += 1

        loop_index = 0

        while loop_index < len(HOURS_LIST):
            del HOURS_LIST[loop_index]
            loop_index += 1

        loop_index = 0

        while loop_index < len(GROSS_LIST):
            del GROSS_LIST[loop_index]
            loop_index += 1

        #Once program reaches this point, the associated global lists have been
        #cleared and the global sentinel "RUN_CHECK" is reset to 0.
        RUN_CHECK = 0

        #function "2" is recalled so user will still see information displayed
        #normally by this function. Otherwise, if program was to continue from
        #this point, it would display empty lists.
        computePay()

    #Program will check "WORKER" to see if information has been added to global
    #list. If "WORKER" is != 0, program will begin reading information from list
    #and adding it to global "NAME_LIST", "RATE_LIST", "HOURS_LIST",
    #and "GROSS_LIST"
    elif len(WORKER) != 0:

        RUN_CHECK = 1
       
        while name_index < len(WORKER):
            name = WORKER[name_index]
            NAME_LIST.append(name)
            name_index += 3
        
        while pay_index < len(WORKER):
            pay_rate = WORKER[pay_index]
            RATE_LIST.append(pay_rate)
            pay_index += 3

        while hours_index < len(WORKER):
            hours = WORKER[hours_index]
            HOURS_LIST.append(hours)
            hours_index += 3

        try:

            while gross_index < len(NAME_LIST):
                emp_rate = RATE_LIST[gross_index]
                emp_hours = HOURS_LIST[gross_index]
            
                if emp_hours > 40:
            
                    ot_pay_rate = emp_rate * 1.5
                    ot_hours = emp_hours - 40
                    ot_pay = ot_pay_rate * ot_hours
                    total_pay = ot_pay + (emp_rate * 40)
                    GROSS_LIST.append(total_pay)
                    gross_index += 1
            
                else:

                    emp_pay = emp_rate * emp_hours
                    GROSS_LIST.append(emp_pay)
                    gross_index += 1
                    
        except:
            
            print()
            print('Program Failed: will redirect to main menu')

        #If program was succesful in acquiring all information from "WORKER"
        #program will then display the newly created lists.
        print()
        print('Employee pay calculated.')
        print()
        print(NAME_LIST, ' - ', "Employee Name's")
        print(RATE_LIST, ' - ', "Employee Pay Rate's")
        print(HOURS_LIST, ' - ', "Employee Hour's")
        print(GROSS_LIST, ' - ', "Employee Gross")

    else:

        #Other wise program will inform user that there is no information in
        #"WORKER" and recommends adding information prior to selecting this
        #function
        print()
        print("Please add employee information" \
              " prior to selecting option '2'")


    #After all code has been completed, function will call main.
    main()


def displayPay():

    #Function "3" will first call global list "WORKER" and global accumulator
    #"TOTAL_WORKER", these will be used to correctly display information
    global TOTAL_WORKER
    global WORKER



    #"if" check to ensure there is information present in "WORKER", if there
    #if not, program will redirect user to main.
    if len(WORKER) != 0:

        #Variables used to recalculate total pay.
        index = 0
        worker_index = 0
        time_and_half = 1.5

        #Heading for information display
        print()
        print('DOODAD MANUFACTURING COMPANY JUNE PAYROLL')
        print('EMPLOYEE NAME' + '\t' + 'HOURS WORKED'
                + '\t' + 'PAY RATE' + '\t' + 'GROSS PAY')
        print('-------------' + '\t' + '------------'
                + '\t' + '--------' + '\t' + '---------')


        #"worker_index" is a local accumulator used to fufil calculations        
        while worker_index < TOTAL_WORKER:

            if worker_index >= 1:

                index += 3

            else:

                index = 0
                
            worker_name = WORKER[index]
            worker_rate = WORKER[index + 1]
            worker_hours = WORKER[index + 2]

            worker_hours = int(worker_hours)

            if worker_hours > 40:

                ot_pay_rate = worker_rate * 1.5
                ot_hours = worker_hours - 40
                ot_pay = ot_pay_rate * ot_hours
                ot_total_pay = ot_pay + (worker_rate * 40)

                worker_hours = str(worker_hours)

                #After program succesfully calculates list information. the
                #program will print it.
                print(worker_name, '\t', worker_hours, '\t', worker_rate,
                      '\t', ot_total_pay)

            else:

                gross_pay = worker_rate * worker_hours 
                print(worker_name, format(worker_hours, '18.1f'),
                      format(worker_rate, '15.2f'),
                      format(gross_pay, '15.2f'))
            #Once the program has displayed the information for that particular
            #employee, whether they acquired over time or not. "worker_index"
            #will have one added to the overall total.
            worker_index += 1

    else:

        #If there is no information present in "WORKER" this is the message
        #recieved 
        print()
        print("Please add employee information prior" \
              " to selecting option '3'")

    #After all code completes, main is called.
    main()

            
def exitProg():

    #Code to kill the command prompt program.
    os.system('TASKKILL /F /IM py.exe')




#First and last main call.
main()
