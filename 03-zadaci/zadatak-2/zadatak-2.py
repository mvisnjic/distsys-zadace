import asyncio
import psutil
import numpy as np
import time

async def afun1():
    arr = []
    for _ in range(10):
        time.sleep(0.9)
        arr.append(np.random.normal(size=(1000000)))
    return arr

async def afun2():
    return psutil.cpu_percent(10)                   
async def main():
    fun1 = await afun1()
    fun2 = await afun2()
    print(fun1)
    print(fun2)
if __name__ == "__main__":
    asyncio.run(main())            