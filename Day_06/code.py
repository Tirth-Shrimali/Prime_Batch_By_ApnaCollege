import os
os.system("cls")



'''
    6.2     Operation in files
            Modes in file operation
                by default when all operation is done then file close automatically
'''



# f = open("sample.txt","r")      #   File object 
 
# data = f.read()
# print(data)
# data = f.readline()     #   read line by line
# print(data)
# print(type(data))
# f.close()


# f = open("example.txt","w")
# f.write("hi there text to overwrite \nthe complete data .")
# f.close

# f = open("example.txt","r")
# data = f.read()
# f.close()
# print(data)



'''
    6.3     With keyword
'''



# with open("sample.txt","r") as f:
#     data = f.read()
#     print(data)
#     print(len(data))



'''
    6.4     Delete Files
'''



# import os
# os.remove("example.txt")



'''
    6.5     File Operations Modes
'''



''' r = reading [default] '''



# with open ("sample.txt","r") as f :
#     print(f.read())



''' w = writing, truncates files first , replace, overwrite'''



# with open ("sample.txt","w") as f :
#     f.write("hi")

# with open ("sample.txt","r") as f :
#     print(f.read())



''' x = creates new and open for writing , if exists then gives error '''



# with open("sample2.txt","x") as f:
#     f.write("Some randome text is here ")



''' a = writing, appends at end '''



# with open("sample.txt","a") as f:
#     f.write("\nAppend mode")



''' b = binary mode'''



# with open("sample2.txt","b") as f:
#     f.write("\nAppend mode")



''' t = text mode [default]'''



# with open("sample.txt","rt") as f:
#     f.write("\ntext mode")


''' + = opens disk file for update ( r& w )'''



# with open("sample.txt","r+")as f:
#     f.write("122333")
#     print(f.read())

# with open("sample.txt","a+")as f:
#     f.write("122333")
#     print(f.read())

# with open("sample.txt","w+")as f:
#     f.write("122333")
#     print(f.read())



'''
    6.6, 6.7, 6.8, 6.9, 6.10
'''

# data = True
# line = 1
# word = "store"

# with open("sample.txt","r")as f :
#     while data:
#         data = f.readline()
#         if word in data:
#             print(f"{word} found at {line}")
#             break
#         line += 1
#     print(data)




'''exception handling
        try, except, else, finally
'''







# try:
#     x = int(input("Enter x : "))
#     ans = 10 / x
# except ZeroDivisionError:
#     print("Divide by 0 is not allowed")
# except ValueError:
#     print("Invalid input")
# else:
#     print(f"ans : = {ans}")
# finally:        # Every times executes
#     print("End of program")


'''list comprehension'''

# Normal trick  
# squares =[]

# for i in range(6):
#     squares.append(i*i)
# print(squares)

# list coprehenison
# sq = [i*i for i in range(6)]
# print(sq)

# # sq = [i*i for i in range(1,6,2)]
# sq = [i*i for i in range(6) if i%2!=0]
# print(sq)

# Negative num replace by 0
# nums = [-2, -4, -6, -8, 9, 4, 5, 6, 7] 
# print(nums)
# nums = [0 if val < 0 else val for val in nums]
# print(nums)

# words = ["hello", "python", "college"]
# print(words)
# words = [val.upper() for val in words]
# # print(words.upper)
# print(words)



'''json module 
JavaScript Object Notation'''
import json

# last s for strings

'''json.loads'''
# json_str = '{"name" : "Tirth", "isTeacher" : true}' #   true convert into True      ||      None convert into null

# py_obj = json.loads(json_str)
# print(type(py_obj), py_obj)


'''json.dumps'''
# py_obj = {
#     "name" : "Tirth",
#     "isTeacher" : True
# }

# json_str = json.dumps(py_obj)
# print(type(json_str), json_str)


'''json.load    in files'''
# with open("data.json", "r")as f:
#     py_obj = json.load(f)
#     print(py_obj)


'''json.dump    in files'''
py_obj = {
    "name" : "Tirth",
    "isTeacher" : True,
    "age" : 18
}
with open("data.json", "w")as f:
    json.dump(py_obj, f, indent=10, sort_keys = True )     #   idsentation in files 10 spaces 
    print(py_obj)