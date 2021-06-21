"""
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.
"""


def maximumUnits(boxTypes, truckSize) -> int:
    #Sort by number of units
    boxTypes.sort(key=lambda x: -x[1])
    result = 0
    for num_box, upb in boxTypes:
        if truckSize > num_box:
            truckSize -= num_box
            result += num_box * upb
        else:
            result += truckSize * upb
            return result
    return result

if __name__ == '__main__':
    boxTypes = [[1, 3], [2, 2], [3, 1]]
    truckSize = 4
    print(maximumUnits(boxTypes, truckSize))
    # Returns 8

    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    print(maximumUnits(boxTypes, truckSize))
    # Returns 91