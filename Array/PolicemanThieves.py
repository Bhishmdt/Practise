"""
Given an array of size n that has the following specifications:

    Each element in the array contains either a policeman or a thief.
    Each policeman can catch only one thief.
    A policeman cannot catch a thief who is more than K units away from the policeman.
"""

def policeThief(arr, k):
    pi = -1
    ti = -1

    result = 0

    for i in range(len(arr)):
        if arr[i] == 'P':
            pi = i
            break
    for i in range(len(arr)):
        if arr[i] == 'T':
            ti = i
            break

    if pi == -1 or ti == -1:
        return 0

    while pi < len(arr) and ti < len(arr):
        if abs(pi - ti) <= k:
            result += 1

            pi += 1
            while pi < len(arr) and arr[pi] != 'P':
                pi += 1

            ti += 1
            while ti < len(arr) and arr[ti] != 'T':
                ti += 1

        else:
            if ti < pi:
                ti += 1
                while ti < len(arr) and arr[ti] != 'T':
                    ti += 1
            else:
                pi += 1
                while pi < len(arr) and arr[pi] != 'P':
                    pi += 1

    return result

if __name__ == '__main__':
    arr = ['P', 'T', 'T', 'P', 'T']
    print(policeThief(arr, 2))
    # Returns 2

    arr = ['T', 'T', 'P', 'P', 'T', 'T', 'P']
    print(policeThief(arr, 2))
    # Returns 3

