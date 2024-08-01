#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each box may
contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists, where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, else False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    
    return len(unlocked) == len(boxes)
