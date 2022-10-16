def func1(list):
    return [y if y%4==0 else round(y**0.5,2) for y in list]

#print(func1([213,14,12,6543,232]))

def func2(list, list2):
    return {k:v for k,v in zip(list,list2) if len(list) == len(list2)}

#print(func2([1,2,3], [4,3,2]))

def func3(list):
    return {y for d in list for _,y in d.items()}

#print(func3([{"ip":"192.168.3.1"}, {"ip":"10.0.0.0"}, {"ip":"127.0.0.0"}]))