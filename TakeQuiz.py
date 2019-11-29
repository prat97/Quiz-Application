# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:04:30 2019

@author: Prat
"""

import random

def take_quiz(q):
    
    f = open("Questions.txt", 'r')
    c = 0
    score = 0
    
    for i in range(1 , 7):
        
        if q[c] == i:
            
            print(f.readline())
            print(f.readline())
            print(f.readline())
            ans = str(input("Please enter your answer (1 or 2): "))
            
            while ans != str(1) and ans != str(2):
                
                ans = str(input("Please enter valid answer (1 or 2): "))
            
            if ans + "\n" == str(f.readline()):
                
                score = score + 1
                print("Correct Answer")
            else:
                
                print('Wrong Answer')
            
            c = c + 1
            
            if(c > len(q) - 1):
                
                break
            
        else:
            
            f.readline()
            f.readline()
            f.readline()
            f.readline()
    
    print("Your score is %1d out of %2d" %(score, len(q)))

def main():
    
    try:
    
        num = int(input("How many questions do you want the quiz to have ?: "))
    
    except ValueError:
        
        num = int(input("Please enter an integer: "))
        
    while num > 6 or num == 0:
        
        try:
            
            num = int(input("Please enter number equal or lesser than the total number of questions (6) and more than 0: "))    

        except ValueError:
        
            num = int(input("Please enter an integer: "))
        
    if num == 6:
        
        q = [1, 2, 3, 4, 5, 6]

    else:
        q = random.sample(range(1,6), num)
        q.sort()
    
    take_quiz(q)

if __name__ == '__main__':
    main()