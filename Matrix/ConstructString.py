"""
Find the shortest route in a device to construct a given string.
Keypad:

A  B  C  D  E
F  G  H  I  J
K  L  M  N  O
P  Q  R  S  T
U  V  W  X  Y

Device:

    T
 L  M  R
    B

where,

T — Move up
B — Move down
L — Move left
R — Move right
M — Press OK
"""

def findPath(S):
    i = 0
    j = 0
    path = ""
    for c in S:
        r = (ord(c) - ord('A')) // 5
        c = (ord(c) - ord('A')) % 5

        while i > r:
            path += 'T'
            i -= 1

        while i < r:
            path += 'B'
            i += 1

        while j > c:
            path += 'L'
            j -= 1

        while j < c:
            path += 'R'
            j += 1

        path += 'M'

    return path

if __name__ == '__main__':
    S = 'TECHIE'
    print(findPath(S))
    # Returns BBBRRRRMTTTMLLMBMRMTRM