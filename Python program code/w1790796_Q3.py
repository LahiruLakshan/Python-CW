# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1790796
# Date: 17/04/2020
valid_inputs = [0,20,40,60,80,100,120]
pass_mark,defer_mark,fail_mark = 0,0,0
progress_times,trailer_times,retriever_times,exclude_times = 0,0,0,0
total_times = 0
print("            │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│")
print("————————————│ Welcome to Staff Version-Vertical Histrogram │————————————")
print("            │______________________________________________│")
print("             _______________│______________│_______________ ")
print("            │Credits are in the range 0,20,40,60,80,100,120│")
print("             ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

def start_vertical_histogram():#start in Staff Version-Horizontal Histogram 
    while True:
        print("\n\t◊ Type 'S' to Start Checking Students Results.\n\t◊ Type 'Q' to Check Vertical Histogram and Quit the Program. ")
        enter_input = str(input("Enter your Decision('S'/'Q') : "))
        if enter_input == 'S' or enter_input == 's':
            print()
            start()  # Call the start function to collect the credit level
            decision() # Call the decision function to check outcome
        elif enter_input == 'Q' or enter_input == 'q':
            final_result_vertical_histogram()# call the function for the shows vertical histrogram
            break
        else:
            print("\n\t**** Invalid Input! ****")
            continue
def start():  # collect the credits 
    global pass_mark,defer_mark,fail_mark
    def input_credits(level):
        while True:
            try:
                marks = int(input("♦ Enter " + level + " Credits : "))
                if marks in valid_inputs:  # level value return to pass_mark or defer_mark or fail_mark
                    return marks
                else:
                    print("\n\t**** Range Error! ****\n")
                    continue
            except ValueError:
                print("\n\t**** Integers Required! ****\n")
                continue
    pass_mark = input_credits("Pass")  # input_credits functaion has a parameter and it assign to string.
    defer_mark = input_credits("Defer")
    fail_mark = input_credits("Fail")

def decision():
    global pass_mark,defer_mark,fail_mark,progress_times,trailer_times,retriever_times,exclude_times,total_times
    if (pass_mark + defer_mark + fail_mark) != 120:
        print("\n\t**** Total Error! ****\n")
    else:
        if pass_mark == 120:
            print("\n\t>>> Progress <<<")
            progress_times += 1
        elif pass_mark == 100:
            print("\n\t>>> Progress – module trailer <<<")
            trailer_times += 1
        elif pass_mark <= 80 and fail_mark <= 60:
            print("\n\t>>> Do not progress – module retriever <<<")
            retriever_times += 1
        else:
            print("\n\t>>> Exclude <<<")
            exclude_times += 1
        total_times += 1
            
def final_result_vertical_histogram():# display Vertical Histogram 
    global progress_times,trailer_times,retriever_times,exclude_times
    print()
    print("                        │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│")
    print("————————————————————————│  Vertical Histogram  │————————————————————————")
    print("                        │______________________│\n")
    print("Progress   Trailer   Retriever   Exclude")
    while progress_times + trailer_times + retriever_times +exclude_times != 0:
        if progress_times != 0:
            print("   *       ",end = '')
            progress_times -= 1
        else:
            print("           ",end = '')
        if trailer_times != 0:
            print("   *      ",end = '')
            trailer_times -= 1
        else:
            print("          ",end = '')
        if retriever_times != 0:
            print("    *       ",end = '')
            retriever_times -= 1
        else:
            print("            ",end = '')
        if exclude_times != 0:
            print("   *      ",end = '')
            exclude_times -= 1
        else:
            print("          ",end = '')
        print()
    print()
    print(total_times,"Outcome in Total.\n")
    
start_vertical_histogram()  # Call the start_vertical_histogram function to start the program

print("                           │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│  ")
print("___________________________│    Thank You!   │__________________________")
print("                           │ Have a Nice Day!│                     ")
print("                           │_________________│")

