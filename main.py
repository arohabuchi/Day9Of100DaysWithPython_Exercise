########################################## DICTIONARY IN PYTHON ########################################################
#Dictionary i an example of a key-value store also known as mapping
d={}
d[1]='hi'
d[2]='hg'
d[3]='ike'
d['ikes']=7
print(d)

#to delete an item
del d['ikes']
print(d)

#iterating over a dictionary
for k,v in d.items():
    print(k, ":", v)

#merging a dictionary
d2={'d2': 72, 'd22': 89, 'd222': 90}
dd2 ={**d, **d2}
print(dd2)

#accessing keys and value
ddd = {1: 'hi', 2: 'hg', 3: 'ike', 'd2': 72, 'd22': 89, 'd222': 90}
for k in ddd:
    print(k)
print(ddd.keys())
print(ddd[2])

#creating dictionary
md = {'a':[1,2,3], 'b':40,'c':['hi', 'hello', 'good']}
print(md)

cdd ={'name':'sammy black','gender':'male', 'age':'99'}
det= {'d2': 72, 'd22': 89, 'd222': 90}
pt = cdd['name'] + " a " + cdd['age'] + ' years old man'
print("the numbers are", det['d2'],det['d22'], " and ", det['d222'])
print(pt)


############################################ LIST IN PYTHON #########################################################
a =[1,22,3,4,7,8,9,0]
print(a)

################### List method ####################

############ APPEND
#append same type
a.append(22)
print(a)

#append different type
hi ="hii"
a.append(hi)
print(a)

#append another list
b=[44,90,60]
a.append(b)
print(a)

###################### Index
a=[2,2,34,4,7,8,9,9,2]
print(a.index(9))

#we also have other methon like: pop, count, remove,clear, sort, reverse
a.pop() #remove the last item
a.pop(2)# remove item at index of two
print(a)
a.count(9)
print(a)
a.sort()
print(a)
a.remove(2)
print(a)
a.reverse()
print(a)
a.clear()
print(a)

#element deletion
a=[1,2,3,4,5,67,7,8,9]
del a[5] #delete index of 5
print(a)
del a[6:] #delete from index of 6 up
print(a)
del a[::2] #delete odd index
print(a)
del a[:] # delete all
print(a)

#checking if list is empty
a=[]
if not a:
    print("empty list")

#iterating over a list
mylst= [1,2,3,4,'leo','tt','hi',90]
for i in mylst:
    print(i)

print(len(mylst))

#checking if an item i in a list
print('leo' in mylst)


# Any and All (if any item in a list evaluate to true and if any item in a list evaluate to true
a=[1,2,3,4,0,9,8]
aa=['hi',9,8,0]
print(any(a))
print(all(a))
g=a+aa  #concatenation of list
print(g)

#Remove duplicate value

a=[1,1,2,2,3,4,4,7,8,8,9,9,0,0]
au =list(set(a))
print(au)

#list slicing
lt=[1,2,3,4,1,222,3,4,7,8,9,0,7,8,9,9]
print(lt[9:])
print(lt[::2])
slt=lt[3:7]
print(slt)

############################################### FILTER #############################################################
nam=['hi','hii','hiii','hiiii']
def longn(name):
    return  len(name)>3

ltt=list(filter(longn, nam))
print(ltt)

########################################### HEAPQ #####################################################################

import  heapq
nm =[90,89,890,878,789,900,897,777]
v = heapq.nlargest(2, nm)
low = heapq.nsmallest(2, nm)
print(v)
print(low)
peps =[
     {'name': 'tochi', 'gender': 'female', 'age': 99},
     {'name': 'tobe', 'gender': 'male', 'age': 98},
     {'name': 'ike', 'gender': 'female', 'age': 909},
     {'name': 'chi', 'gender': 'female', 'age': 89},
     {'name': 'tbliz', 'gender': 'female', 'age': 100}
]
oldest= heapq.nlargest(2, peps, key=lambda s:s['age'] )
print(oldest)