name = 'abc'
#name2 = 'a' + 'b' +'c'
name2 = 'join'
print(name)
if name==name2:
    print('both are equal')
else:
    print('both not equal')
if name is name2:
    print('They are same')
else:
    print('They not same')
    print(id(name), id(name2))
    if name is not name2:
        print('they are two value')
        x = 2
        print(x)
        y = 3/4
        print(y)
        if x==y:
            print('both')
        else:
            print('not same')
            if x is y:
                print('This relly true')
            else:
                print('may be true')
                print(id(x),id(y))
