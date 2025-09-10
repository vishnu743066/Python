#import modulus
import addition
import subtraction
import division
import multiplication
import mod_division


operations = {
    "1.Addition \n",
    "2. Subtraction \n",
    "3. Multiplication \n",
    "4. Division\n",
    "5. Modulus Division \n"
}

if __name__ == "__main__":
    print(*operations)
    while True:
        choice = int(input("Please select your operation: "))
        if choice == 1:
            a,b = map(int,input("Please enter the values: ").split())
            res = addition.add(a,b)
            print(res)
    
        elif choice == 2:
            a,b=map(int,input("please enter the values: ").split())
            res = subtraction.sub(a,b)
            print(res)

        elif choice ==3:
            a,b=map(int,input("please enter the numbers:").split())
            res=multiplication.multi(a,b)
            print(res)
    
        elif choice==4:
            a,b=map(int,input("please enter the numbers: ").split())
            res=division.div(a,b)
            print(res)

        elif choice == 5:
            a,b=map(int,input("please enter the numbers: ").split())
            res=mod_division.mod(a,b)
            print(res)

        elif choice > 5 or choice < 1:
            print("work is under process please select between 1-5 numbers.")
            exit()