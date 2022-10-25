from tasks import add

res = add.apply_async((1, 2))
# Status
print(res.ready())

# Backend URL
print(res.backend)

# Task async ID
print(res.id)

# Will get the result, once after the processing is done. 
print(res.wait())