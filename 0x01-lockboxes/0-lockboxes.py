#!/usr/bin/python3
"""
Method to determine if all lockboxes are opened
"""


def canUnlockAll(boxes):
    """
    comments
    """
    num_boxes = len(boxes)
    unlocked_boxes = {0}
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < num_boxes and key not in unlocked_boxes:
            unlocked_boxes.add(key)
            keys.update(boxes[key])
    return len(unlocked_boxes) == num_boxes
