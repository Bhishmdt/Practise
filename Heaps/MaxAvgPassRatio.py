"""
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer
array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students,
but only passi number of students will pass the exam.
You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to
pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a
way that maximizes the average pass ratio across all the classes.
The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total
number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
Return the maximum possible average pass ratio after assigning the extraStudents students.
"""

from heapq import *

def maxAverageRatio(classes, extraStudents):
    #Find the gain for increasing passing student by 1 for each class
    heap = [(x / y - (x + 1) / (y + 1), x, y) for x, y in classes]
    heapify(heap)

    while extraStudents:
        gain, x, y = heappop(heap)
        x, y = x + 1, y + 1
        heappush(heap, (x / y - (x + 1) / (y + 1), x, y))
        extraStudents -= 1
    total = 0
    for _, x, y in heap:
        total += x / y
    return total / len(heap)

if __name__ == '__main__':
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    print(maxAverageRatio(classes, extraStudents))
    #Returns 0.78333

    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    print(maxAverageRatio(classes, extraStudents))
    #Returns 0.53485