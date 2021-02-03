import pandas as pd
import csv
import re
import math
import itertools
import numpy as np
from tqdm import tqdm
from dataclasses import dataclass
import copy

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
        minimum, maximum = number.split("-")
        letter = letter.strip(":")
        letter_count=0
        for i in text:
            if i==letter:
                letter_count+=1
        if (int(minimum)<=letter_count) & (letter_count<=int(maximum)):
            valid1+=1
        if (letter==text[int(minimum)-1]) & (letter!=text[int(maximum)-1]):
            valid2+=1
        if (letter!=text[int(minimum)-1]) & (letter==text[int(maximum)-1]):
            valid2+=1
    print("Number of valid password by policy 1: "+ str(valid1))
    print("Number of valid password by policy 2: "+ str(valid2))

#Day_3
def split(word):
    return [char for char in word]

with open('Day3/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[11,31,51,71,12]
    for i in list_of_numbers:
        locals()["location" + str(i)] = 0
        locals()["trees" + str(i)] = 0
    for row in reader:
        mylist=split(row[0])
        for i in list_of_numbers[:-1]:
            if mylist[locals()["location" + str(i)]%31]=="#":
                locals()["trees" + str(i)]+=1
        if (mylist[location12%31]=="#")&(location11%2==0):
            trees12+=1
        for i in list_of_numbers[:-1]:
            locals()["location" + str(i)]+=int(str(i)[0])
        if location11%2==0:
            location12+=1
    print("We pass %d number of trees by going 1 down and 3 right!"%trees31)
    print("The product for the second part: "+str(trees11*trees31*trees51*trees71*trees12))

#Day_4
with open('Day4/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    passport_dict={}
    valid1=0
    valid2=0
    for row in reader:
        try:
            splitted_list=row[0].split(" ")
            for i in splitted_list:
                key, value= i.split(":")
                passport_dict[key]=value
        except:
            try:
                key, value= row[0].split(":")
                passport_dict[key]=value
            except:
                keys=passport_dict.keys()
                if "byr" in keys and "iyr" in keys and "eyr" in keys and "hgt" in keys and\
                "hcl" in keys and "ecl" in keys and "pid" in keys:
                    valid1+=1
                    valid_height=False
                    valid_hair=False
                    valid_eye=False
                    valid_pid=False
                    eyes=["amb","blu","brn","gry","grn","hzl","oth"]
                    height=re.match(r"([0-9]+)([a-z]+)",passport_dict["hgt"],re.I)
                    hair=re.match(r"(#)([0-9a-f]{6})",passport_dict["hcl"],re.I)
                    if height:
                        if (height.groups()[1]=="cm") & (150<=int(height.groups()[0])) &\
                        (int(height.groups()[0])<=193):
                            valid_height=True
                        elif (height.groups()[1]=="in") & (59<=int(height.groups()[0])) &\
                             (int(height.groups()[0])<=76):
                             valid_height=True
                    if hair:
                        valid_hair=True
                    if passport_dict["ecl"] in eyes:
                        valid_eye=True
                    if (len(passport_dict["pid"])==9) & (passport_dict["pid"].isnumeric()):
                        valid_pid=True
                    if (len(passport_dict["byr"])==4) & (1920<=int(passport_dict["byr"])) &\
                       (int(passport_dict["byr"])<=2002) & (len(passport_dict["iyr"])==4) &\
                       (2010<=int(passport_dict["iyr"])) & (int(passport_dict["iyr"])<=2020) &\
                       (len(passport_dict["eyr"])==4) & (2020<=int(passport_dict["eyr"])) &\
                       (int(passport_dict["eyr"])<=2030)& valid_height & valid_hair&\
                       valid_eye & valid_pid:
                        valid2+=1
                passport_dict={}
    print("There are %d valid passports"%valid1)
    print("There are %d strongly valid passports"%valid2)

#Day_5
with open('Day5/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    ids=[]
    for line in reader:
        row=line[0][:7]
        column=line[0][7:]
        list_of_rows=[i for i in range(128)]
        list_of_columns=[i for i in range(8)]
        for i in row:
            if i=="F":
                list_of_rows=list_of_rows[:int(len(list_of_rows)/2)]
            else:
                list_of_rows=list_of_rows[int(len(list_of_rows)/2):]
        for i in column:
            if i=="L":
                list_of_columns=list_of_columns[:int(len(list_of_columns)/2)]
            else:
                list_of_columns=list_of_columns[int(len(list_of_columns)/2):]
        id=list_of_rows[0]*8+list_of_columns[0]
        ids.append(id)
    for i in ids[:-1]:
        if i+1 not in ids:
            my_id=i+1
    print("The highest ID is: "+str(max(ids)))
    print("My ID is: "+str(my_id))


#Day_6
def split(word):
    return [char for char in word]
def length_calculator(answers,any_unique,all_unique):
    letters=''.join(answers)
    any_unique.append(len(set(letters)))
    all_answered=split(answers.pop(0))
    for i in answers:
        for j in all_answered:
            if j not in i:
                all_answered=[k for k in all_answered if k != j]
    all_unique.append(len(all_answered))
    return any_unique,all_unique
with open('Day6/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    answers=[]
    any_unique=[]
    all_unique=[]
    for line in reader:
        if line==[]:
            any_unique,all_unique=length_calculator(answers,any_unique,all_unique)
            answers=[]
        else:
            answers.extend(line)
    any_unique,all_unique=length_calculator(answers,any_unique,all_unique)
    print("The number of questions anyone answered 'yes': "+ str(sum(any_unique)))
    print("The number of questions everyone answered 'yes': "+ str(sum(all_unique)))

#Day_7
with open('Day7/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    rules={}
    for line in reader:
        line=', '.join(line)
        bigbag, smallbag=line.split(" contain ")
        bigbag=bigbag[:-1]
        smallbag=smallbag.strip('.')
        if ", " in smallbag:
            smallbags=smallbag.split(",  ")
            smallbags=[x[:-1] if x[-1]=="s" else x for x in smallbags]
        else:
            smallbags=[smallbag]
        smallbags=[x[:-1] if x[-1]=="s" else x for x in smallbags]
        if smallbags != ["no other bag"]:
            smallbags=[x.split(" ",1) for x in smallbags]
        else:
            smallbags=[[0,"no other bag"]]
        rules[bigbag]=smallbags

class Bag():
    def __init__(self, type, contain, my_rules):
        """
        contain is a list of strings or Bag objects
        """
        self.type=type
        self.contain=contain
        self.my_rules=my_rules
    def __eq__(self, other):
        if not isinstance(other, Bag):
            return NotImplemented
        return self.type == other.type
    def get_type(self):
        return self.type
    def get_elements(self):
        return self.contain
    def get_rules(self):
        return self.my_rules
    def elements_to_object(self, full_set=False):
        current_elements=self.get_elements()
        bags=current_elements.copy()
        my_rules=self.get_rules()
        try:
            for bag in bags:
                children=my_rules[bag[1]]
                bag_object=Bag(bag[1],children,my_rules)
                if full_set==True:
                    for i in range(int(bag[0])):
                        current_elements.append(bag_object)
                else:
                    current_elements.append(bag_object)
            for bag in bags:
                current_elements.remove(bag)
        except KeyError:
            pass
        self.contain=current_elements
        return current_elements
    def update_elements(self, newly_added_elements,full_set=False):
        current_elements=self.get_elements()
        my_rules=self.get_rules()
        added_elements=[]
        for bag in newly_added_elements:
            bag_type=bag.get_type()
            children=bag.get_elements()
            for element in children:
                if element != [0,"no other bag"]:
                    grand_children=my_rules[element[1]]
                    bag_object=Bag(element[1],grand_children,my_rules)
                    to_add=True
                    total_elements=current_elements.copy()
                    total_elements.extend(added_elements)
                    for i in total_elements:
                        if bag_object==i:
                            to_add=False
                    if full_set==True:
                        for i in range(int(element[0])):
                            added_elements.append(bag_object)
                    elif to_add==True:
                        added_elements.append(bag_object)
        current_elements.extend(added_elements)
        self.contain=current_elements
        return added_elements

shiny_gold_containers=0
for key,value in rules.items():
    mybag=Bag(key, value.copy(), rules)
    i=0
    added_elements=mybag.elements_to_object()
    if added_elements==[[0, 'no other bag']]:
        pass
    else:
        while i<len(mybag.get_elements()):
            added_elements=mybag.update_elements(added_elements)
            i+=1
        elements=mybag.get_elements()
        for i in elements:
            if i!=[0,"no other bag"]:
                if i.get_type()=="shiny gold bag":
                    shiny_gold_containers+=1
print("The number of bags that may contain a shiny gold bag: "+str(shiny_gold_containers))

mybag=Bag("shiny gold bag", [[1,"pale maroon bag"], [3,"plaid blue bag"],\
          [5, "dull tan bag"]], rules)
added_elements=mybag.elements_to_object(full_set=True)
while added_elements!=[]:
    added_elements=mybag.update_elements(added_elements,full_set=True)

print("The number of bags within a shiny gold bag: "+str(len(mybag.get_elements())))

#Day_8
with open('Day8/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    rules=[]
    for line in reader:
        particular_rule = line[0].split(" ")
        rules.append(particular_rule)


def run_through(start_index, my_rules):
    proceed=True
    new_index=start_index
    element=my_rules[new_index]
    visited_elements=[[element,new_index]]
    accumulator=0
    last_index=len(my_rules)-1
    last_element=[my_rules[-1], last_index]
    while proceed:
        direction, number = element
        current_index=new_index
        if direction=="acc":
            new_index=current_index+1
            accumulator+=int(number)
        elif direction=="jmp":
            new_index=current_index+int(number)
        else:
            new_index=current_index+1
        element=my_rules[new_index]
        element_list=[element,new_index]
        if element_list in visited_elements:
            cause="Infinite loop"
            break
        elif element_list==last_element:
            cause="Reached the end"
            visited_elements.append(element_list)
            if element[0]=="acc":
                accumulator+=int(last_element[0][1])
            break
        visited_elements.append(element_list)
    return accumulator, cause

accumulator, cause=run_through(0, rules)
print("The value of the accumulator before visiting the same element again: "+str(accumulator))
for i in range(len(rules)):
    modified_rules=[x[:] for x in rules]
    if rules[i][0]=="jmp":
        modified_rules[i][0]="nop"
        accumulator, cause = run_through(0, modified_rules)
        if cause=="Reached the end":
            break
    elif rules[i][0]=="nop":
        modified_rules[i][0]="jmp"
        accumulator, cause = run_through(0, modified_rules)
        if cause=="Reached the end":
            break
print("The value of the accumulator after the last item with the modified rule: "+str(accumulator))

#Day_9

with open('Day9/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    numbers=[]
    for line in reader:
        numbers.extend(line)
    numbers=[int(x) for x in numbers]

for i in range(len(numbers[25:])):
    index=i+25
    my_sums=[]
    for j in range(len(numbers[i:i+24])):
        for k in range(len(numbers[j+1:i+25])):
            my_sum=numbers[j+i]+numbers[k+j+1]
            my_sums.append(my_sum)
    if int(numbers[index]) not in my_sums:
        print("The invalid number: "+str(numbers[index]))
        invalid_number=numbers[index]
        break

for i in range(len(numbers[:index-2])):
    for j in range(len(numbers[i+1:index-1])):
        start_number=numbers[i]
        end_number=numbers[i+j+1]
        my_sum=0
        for element in numbers[i:i+j+2]:
            my_sum+=element
        if my_sum==invalid_number:
            print("The sum of the numbers: "+str(min(numbers[i:i+j+2])+max(numbers[i:i+j+2])))
            break

#Day_10

with open('Day10/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_numbers=[]
    for row in reader:
        list_of_numbers.append(int(row[0]))
list_of_numbers.append(0)
list_of_numbers.sort()
my_device=list_of_numbers[-1]+3
list_of_numbers.append(my_device)
jolts1=0
jolts2=0
jolts3=0
for i in range(len(list_of_numbers[:-1])):
    difference=list_of_numbers[i+1]-list_of_numbers[i]
    if difference==1:
        jolts1+=1
    elif difference==2:
        jolts2+=1
    else:
        jolts3+=1
print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is: "\
      +str(jolts1*jolts3))


def update_adapter_chain(dict_of_chains, adapters, my_device):
    new_dict_of_chains={}
    updated=False
    for key, value in dict_of_chains.items():
        for i in range(1,4):
            new_number=key+i
            if new_number in adapters:
                if new_number in new_dict_of_chains.keys():
                    existing_lenght=new_dict_of_chains[new_number]
                    new_dict_of_chains[new_number]=existing_lenght+value
                else:
                    new_dict_of_chains[new_number]=value
                updated=True
        if key==my_device:
            if key in new_dict_of_chains.keys():
                existing_lenght=new_dict_of_chains[key]
                new_dict_of_chains[key]=existing_lenght+value
            else:
                new_dict_of_chains[key]=value
    return new_dict_of_chains, updated

dict_of_chains={}
dict_of_chains[0]=1
updated=True

while updated==True:
    dict_of_chains, updated= update_adapter_chain(dict_of_chains, list_of_numbers, my_device)

i=0
for key, value in dict_of_chains.items():
    length=value
    i+=length

print("The number of distinct ways to arrange adapters: "+str(i))

#Day_11

with open('Day11/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_seats=[]
    for row in reader:
        list_of_row=[element for element in row[0]]
        list_of_seats.append(list_of_row)

def march(list_of_seats,first_index,second_index,j):
    try:
        first_index=first_index+j[0]
        second_index=second_index+j[1]
        if (first_index==-1) | (second_index==-1):
            neighboring_seat=".."
        else:
            neighboring_seat=list_of_seats[first_index][second_index]
    except IndexError:
        neighboring_seat=".."
    return neighboring_seat, first_index, second_index

def check_neighbors(list_of_seats, row, column, complex=False):
    neighbors=[]
    neighbor_indices=[(-1,0), (-1,1), (0,1), (1,1),\
                      (1,0), (1,-1), (0,-1), (-1,-1)]
    for j in neighbor_indices:
        first_index=row
        second_index=column
        try:
            neighboring_seat, first_index, second_index=march(list_of_seats,first_index,second_index,j)
            if complex==True:
                while neighboring_seat==".":
                    neighboring_seat, first_index, second_index=march(list_of_seats,first_index,second_index,j)
            neighbors.append(neighboring_seat)
        except IndexError:
            neighbors.append("..")
    return neighbors

def update_seat(list_of_seats, row, column, complex):
    updated_seat=list_of_seats[row][column]
    updated=False
    if list_of_seats[row][column]=="L":
        neighbors=check_neighbors(list_of_seats, row, column, complex)
        if "#" not in neighbors:
            updated_seat="#"
            updated=True
    if list_of_seats[row][column]=="#":
        neighbors=check_neighbors(list_of_seats, row, column, complex)
        list_occupied=[1 for i in neighbors if i=="#"]
        number_occupied=sum(list_occupied)
        if complex==True:
            threshold=5
        else:
            threshold=4
        if threshold<=number_occupied:
            updated_seat="L"
            updated=True
    return updated_seat, updated

def update_hall(list_of_seats, complex=False):
    updated_hall=False
    updated_seats=[x[:] for x in list_of_seats]
    for row in range(len(list_of_seats)):
        for column in range(len(list_of_seats[0])):
            updated_seat, updated=update_seat(list_of_seats, row, column, complex)
            if updated==True:
                updated_hall=True
                updated_seats[row][column]=updated_seat
    return updated_seats, updated_hall

list_of_seats_copy=[element[:] for element in list_of_seats]

updated_hall=True
while updated_hall==True:
    list_of_seats, updated_hall=update_hall(list_of_seats)

updated_hall=True
while updated_hall==True:
    list_of_seats_copy, updated_hall=update_hall(list_of_seats_copy, complex=True)

for i in [(list_of_seats,"first rule"), (list_of_seats_copy, "second rule")]:
    occupied_seats=0
    for row in i[0]:
        for seat in row:
            if seat=="#":
                occupied_seats+=1
    print("The number of occupied seats with %s: "%i[1]+str(occupied_seats))

#Day_12

with open('Day12/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_instructions=[]
    for row in reader:
        list_of_row=[row[0][0], int(row[0][1:])]
        list_of_instructions.append(list_of_row)

def turn_waypoint(waypoint, instruction):
    waypoint_x=waypoint[0]
    waypoint_y =waypoint[1]
    old_x=waypoint_x
    old_y=waypoint_y
    if instruction[0]=="R":
        number_of_turns=(instruction[1]/90)%4
    else:
        number_of_turns=4-(instruction[1]/90)%4
    if  number_of_turns==1:
        waypoint_x=old_y
        waypoint_y=-old_x
    elif number_of_turns==2:
        waypoint_x=-old_x
        waypoint_y=-old_y
    elif number_of_turns==3:
        waypoint_x=-old_y
        waypoint_y=old_x
    return waypoint_x, waypoint_y

def turn_direction(direction, instruction):
    mappings={"N":0, "E":1, "S":2, "W":3}
    contra_mappings={0:"N", 1:"E", 2:"S", 3:"W"}
    current_direction=mappings[direction]
    if instruction[0]=="R":
        number_of_turns=(instruction[1]/90)%4
    else:
        number_of_turns=4 - ((instruction[1]/90)%4)
    updated_direction=(current_direction+number_of_turns)%4
    updated_direction=contra_mappings[int(updated_direction)]
    return updated_direction

def move_forward(position, instruction):
    x_value=position[0][0]
    y_value=position[0][1]
    if position[1]=="N":
        y_value+=instruction[1]
    if position[1]=="S":
        y_value-=instruction[1]
    if position[1]=="E":
        x_value+=instruction[1]
    if position[1]=="W":
        x_value-=instruction[1]
    return x_value, y_value

def move_forward_waypoint(position, instruction):
    x_value=position[0][0]
    y_value=position[0][1]
    waypoint_x=position[2][0]
    waypoint_y=position[2][1]
    x_value+=waypoint_x*instruction[1]
    y_value+=waypoint_y*instruction[1]
    return x_value, y_value

def update_position(position, instruction, waypoint_move=False):
    x_value=position[0][0]
    y_value=position[0][1]
    direction=position[1]
    waypoint=position[2]
    if waypoint_move==True:
        modify_x=position[2][0]
        modify_y=position[2][1]
    else:
        modify_x=x_value
        modify_y=y_value
    if instruction[0]=="N":
        modify_y+=instruction[1]
    if instruction[0]=="S":
        modify_y-=instruction[1]
    if instruction[0]=="E":
        modify_x+=instruction[1]
    if instruction[0]=="W":
        modify_x-=instruction[1]
    if (instruction[0]=="R") | (instruction[0]=="L"):
        if waypoint_move==True:
            modify_x, modify_y=turn_waypoint(waypoint, instruction)
        else:
            direction=turn_direction(direction, instruction)
    if instruction[0]=="F":
        if waypoint_move==True:
            x_value, y_value=move_forward_waypoint(position, instruction)
        else:
            modify_x, modify_y=move_forward(position, instruction)
    if waypoint_move==True:
        waypoint=[modify_x, modify_y]
    else:
        x_value, y_value = modify_x, modify_y
    return [[x_value, y_value], direction, waypoint]

starting_position=[[0,0],"E",[10,1]]
new_position_1=starting_position
new_position_2=starting_position

for i in list_of_instructions:
    new_position_1=update_position(new_position_1, i)
    new_position_2=update_position(new_position_2, i, waypoint_move=True)

print("Manhattan distance with first rule: "+str(abs(new_position_1[0][0])+abs(new_position_1[0][1])))
print("Manhattan distance with second rule: "+str(abs(new_position_2[0][0])+abs(new_position_2[0][1])))

#Day_13

with open('Day13/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    input_lines_first=[]
    input_lines_second=[]
    for row in reader:
        input_lines_second.append(row)
        row=[int(i) for i in row if i!="x"]
        input_lines_first.append(row)

possible_departures=[]
for i in input_lines_first[1]:
    departure=input_lines_first[0][0]/i
    departure=math.ceil(departure)*i
    possible_departures.append(departure)

possible_departures=list(zip(input_lines_first[1], possible_departures))
earliest_departure=possible_departures[0]

for j in possible_departures:
    if j[1]<earliest_departure[1]:
        earliest_departure=j

print("The earliest bust to take: "+str(earliest_departure[0]*(earliest_departure[1]\
       -input_lines_first[0][0])))

minutes=[i for i in range(len(input_lines_second[1]))]
ids_minutes=list(zip(input_lines_second[1], minutes))
ids_minutes={int(i[0]): -i[1]%int(i[0]) for i in ids_minutes if i[0]!="x"}
ids_minutes_items = ids_minutes.items()
ids_minutes=sorted(ids_minutes_items, reverse=True)
max_id_minutes=ids_minutes[0]
ids_minutes=dict(ids_minutes)
ids=list(ids_minutes.keys())

val=max_id_minutes[1]
r=max_id_minutes[0]

for bus in ids[1:]:
    while val % bus != ids_minutes[bus]:
        val += r
    r *= bus

print("The earliest timestamp: "+str(val))

#Day_14
with open('Day14/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_rows=[]
    for row in reader:
        list_of_rows.append(row[0].split(" = "))

def rule_1(list_of_rows):
    memory_dictionary={}
    for i in list_of_rows:
        if i[0]=="mask":
            mask=i[1]
        else:
            dict_key=int("".join(filter(str.isdigit, i[0])))
            number_to_convert=str(f'{int(i[1]):036b}')
            number_converted=[i if mask[index]=="X" else mask[index] for index, i in enumerate(number_to_convert)]
            number_converted=int("".join(number_converted),2)
            memory_dictionary[dict_key]=number_converted
    return memory_dictionary

def rule_2(list_of_rows):
    memory_dictionary={}
    for i in list_of_rows:
        if i[0]=="mask":
            mask=i[1]
        else:
            dict_key=int("".join(filter(str.isdigit, i[0])))
            number_to_convert=str(f'{dict_key:036b}')
            number_converted=["X" if mask[index]=="X" else i if mask[index]=="0" else "1" for index, i in enumerate(number_to_convert)]
            number_of_floating=sum([1 for i in number_converted if i=="X"])
            permutations=list(itertools.product([0, 1], repeat=number_of_floating))
            list_of_new_keys=[]
            for j in permutations:
                final_number=[]
                j_index=0
                for k in number_converted:
                    if k!="X":
                        final_number.append(k)
                    else:
                        final_number.append(str(j[j_index]))
                        j_index+=1
                list_of_new_keys.append(int("".join(final_number),2))
            for j in list_of_new_keys:
                memory_dictionary[j]=int(i[1])
    return memory_dictionary

memory_dictionary_1=rule_1(list_of_rows)
print("Sum of memory values using Rule 1: "+str(sum(list(memory_dictionary_1.values()))))

memory_dictionary_2=rule_2(list_of_rows)
print("Sum of memory values using Rule 2: "+str(sum(list(memory_dictionary_2.values()))))

#Day 15
from tqdm import tqdm

played_numbers=[20,9,11,0,1,2]

turns={20:[1], 9:[2], 11:[3], 0:[4], 1:[5], 2:[6]}

last_key=played_numbers[-1]
last_value=turns[last_key]
for j in [(7,2021), (2021,30000001)]:
    for i in tqdm(range(j[0],j[1])):
        if len(last_value)>1:
            #played_numbers.remove(played_numbers[-1])
            new_element=last_value[1]-last_value[0]
            turns[last_key]=[last_value[1]]
            #played_numbers.append(new_element)
        else:
            new_element=0
            #played_numbers.append(new_element)
        new_key=new_element
        new_value=i
        if new_key in turns:
          turns[new_key].append(new_value)
        else:
          turns[new_key] = [new_value]
        last_key=new_key
        last_value=turns[last_key]
    spoken_number=j[1]-1
    for key,value in turns.items():
        if spoken_number in value:
          print("The %d spoken number is: "%spoken_number+str(key))
          break

#Day_16
with open('Day16/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_rules=[]
    my_ticket=[]
    nearby_tickets=[]
    list_of_lists=["list_of_rules","my_ticket", "nearby_tickets"]
    current_list=0
    for row in reader:
        if row==[]:
            current_list+=1
        elif current_list==0:
            new_row=row[0].split(": ")
            new_row[0]=[new_row[0]]
            new_row[1]=new_row[1].split(" or ")
            for i in range(2):
                new_row[1][i]=new_row[1][i].split("-")
                new_row[1][i]=[int(j) for j in new_row[1][i]]
            new_row=[item for sublist in new_row for item in sublist]
            eval(list_of_lists[current_list]).append(new_row)
        elif (row==["your ticket:"]) | (row==["nearby tickets:"]):
            pass
        else:
            row=[int(j) for j in row]
            eval(list_of_lists[current_list]).append(row)

possible_numbers=[]
for i in list_of_rules:
    for j in range(1,3):
        for l in range(i[j][0],i[j][1]+1):
            possible_numbers.append(l)
possible_numbers=list(set(possible_numbers))

not_valid=[]
valid_tickets=my_ticket.copy()
for i in range(len(nearby_tickets)):
    valid_ticket=True
    for j in nearby_tickets[i]:
        if j not in possible_numbers:
            not_valid.append(j)
            valid_ticket=False
    if valid_ticket:
        valid_tickets.append(nearby_tickets[i])

possibility_matrix=[[True]*20 for i in range(20)]

for i in range(len(valid_tickets[0])):
    for j in range(len(valid_tickets)):
        for k in range(len(list_of_rules)):
            if (valid_tickets[j][i] not in range(list_of_rules[k][1][0], list_of_rules[k][1][1]+1)) &\
            (valid_tickets[j][i] not in range(list_of_rules[k][2][0], list_of_rules[k][2][1]+1)):
                possibility_matrix[i][k]=False

possibility_matrix = {k: v for (k, v) in enumerate(possibility_matrix)}
optimal_order=[]
for i,v in possibility_matrix.items():
    total_sum=[1 for i in v if i==True]
    optimal_order.append(sum(total_sum))

optimal_order=list(zip(optimal_order, possibility_matrix.keys()))
optimal_order=sorted(optimal_order, key=lambda tup: tup[0])

possibility_matrix = {k[1]: possibility_matrix[k[1]] for k in optimal_order}

current_items=[]
taken_columns=[]
data_columns=[i[0] for i in list_of_rules]

@dataclass
class ordering:
    choices: dict
    taken_columns:list
    data_columns: list
    def add_new_element(self):
        new_orderings=[]
        if self.taken_columns!=[]:
            taken_indexes=[i[2] for i in self.taken_columns]
        else:
            taken_indexes=[]
        try:
            next_element=list(self.choices.items())[0]
            element_index=next_element[0]
            element_value=next_element[1]
            for element in range(len(v)):
                if element_value[element]==True:
                    if element not in taken_indexes:
                        new_choices=self.choices.copy()
                        new_choices.pop(element_index)
                        new_taken_columns=self.taken_columns.copy()
                        new_taken_columns.append((element_index, self.data_columns[element], element))
                        new_orderings.append(ordering(new_choices, new_taken_columns, self.data_columns))
            return new_orderings
        except IndexError:
            return []

class_items = [ordering(possibility_matrix, taken_columns, data_columns)]
iter = 0
while iter<len(class_items):
    class_items = class_items + class_items[iter].add_new_element()
    iter +=1

final_positions=class_items[-1].taken_columns
final_positions=[i[0] for i in final_positions if "departure" in i[1]]
final_product=1
for i in final_positions:
    final_product*=my_ticket[0][i]
print("The product of the numbers in my ticket: "+str(final_product))

import pandas as pd
import csv
import re
import math
import itertools
import numpy as np
from tqdm import tqdm
from dataclasses import dataclass

#Day_17
with open('Day17/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_cubes=[]
    for row in reader:
        row=[element for element in row[0]]
        list_of_cubes.append(row)

space_3d = np.zeros((13,20,20), str)
space_4d = np.zeros((13,13,20,20), str)

for i in range(len(list_of_cubes)):
    for j in range(len(list_of_cubes[i])):
        space_3d[6][13-i][j+6]=list_of_cubes[i][j]
        space_4d[6][6][13-i][j+6]=list_of_cubes[i][j]

space_3d=np.where(space_3d=='', '.', space_3d)
space_4d=np.where(space_4d=='', '.', space_4d)

def check_neighbors(space, dimensions, z_dim, y_dim, x_dim, w_dim = 0):
    number_of_actives=0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                if dimensions==4:
                    for l in [-1,0,1]:
                        try:
                            if (space[w_dim+l][z_dim+i][y_dim+j][x_dim+k]=='#') & ((i!=0) | (j!=0) | (k!=0) | (l!=0)):
                                number_of_actives+=1
                        except IndexError:
                            pass
                else:
                    try:
                        if (space[z_dim+i][y_dim+j][x_dim+k]=='#') & ((i!=0) | (j!=0) | (k!=0)):
                            number_of_actives+=1
                    except IndexError:
                        pass
    return  number_of_actives

def activation_cycle(space, dimensions):
    space_copy=space.copy()
    if dimensions==4:
        for w_dim in range(len(space)):
            for z_dim in range(len(space[w_dim])):
                for y_dim in range(len(space[w_dim][z_dim])):
                    for x_dim in range(len(space[w_dim][z_dim][y_dim])):
                        if space[w_dim][z_dim][y_dim][x_dim]=='.':
                            number_of_actives=check_neighbors(space, dimensions, z_dim, y_dim, x_dim, w_dim)
                            if number_of_actives==3:
                                space_copy[w_dim][z_dim][y_dim][x_dim]='#'
                        else:
                            number_of_actives=check_neighbors(space, dimensions, z_dim, y_dim, x_dim, w_dim)
                            if (number_of_actives==2) | (number_of_actives==3):
                                space_copy[w_dim][z_dim][y_dim][x_dim]='#'
                            else:
                                space_copy[w_dim][z_dim][y_dim][x_dim]='.'
    else:
        for z_dim in range(len(space)):
            for y_dim in range(len(space[z_dim])):
                for x_dim in range(len(space[z_dim][y_dim])):
                    if space[z_dim][y_dim][x_dim]=='.':
                        number_of_actives=check_neighbors(space, dimensions, z_dim, y_dim, x_dim)
                        if number_of_actives==3:
                            space_copy[z_dim][y_dim][x_dim]='#'
                    else:
                        number_of_actives=check_neighbors(space,dimensions, z_dim, y_dim, x_dim)
                        if (number_of_actives==2) | (number_of_actives==3):
                            space_copy[z_dim][y_dim][x_dim]='#'
                        else:
                            space_copy[z_dim][y_dim][x_dim]='.'
    return space_copy

for i in tqdm(range(6)):
    space_3d=activation_cycle(space_3d, 3)
    space_4d=activation_cycle(space_4d, 4)

unique, counts = np.unique(space_3d, return_counts=True)
final_dict=dict(zip(unique, counts))
print("The total number of active cubes in a 3D space: "+str(final_dict['#']))

unique, counts = np.unique(space_4d, return_counts=True)
final_dict=dict(zip(unique, counts))
print("The total number of active cubes in a 4D space: "+str(final_dict['#']))


#Day_18
with open('Day18/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    list_of_expressions=[]
    for row in reader:
        row=[i for i in row[0] if i!=" "]
        row=[int(i) if (i!='*') & (i!='+') & (i!='(') & (i!=')') else i for i in row ]
        list_of_expressions.append(row)

def find_smallest_brackets(expression):
    index_of_brackets={'bracket_exists':'no'}
    last_index='bracket_exists'
    for i in range(len(expression)):
        if (index_of_brackets=={'bracket_exists':'no'}) & (expression[i]=='('):
            index_of_brackets[i]='('
            last_index=i
            index_of_brackets['bracket_exists']='yes'
        elif (expression[i]=='(') & (index_of_brackets[last_index]=='('):
            del index_of_brackets[last_index]
            index_of_brackets[i]='('
            last_index=i
        elif (expression[i]==')') & (index_of_brackets[last_index]=='('):
            index_of_brackets[i]=')'
            last_index=i
        elif (expression[i]=='(') & (index_of_brackets[last_index]==')'):
            index_of_brackets[i]='('
            last_index=i
    return index_of_brackets

def execute_simple_calculation(expression, advanced_math=False):
    old_numbers=expression.copy()
    if advanced_math==False:
        new_numbers=[]
        while len(new_numbers)!=1:
            new_numbers=[]
            for i in range(len(old_numbers)):
                if old_numbers[i]=='+':
                    new_number=old_numbers[i-1]+old_numbers[i+1]
                    new_numbers.append(new_number)
                    new_numbers.extend(old_numbers[i+2:])
                    break
                elif old_numbers[i]=='*':
                    new_number=old_numbers[i-1]*old_numbers[i+1]
                    new_numbers.append(new_number)
                    new_numbers.extend(old_numbers[i+2:])
                    break
            old_numbers=new_numbers.copy()
    else:
        while "+" in old_numbers:
            new_numbers=[]
            for i in range(len(old_numbers)):
                if old_numbers[i]=='+':
                    new_number=old_numbers[i-1]+old_numbers[i+1]
                    if old_numbers[:i-1]!=[]:
                        new_numbers.extend(old_numbers[:i-1])
                    else:
                        pass
                    new_numbers.append(new_number)
                    new_numbers.extend(old_numbers[i+2:])
                    break
            old_numbers=new_numbers.copy()
        new_numbers=old_numbers
        while len(new_numbers)!=1:
            new_numbers=[]
            for i in range(len(old_numbers)):
                if old_numbers[i]=='*':
                    new_number=old_numbers[i-1]*old_numbers[i+1]
                    new_numbers.append(new_number)
                    new_numbers.extend(old_numbers[i+2:])
                    break
            old_numbers=new_numbers.copy()
    return new_numbers[0]


def execute_complex_calculation(expression, index_of_brackets, advanced_math=False):
    new_expression=expression.copy()
    substract_length=0
    if index_of_brackets['bracket_exists']=='yes':
        for j in range(1, len(index_of_brackets)-1, 2):
            opening_bracket_position=list(index_of_brackets.keys())[j]-substract_length
            closing_bracket_position=list(index_of_brackets.keys())[j+1]-substract_length
            calculation=execute_simple_calculation(new_expression[opening_bracket_position+1:closing_bracket_position],\
            advanced_math)
            substract_length+=len(new_expression[opening_bracket_position+1:closing_bracket_position])+1
            new_expression[opening_bracket_position:closing_bracket_position+1]=[calculation]
    else:
        new_expression=execute_simple_calculation(new_expression, advanced_math)
    return new_expression


for j in [False, True]:
    final_number=0
    for i in list_of_expressions:
        while isinstance(i, int)==False:
            index_of_brackets=find_smallest_brackets(i)
            i=execute_complex_calculation(i, index_of_brackets, advanced_math=j)
        final_number+=i
    if j==False:
        print("The final number with simple maths: "+str(final_number))
    else:
        print("The final number with advanced maths: "+str(final_number))

#Day_19
with open('Day19/input.txt', 'r') as fd:
    reader = csv.reader(fd)
    dict_of_rules={}
    patterns=[]
    append_rules=True
    for row in reader:
        if row:
            if append_rules==True:
                key, value = row[0].split(': ')
                key = int(key)
                value = value.replace("\"", "")
                dict_of_rules[key]=value
            else:
                patterns.append(row[0])
        else:
            append_rules=False

def fill_rule(rules, rule_num):
	rule = rules[rule_num]
	if re.search("[a-z]", rule):
		return rule
	for sub_rule in rule.split(" | "):
		for num in sub_rule.split():
			inner_rule = fill_rule(rules, int(num))
			if "|" in inner_rule:
				inner_rule = f"({inner_rule})"
			rule = rule.replace(num, inner_rule, 1)
	rule = rule.replace(" ", "")
	rules[rule_num] = rule
	return rule

def is_following_rule(message, rule):
	return bool(re.match(f"^({rule})$", message))

filled_rules = dict_of_rules.copy()
rule_num = 0
fill_rule(filled_rules, rule_num)
num_valid = 0
for message in patterns:
	if is_following_rule(message, filled_rules[rule_num]):
		num_valid += 1
print("The number of matching messages :", num_valid)
