#!/usr/bin/python3
'''
A method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    Ascertains if all boxes can be unlocked given\
    that the first box is unlocked.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box = unseen_boxes.pop()
        if not isinstance(box, int) or box < 0 or box >= n:
            continue
        if box not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box])
            seen_boxes.add(box)
    return len(seen_boxes) == n
