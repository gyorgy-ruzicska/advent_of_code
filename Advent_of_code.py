import pandas as pd
import csv
import re


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
            list=row[0].split(" ")
            for i in list:
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
        sum=0
        for element in numbers[i:i+j+2]:
            sum+=element
        if sum==invalid_number:
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
import pandas as pd
import csv
import re

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
