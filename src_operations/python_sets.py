# Sets cannot have duplicates
X = {1,2,3,4,3,2}

# We can make a set from a list
Y = set([1,2,3,4,5])

print(f"El tipo es: {type(X)} y está conformado de {X}")
print(f"El tipo es: {type(Y)} y está conformado de {Y} \n")

X.add(8)
X.update([9,10,11])
X.discard(3)
print(f"Modificamos el conjunto X, y obtenemos {X} \n")

# UNION
print("    UNION    \n")
xy_union = X.union(Y)
print(f"Si unimos {X} con {Y} obtenemos {xy_union}")
print(f"Tambien funciona si hacemos 'X|Y', por ejemplo: {X|Y} \n")

# Intersection of sets
print("    INTERSECTION    \n")
xy_intersection = X.intersection(Y)
print(f"Si los conjuntos {X} y {Y} se intersectan, obtenemos {xy_intersection}")
print(f"Tambien funciona si hacemos 'X&Y', por ejemplo: {X&Y} \n")

# Difference beetwen sets
print("    DIFFERENCE    \n")
x_diff_from_y = X.difference(Y)
print(f"La diferencia de {X} con {Y} es {x_diff_from_y}")
print(f"La diferencia de {Y} con {X} es {Y-X} \n")

# Symetric difference
print("    SYMMETRIC DIFFERENCE    \n")
xy_sym_difference = X.symmetric_difference(Y)
print(f"La diferencia simétrica de {X} y {Y} es {xy_sym_difference}")
print(f"También funciona si hacemos 'X^Y', por ejemplo: {X^Y} \n")

# Set cannot have mutable items, par example {1,2,[3,4]} is a mutable list, and
# it will cause an error.

# To distinguish set and dictionary while creating an empty list:
a = {}
b = set()

print("El tipo es: ", type(a), "y está conformado de ", a)
print("El tipo es: ", type(b), "y está conformado de ", b)
