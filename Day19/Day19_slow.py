import pandas as pd
import csv
import re
import math
import itertools
import numpy as np
from tqdm import tqdm
from dataclasses import dataclass
import copy
import re

def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result

#Day_19
with open('Day19/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    dict_of_rules={}
    for row in reader:
        if row:
            key, value = row[0].split(': ')
            key = int(key)
            values = value.split(' | ')
            values_list=[]
            for i in values:
                value = i.split(' ')
                values_list.append(value)
            for i in range(len(values_list)):
                for j in range(len(values_list[i])):
                    try:
                        values_list[i][j] = int(values_list[i][j])
                    except ValueError:
                        values_list[i][j] = values_list[i][j][1:-1]
            dict_of_rules[key]=values_list
        else:
            break

def update_list(dict_of_rules, list_of_matches, final_matches, dividing_rules):
    updated=False
    new_list_of_matches=[]
    for i in range(len(list_of_matches)):
        new_match=copy.deepcopy(list_of_matches[i])
        for j in range(len(new_match)):
            number_of_letters=0
            if (new_match[j]=='b') | (new_match[j]=='a'):
                number_of_letters+=1
            else:
                if new_match[j] in dividing_rules:
                    new_match_1=copy.deepcopy(new_match)
                    new_match_2=copy.deepcopy(new_match)
                    new_match_1[j]=dict_of_rules[new_match[j]][0]
                    new_match_2[j]=dict_of_rules[new_match[j]][1]
                    new_list_of_matches.append(new_match_1)
                    new_list_of_matches.append(new_match_2)
                    updated=True
                    break
                    #new_match[j] = dict_of_rules[new_match[j]]
                else:
                    new_match[j] = dict_of_rules[new_match[j]][0]
                    updated=True
            if j==max(range(len(new_match))):
                if number_of_letters==len(new_match):
                    final_matches.append(new_match)
                else:
                    new_list_of_matches.append(new_match)
    if updated==True:
        for i in range(len(new_list_of_matches)):
            new_list_of_matches[i]=flatten(new_list_of_matches[i])
    return new_list_of_matches, final_matches, updated

dividing_rules=[]
for key,value in dict_of_rules.items():
    if len(dict_of_rules[key])>1:
        dividing_rules.append(key)

list_of_matches = dict_of_rules[0]
final_matches=[]
updated=True
while updated==True:
    list_of_matches, final_matches, updated = update_list(dict_of_rules, list_of_matches, final_matches, dividing_rules)
    print(final_matches)
#list_of_matches = update_list(dict_of_rules, list_of_matches)


print(dict_of_rules[42])
print(dict_of_rules[110])

print(list_of_matches)
