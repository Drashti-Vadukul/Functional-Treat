
print("\nWelcome To The Data Analyzer And Transformer Program")

arry = []


# Input Data
def enter_data():
    global arry

    data = input("Enter Data For a 1D Array (Separated By Spaces): ")
    arry = data.split()

    for i in range(len(arry)):
        arry[i] = int(arry[i])

    print("\nData has been Stored Successfully!")


# Display Summary
def show_summary():
    print("\nData Summary:")
    print("")
    print("- Total Elements :", len(arry))
    print("- Minimum Value :", min(arry))
    print("- Maximum Value :", max(arry))
    print("- Sum of All Values :", sum(arry))
    print("- Average Value :", sum(arry) / len(arry))

# Calculate Factorial (Recursion)
def factorial(n):
  
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# filter Data
def filter_data():
    data = int(input ("Enter a Thredshold Value To Filter Out Data Above This Value:"))
    result = list(filter(lambda x: x >= data, arry))
    print("\n Filtered Data (Values = "+ str(data) + "):", result)

#Sorting Data
def sort_data():
    print("\n Choose Sorting Option :")
    print(" 1. Ascending")
    print(" 2. Descending")

    choice = int(input("Enter Your Choice :"))

    if choice == 1:
        arry.sort()
        print("Sorted Data in Ascending Order:", arry) 

    elif choice == 2:
        arry.sort(reverse=True)
        print("Sorted Data in Descending Order:", arry)

    else:
        print("Invalid Choice.")

# Data Statistics (Return Multiple Values)
def data_statistics():
    total = len(arry)
    minimum = min(arry)
    maximum = max(arry)
    sum_value = sum(arry)
    average = sum_value / total

    print("\nDataset Statistics:")

    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Total values:", total)
    print("Sum of all values:", sum_value)
    print("Average value:", average)

        
     


while True:

        print("\n Main Manu :")
        print("\n 1. Input Data ")
        print(" 2. Display Data Summary (Built-in-Functions)")
        print(" 3. Calculate Factorial(Rucursion)")
        print(" 4. Filter Data By Threshold (Lambda Function)")
        print(" 5. Sort Data")
        print(" 6. Display Dataset Statistics (Return Multiple Value )")
        print(" 7. Exit Program ")
    
        print("")
        choice = int(input("Please Enter Your Choice :"))
        print("")

        if choice == 1:
            enter_data()

        elif choice == 2:
            show_summary()

        elif choice ==3:
            n = int(input("Enter a Number to Calculate It's Factorial: "))
            fact = factorial(n)
            print(f"The Factorial {n} is: {fact}")

        elif choice ==4:
            filter_data()

        elif choice ==5:
            sort_data()

        elif choice ==6:
            data_statistics()
               

        elif choice == 7:
            print("\nThank You For Using The Program. Goodbye!")
            break