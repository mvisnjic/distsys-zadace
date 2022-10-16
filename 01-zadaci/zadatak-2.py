def dz_func2(l, d):
    assert isinstance(l, list)
    assert isinstance(d, dict)
    assert all(isinstance(n, int) for n in l)
    
    if len(l) != len(d):
        return 'length !='
    
    keys = [key for key in d]
    return {keys[k]:v if v>=5 and v<=10 else -1 for k,v in enumerate(l)}
    
    
print(dz_func2([8,7,1], {1:2,2:1,3:2}))