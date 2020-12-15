import pandas as pd
import csv


#Day_1
with open('Day1/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[]
    for row in reader:
        list_of_numbers.extend(row)
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers[i:])):
            for k in range(len(list_of_numbers[j:])):
                total=int(list_of_numbers[i])+int(list_of_numbers[j])\
                      +int(list_of_numbers[k])
                if total==2020:
                    print(int(list_of_numbers[i])*int(list_of_numbers[j])\
                          *int(list_of_numbers[k]))
