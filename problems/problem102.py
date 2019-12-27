# Problem 102 : Triangle containment

# file which contains the triangle coordinates
triangle_file = "triangle.txt"
# read the triangle coordinates
with open(triangle_file, "r") as triangleFile:
    triangles = triangleFile.read()
# creation of a list of lists which includes the 3 points coordinates (tuples)
triangles = triangles.strip().split("\n")
list_triangles = []
for triangle in triangles:
    triangle = triangle.strip().split(',')
    list_triangles.append([(int(triangle[0]), int(triangle[1])),
                           (int(triangle[2]), int(triangle[3])),
                           (int(triangle[4]), int(triangle[5]))
                           ])


def contain_origin(triangle):
    """
    this function takes a triangle, i-e 3 tuples, coordinates of triangle's vertices,
    and returns whteher or not the origin is inside the triangle.
    We search the barycentric coordinates of the origin :
    O = A + (B-A)*s + (C-A)*t
    if 0 <= s <= 1 and 0 <= t <= 1 and s+t<=1, the origin is inside the triangle
    """
    s = 0
    t = 0
    [A, B, C] = triangle
    if B[0] != A[0]:
        if C[0] != A[0]:
            if not (A[1] == 0 and B[1] == 0 and C[1] == 0):
                t = (B[1]*A[0]-A[1]*B[0])/(C[1]*(B[0]-A[0]) +
                                           B[1]*(A[0]-C[0])+A[1]*(C[0]-B[0]))
                s = ((A[0]-C[0])*t-A[0])/(B[0]-A[0])
        else:
            if C[1] != A[1]:
                s = A[0]/(A[0]-B[0])
                t = (A[1]*B[0] - B[1]*A[0])/((A[0]-B[0])-(C[1]-A[1]))
    else:
        if A[0] != C[0]:
            t = A[0]/(A[0]-C[0])
            s = (A[1]*C[0]-C[1]*A[0])/((A[0]-C[0])*(B[1]-A[1]))
    if 0 <= s <= 1 and 0 <= t <= 1 and 0 <= s+t <= 1:
        return True
    return False


# count of every triangle with the required property (origin inside the triangle)
counter = 0
for triangle in list_triangles:
    if contain_origin(triangle):
        counter += 1

print(counter)

# Result 228
