# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1790796
# Date: 17/04/2020
valid_inputs = [0,20,40,60,80,100,120]
pass_mark,defer_mark,fail_mark = 0,0,0
print("                     │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│")
print("—————————————————————│ Welcome to Student Version │—————————————————————")
print("                     │____________________________│")
print("             _______________│______________│_______________ ")
print("            │Credits are in the range 0,20,40,60,80,100,120│")
print("             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n")

def start():# collect the credits 
    global pass_mark,defer_mark,fail_mark
    def input_credits(level):
        while True:
            try:
                marks = int(input("♦ Enter " + level + " Credits : "))
                if marks in valid_inputs:
                    return marks # level value return to pass_mark or defer_mark or fail_mark
                else:
                    print("\n\t**** Range Error! ****\n")
                    continue
            except ValueError:
                print("\n\t**** Integers Required! ****\n")
                continue
    pass_mark = input_credits("Pass") # input_credits functaion has a parameter and it assign to string.
    defer_mark = input_credits("Defer")
    fail_mark = input_credits("Fail")
    
def decision():
    if (pass_mark + defer_mark + fail_mark) != 120:  # check the credits total
        print("\n\t**** Total Error! ****\n")
        start()
        decision()
    else:  # check the Progression Outcome
        if pass_mark == 120:
            print("\n\t>>> Progress <<<\n")
        elif pass_mark == 100:
            print("\n\t>>> Progress – module trailer <<<\n")
        elif pass_mark <= 80 and fail_mark <= 60:
            print("\n\t>>> Do not progress – module retriever <<<\n")
        else:
            print("\n\t>>> Exclude <<<\n")

start() # Call the start function to start the program
decision() # Call the decision function to check outcome

print("                           │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│  ")
print("___________________________│    Thank You!   │__________________________")
print("                           │ Have a Nice Day!│                     ")
print("                           │_________________│")

