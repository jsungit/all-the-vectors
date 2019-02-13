# read in the vectors.txt file
# create a  list of vectors
# scale the first and last vector by 3
# add them all together and find
# that new vector
# find the norm of the final vector
# also find the dot product between the 2nd and 3rd vector
import vector as v

vecs = []
with open('vectors.txt') as f:
    for line in f:
        # vx, vy = line.strip().split(',')
        # vec = Vector(vx, vy)
        # print(vx, vy)

        # vec = v.Vector(line.strip().split(','))

        vec = line.strip().split(',')
        # vec = map(v.myfloat(vec), vec)
        vec = list(map(lambda x: float(x), vec))
        vec = v.Vector(*vec)
        vecs.append(vec)

# print(len(vecs))
# print(vecs[1])
# print(vecs)

v1 = vecs[0].scale(3)
print(v1)
print(vecs)

# vx = list[vecs[i][0] for i in len(vecs)]
# print(vx)

# num1 = [vecs.vx for vec in vecs]
# print(num1)
