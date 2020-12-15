import pandas as pd
import csv


#Day_1
with open('Day1/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[]
    for row in reader:
        list_of_numbers.extend(row)
    for i in range(len(list_of_numbers)):
        for j in range(i, len(list_of_numbers)):
            total1=int(list_of_numbers[i])+int(list_of_numbers[j])
            if total1==2020:
                print("The product of the two numbers: "+str(int(list_of_numbers[i])\
                *int(list_of_numbers[j])))
            for k in range(j, len(list_of_numbers)):
                total2=int(list_of_numbers[i])+int(list_of_numbers[j])\
                      +int(list_of_numbers[k])
                if total2==2020:
                    print("The product of the three numbers: "+str(int(list_of_numbers[i])\
                    *int(list_of_numbers[j])*int(list_of_numbers[k])))

#Day_2
with open('Day2/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    valid1=0
    valid2=0
    for row in reader:
        number, letter, text = row[0].split(" ")
        min, max = number.split("-")
        letter = letter.strip(":")
        letter_count=0
        for i in text:
            if i==letter:
                letter_count+=1
        if (int(min)<=letter_count) & (letter_count<=int(max)):
            valid1+=1
        if (letter==text[int(min)-1]) & (letter!=text[int(max)-1]):
            valid2+=1
        if (letter!=text[int(min)-1]) & (letter==text[int(max)-1]):
            valid2+=1
    print("Number of valid password by policy 1: "+ str(valid1))
    print("Number of valid password by policy 2: "+ str(valid2))
