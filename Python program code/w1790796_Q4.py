# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1790796
# Date: 17/04/2020
pass_credit = [120,100,100,80,60,40,20,20,20,0]
defer_credit = [0,20,0,20,40,40,40,20,0,0]
fail_credit = [0,0,20,20,20,40,60,80,100,120]
progress_times,trailer_times,retriever_times,exclude_times = 0,0,0,0
total_times = 0
print("                │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│")
print("————————————————│ Welcome to Alternative Staff Version │————————————————")
print("                │______________________________________│")

def start_alternative():# start in Alternative Staff Version 
    global pass_mark,defer_mark,fail_mark
    for test_no in range(10):
        pass_mark = pass_credit[test_no]
        defer_mark = defer_credit[test_no]
        fail_mark = fail_credit[test_no]
        decision()
    final_result_vertical_histogram()
    
def decision():
    global pass_mark,defer_mark,fail_mark,progress_times,trailer_times,retriever_times,exclude_times,total_times
    if pass_mark + defer_mark + fail_mark == 120:
        if pass_mark == 120:
            print("\n\t>>>>  Progress  <<<<")
            progress_times += 1
        elif pass_mark==100:
            print("\n\t>>>>  Progress – module trailer  <<<<")
            trailer_times += 1
        elif pass_mark <= 80 and fail_mark <= 60:
            print("\n\t>>>>  Do not Progress – module retriever  <<<<")
            retriever_times += 1
        else:
            print("\n\t>>>>  Exclude  <<<<")
            exclude_times += 1
        total_times += 1
    else:
        print("\n\t**** Total Error! ****")
        pass_credit()

    
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
start_alternative() # Call the start_alternative function to start the program
print("                           │¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯│  ")
print("___________________________│    Thank You!   │__________________________")
print("                           │ Have a Nice Day!│                     ")
print("                           │_________________│")
