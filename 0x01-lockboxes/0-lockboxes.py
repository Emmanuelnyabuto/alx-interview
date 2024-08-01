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
    if not isinstance(boxes, list) or any(not isinstance(box, list) for box in boxes):
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    
    return len(unlocked) == len(boxes)

# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
