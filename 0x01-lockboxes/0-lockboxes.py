#!/usr/bin/python3
"""n number of locked boxes in a list of boxes, arranged sequentially
   return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """canUnlockAll - check if all boxes can be opened
    Args:
       boxes: list of boxes
    Returns:
       True if all boxes can be opened, else False
    """
    if not boxes:
        return False
    if not isinstance(boxes, list):
        return False
    if not isinstance(boxes[0], list):
        return False
    if boxes[0] == []:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
