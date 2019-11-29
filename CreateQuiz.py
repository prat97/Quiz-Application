# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:33:18 2019

@author: Prat
"""

def main():
    
    f = open("Questions.txt", "a+")
    
    while True:
        
        ans = str(input("Enter the question: "))
        f.write(ans + "?\n")
        op1 = str(input("Enter option 1: "))
        op2 = str(input("Enter option 2: "))
        opr = str(input("The answer is (1 or 2): "))
        
        while opr != str(1) and opr != str(2):
        
            opr = str(input("Please enter valid input! The answer is (1 or 2): "))
        
        f.write("1. " + op1 + "\n")
        f.write("2. " + op2 + "\n")
        f.write(opr + "\n")
        
        choice = str(input("Do you want to add another question (Y or N)?"))
        
        while choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':
            
            choice = str(input("Please enter valid input! Do you want to add another question (Y or N)?: "))
        
        if choice == 'y' or choice == 'Y':
            
            continue
        
        
        if choice == 'n' or choice == 'N':
            
            f.close()
            break
        
if __name__ == '__main__':
    main()