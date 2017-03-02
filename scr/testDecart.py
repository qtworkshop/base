

# colors = ["red", "black"]
# sizes = [1, 2, 3]
#
# decart = tuple((s, c) for c in sizes for s in colors)
# print(decart)


a, q, *rest, b, w = range(5)
print(a, q)
print(b, w)
print(rest)

a = (
    ("point1", 15, (100, 200)),
    ("point555", 25, (10, 20)),
    ("point3", 35, (50, 70)),
     )

for i in a:
    name, radius, (x, y) = i
    if x < 60:
        print("name - {:9}; radius - {:3}".format(name, radius))