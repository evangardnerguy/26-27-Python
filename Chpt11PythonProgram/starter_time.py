##
#  Section 11.7 Worked Example: Computing Travel Time
#  A robot drives along a road (fast), then cuts straight across rocky
#  terrain (slow) to reach an item. Compute the total travel time.
#
#  HAND CALCULATION (dx = 10 km, dy = 3 km, l1 = 6 km, s1 = 5 km/h, s2 = 2 km/h):
#    Segment 1 time   = 1.2
#    Segment 2 length = 5.0
#    Segment 2 time   = 0.4
#    Total time       = 1.6 hours
#
from math import sqrt

# Short hand-calculation names (dx, s1...) become DESCRIPTIVE names in code.
distanceX = input("Enter distance x: ")
distanceY = input("Enter distance y: ")
distanceTotal = sqrt((distanceX ** 2) + (distanceY ** 2))
print("The length of the slope is ", distanceTotal)
# ---------------------------------------------------------------
# TRY IT
#  1. Run with 10, 3, 6, 5, 2.  Does the program match the hand value 3.7?
#  2. By hand: what if the robot drives 8 km on the road instead of 6?
#     (Hint: segment 2 becomes a 2-3 right triangle.) Then check it.
#  3. Rewrite the import as "import math". What else must change?
# ---------------------------------------------------------------