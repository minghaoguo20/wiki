numbers = [1, 2, 3, 4, 5]
fn = lambda x: x**2
square = list(map(fn, numbers))
print(square) # [1, 4, 9, 16, 25]
