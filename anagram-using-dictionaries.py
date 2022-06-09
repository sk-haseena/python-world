#checking whether the given two strings are anagram to each other or not by using dictionories

s1=input("enter string1=")
s1=s1.lower()
dict_1=dict()
for char in s1:
    if char not in dict_1:
        dict_1[char]=1
    else:
        dict_1[char]=dict_1[char]+1
print(dict_1)

s2=input("enter string2=")
s2=s2.lower()
dict_2=dict()
for char in s2:
    if char not in dict_2:
       dict_2[char]=1
    else:
       dict_2[char]=dict_2[char]+1
print(dict_2)

if  s1 is None or s2 is None or len(s1) != len(s2):
	 print("not a anagram")
elif  dict_1 == dict_2:
	print("anagram")
else:
		print("not a anagram")
