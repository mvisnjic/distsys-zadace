def dz_func3(l):
    assert isinstance(l, list)
    assert all(isinstance(n, dict) for n in l)
    # assert all(isinstance(n, dict) for n in l)
    for x in l:
        assert(x["cijena"] and x["naziv"] and x["kolicina"])
    return {"ukupno": {"artikli": [elem["naziv"] for elem in l]}, "cijena": sum([elem["cijena"]*elem["kolicina"] for elem in l])}    
    
print(dz_func3([{"cijena":8,"naziv":"Kruh","kolicina":3}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}]))