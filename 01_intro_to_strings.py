# string is immutuble, we can not change the string after one time initialization
name= "harry"
# string can be written as """harry""" or 'harry' or "harry" 
# negative indexing=,-5,-4-3,-2,-1
print(name[-4:-1])
print(name[1:4])
# positive indexing=0,1,2,3,4
# string sliceing
namesort=name[0:3]#start from index 0 all the way till 3(excluding 3)
print(namesort)
character1=name[1]
print(character1)

print(name[:4]) #starting index is 0
print(name[1:])#is same as print(name[1:5])
print(name[1:5])
