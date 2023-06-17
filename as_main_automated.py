# write a program to sort and given digets in ascending to decending

arr = []

while True:
    user_array_input = int(input("Enter a number to be sorted (one num ata time): ,(enter a str to stop): "))
    arr.append(user_array_input)
    user_continue_or_not = int(input("Enter 1 to stop 2 to continue: "))
    if user_continue_or_not == 1:
        break
    if user_continue_or_not == 2:
        pass
 
user_choice = int(input("Enter 1 for acending , 2 for decending: "))
if user_choice == 1:
    arr.sort()
    print(arr) #ascending
elif user_choice == 2:
    arr.sort(reverse=True) #descending
    print(arr)