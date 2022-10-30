import asyncio
import time 
import os
async def afun1(listOfNames):
    assert isinstance(listOfNames, list)
    time.sleep(0.2)
    return [{"naziv": name, "velicina":os.path.getsize(name+'.txt')} for name in listOfNames]

def fun2(listOfNames):
    assert isinstance(listOfNames, list)
    for name in listOfNames:
        f = open(name+'.txt', "w")
        for i in range(10000):
            f.write(f'{i+1}\n')
        
        
async def main():
    listNames = []
    for i in range(1,4):    
        name = f'datoteka{i}'
        _createFiles = open(name + '.txt', "w")
        listNames.append(name)
    
    var1 = asyncio.create_task(afun1(listNames))
    fun2(listNames)
    res = await asyncio.gather(var1)
    print(res)
    
if __name__ == "__main__":
    asyncio.run(main())