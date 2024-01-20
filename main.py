#Task_1
name = [
    ("Ali",
     2 ,
     [{"name": "Ali", "Age":21},
                   {"Name": "Vali", "Age": 19}]
         )]
result = 0


def add(name, result):
    for x in name:
        for y in x[-1]:
            result += y["Age"]
            print(result)



add(name, result)






lst = ["aziza", "kiyik", "anna", "Dilso'z"]


def isPalendrom(str):
    is_Palendrom = False
    i = 0
    while i < len(str)/2:
        if str[i]==str[len(str)-1-i]:
            is_Palendrom = True
        else:
            return False
        i += 1
    return is_Palendrom

# print(isPalendrom('aziza'))
j=0;
list = []
while j < len(lst):
    if isPalendrom(lst[j]) == True:
        print(list)
        list.append(lst[j])
    j += 1
print(list)








