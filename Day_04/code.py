import os
os.system('cls')



'''
    4.1     Strings     unnutable not changable
'''



# word = "Python is a programming language."

# word2 = "Language is a key."

# print(len(word))
# print(len(word2)) 
# print(word+word2)



'''
    4.2     Slicing
'''



# print(word[:])  #   0 to ending index

# print(word[12:])    #   slicing till end
# # OR
# print(word[12:len(word)])    #   slicing till end

# print(word[12:24])  #   slicing till mention

# print(word[-9:-1])    #   slicing reverse bigger : smaller



'''
    4.2.5   String Formating
'''



# a = 5
# b = 10
# sum = a + b
# print("Sum is ",sum)

'''Normal Formating'''
# print("Sum is {}".format(200))
# print("Sum of {} & {} is := {}".format(a, b, sum))

'''Index - based formating'''
# print("\nIndex - based Formating")
# print("Sum of {0} & {1} is {2} ".format(a, b, sum))
# print("Sum of {1} & {0} is {2} ".format(a, b, sum))   #   b   a   sum     

'''Value - based Formating'''
# print("\nValue - based Formating")
# print("Value of vars {a} & {b}".format(a = 5, b = 10))

'''F-strings'''
# a = 5
# b = 10
# print(f"Sum of {a} & {b} is : = {a+b}")
# print(f"Average of {a} & {b} is : = {(a+b)/2}")



'''
    4.3     List        mutable changable
'''



# marks = [50, 60, 70, 80, 90, 100]

# print("\n",marks)

# print("\n",marks[0], marks[1], marks[2], marks[3], marks[4], marks[5])

# marks[5] = 110
# print("\n",marks)

# print("\nLength of marks : = ",len(marks))

# mix = [1,2,3,4,"abc",'a']
# print("\n",mix)

# print(marks[5]) #   only 5th value

# print(marks[:5])    # till 5th index

# print(marks[3:len(marks)])    # 3rd index to last index 

# print(marks[-5:-1])    # -5 index to -1 index in reverse order

# print(marks[::-1])



'''
    4.4     List Methods
'''



# marks = [50, 60, 70, 80, 90, 100]

# print(marks)

'''append'''
# marks.append(110)   #   append or insert value in last 

# print("append",marks)

'''insert'''
# marks.insert(5,95)  #   insert value at index 5     between 90 and 100

# print("insert",marks)

'''sort'''
# marks2 = [100, 90, 80, 70, 60, 50]  #   Unsorted List
# print("sort",marks2)

# marks2.sort()  #   Sorted the whole list
# marks2.sort(reverse = True)  #   Sorted  desc order list

# print(marks2)

'''reverse'''
# marks = [50, 60, 70, 80, 90, 100]
# marks.reverse()   #   Reverse the list's value

# print(marks)



'''
    4.5     Using Loops With Lists          [ Majorly use For Loops  because list is sequencial ]
'''



# marks = [1, 2, 3, 4, 5, 4]

# for val in marks:
#     print(val)



# x = 4 
# index = 0

# # Linear Search         traverse value until target finds 

# for val in marks:
#     if val == x:
#         print("Index Found at : = ",index)  #   OR
#         print(f"{x} found at index = {index}")
#         break
#     index += 1



'''
    4.6     Tuples in Python        Immutables  [Not changable]
'''



# marks6 = (1, 2, 3, 4, 5, 6, 'a', "abc", 3.14)

# print(marks6)
# print(len(marks6))      #   finding the length of tuple

# # marks6[2] = 10  #   gives ana error because it's immutable

# marks7 = (1)
# print(type(marks7))

# marks8 = ('a')  #   it gives string type
# print(type(marks8))

# marks9 = ('a',)  #   it gives tuple
# print(type(marks9))

# print(marks6[:])  #   0 to ending index     display all the values

# print(marks6[2:4])  #   slicing till mention

# print(marks6[2:])    #   slicing till end # OR
# print(marks6[2:len(marks6)])    #   slicing till end

# print(marks6[-9:-1])    #   slicing reverse bigger : smaller



'''
    4.7     Tuple Methods   not chngable, envirnment like list 
'''
# marks10 = (1, 2, 3, 4, 5, 6, 3.14, 4, 3, 2, 1)

'''Display all the values of tuple'''
# for val in marks10: 
#     print(val)

'''Sum of values of the tuple'''
# sum = 0
# for val in marks10: 
#     sum += val
# print(sum)

'''
Tuple Mathods
index
count
'''

'''returns 1st occurrences index'''
# print(marks10.index(4))

'''count total occurrences'''
# print(marks10.count(0))


'''
    4.8     Dictionary in Python        key value pairs, unique, changable, duplicate not allowed, unordered
'''



info = {
    "name" : "Tirth",
    "cgpa" : 8.2,
    "subjects" : ["maths","history"],
    3.14 : "pi"
}

# print(type(info))
# print(info["name"])
# info["name"] = "Raj"
# print(info["name"])
# print(info["cgpa"])
# print(info["subjects"])
# print(info[3.14])
# print(info)


'''
    4.9 Dictionary Methods
'''


'''keys()        returns all keys'''
# print(info.keys())

'''values()        retuns all values'''
# print(info.values())

'''items()        retuns (key, value)pairs'''
# print(info.items())

'''get(val)      returns val acc. to key '''
# print(info.get("cgps2"))        # it gives none no errors
# # # print(info["cgps2"])    # error

'''update(new_item)      adds new item to dict'''
# print(info)
# info.update({
#     "city" : "delhi"
# })
# print(info)



'''
    4.10        Sets in python          unique values       , set is allowed to mutable but elements are immutable      , unordered  
'''



# s = {1, 2, 3, 4, 3, 2, 5, 5, 6 }

# print(len(s))
# print(s)
# s.add(10)   #   insert 10 at last
# print(s)

# empty_set = {}      #   class dict
# print(type(empty_set))

# empty_set = set()       #   class set 
# print(type(empty_set))



'''
    4.11    Set Methods
'''

# s1 = {1, 2, 3, 4, 5, 2}

'''s1.add(val)'''
# print("add : = ",s1)
# s1.add(10)   #   insert 10 at last
# print(s1)

'''s1.remove(val)        adds a val'''
# print("Remove : = ",s1)
# s1.remove(10)   #   remove 10 at last
# print(s1)

'''s1.clear()        removes a val'''
# print("Clear : = ",s1)
# s1.clear()   #   remove 10 at last
# print(s1)       #   prints empty set()

'''s1.pop()      removes a random val'''
# s1 = {1, 2, 3, 4, 5, 2}
# print("Pop : = ",s1)
# s1.pop()   #   remove 1
# print(s1)       

'''s1.union(set2)        returns new union       all'''
# s1 = {1, 2, 3, 4, 5, 2}
# s2 = {1, 3, 5, 7, 9, 8, 7, 6}
# print("Union : = ",s1,s2)
# print(s1.union(s2))       

'''s1.intersection(set2)     returns new intersection        same'''
# print("intersection : = ",s1,s2)
# print(s1.intersection(s2))      



'''
        Practice Problem        A & B
            Students Enrolments
                Given a list of tuples with info (name, subject)

                    info = [
                        ("Alice","Math"),
                        ("Bob","Science"),
                        ("Alice","Science"),
                        ("Charlie","Math"),
                        ("Bob","Math"),
                        ("Alice","English"),
                        ("Charlie","English"),
                    ]

                    ` list all unique course
                    ` list studentws enrolled in english
                    ` create dictionary (student, set of courses)
'''

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]

'''1'''
# unique_Courses = set()
# for tup in info:
#     unique_Courses.add(tup[1])

# print("Unique Courses : = ",unique_Courses)

''' 2'''
# for name,course in info:
#     if( course == "English"):
#         print(name)

''' 3'''
# dict = {}
# for name,course in info:
#     if( dict.get(name) == None):
#         dict.update({name : set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)