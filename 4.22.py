def anon(a):
    return lambda x: a%2==0
function = anon(4)
print(function(0))