def anon(a,b):
    return lambda x:a>b
function = anon(9,5)
print(function(0))