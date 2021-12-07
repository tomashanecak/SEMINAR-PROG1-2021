# Tuto funkci implementuj.
def is_face_on_photo(photo):
    segment = ["", "", "", ""]
    for i in range(len(photo) -1):
        for j in range(len(photo[0]) -1):
            segment[0] = photo[i][j]
            segment[1] = photo[i][j+1]
            segment[2] = photo[i+1][j]
            segment[3] = photo[i+1][j+1]

            print(segment)
            
            if "f" in segment and "a" in segment and "c" in segment and "e" in segment:
                return True
    return False


# Testy:
print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
print(is_face_on_photo([['x', 'a', 'x', 'x'], ['f', 'e', 'x', 'x'], ['x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x']]))  # False

# def is_face_on_photo(photo):
#     for i in range( len(photo) - 1 ):
#         for j in range( len(photo[0]) - 1 ):
#             face = ['f','a','c','e']
#             if photo[i][j] in face: face.remove(photo[i][j])
#             if photo[i][j + 1] in face: face.remove(photo[i][j + 1])
#             if photo[i + 1][j] in face: face.remove(photo[i + 1][j])
#             if photo[i + 1][j + 1] in face: face.remove(photo[i + 1][j + 1])
            
#             if len(face) == 0:
#                 return True
#     return False