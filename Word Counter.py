#A program that counts the number of times a specific word or name is mentioned and the total number of words in the file
# Creator: Jeffrey Chen @ Portola High School

#import matplotlib.pyplot as plt

def wcounter(tstring):
    x = tstring.split()
    nnn = len(x)
    print "Total number of words:", nnn
    return nnn

def specialcount(tstring, y):
    counter = 0
    x = tstring.split()
    nnn = len(x)
    for i in range (1, nnn):
        if x[i] == y:
            counter = counter + 1
            
    print "number of word <", y , ">: ", counter
    return counter

def count_file(fn_name):
    text_file = open(fn_name)
    text = text_file.read()
    print "Words in file", fn_name
    print "Letters in file:", len(text)
    wcounter(text)    
    text_file.close()

def find_name_in_file(fn_name, person_name):
    t_cnt = 0
    text_file = open(fn_name)
    text = text_file.read()
    print "times mentioned in file", person_name, " : "
    t_cnt = specialcount(text, person_name)
    print t_cnt
    text_file.close()
    return t_cnt
        
########## this is main ############
#fn_xx = 'C:\Users\Jeffrey\Documents\python\pytest.txt'

name_list = ["Harry", "Ron", "Hermione", "Dumbledore", "Voldemort", "Hagrid", "Snape", "James", "Neville", "McGonagall", "Sirius", "Quidditch"]
bar_list = []
my_cnt = 0

hp = 'C:\Users\Jeffrey\Documents\python\HP\HP_5.txt'
count_file(hp)

for p_name in name_list :
    my_cnt = find_name_in_file(hp, p_name)
    bar_list.append([p_name, my_cnt])


# Let sort to find most popular
bar_list.sort(key = lambda x: x[1])

print "we will plot soon"
print bar_list

