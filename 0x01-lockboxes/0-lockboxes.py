#!/usr/bin/python3
def canUnlockAll(boxes):

    print(boxes)
    """"
        taking boxes 
            create set of keys 
            go to box0
             get all keys and save it in setofkeys
            start opening boxes from set of keys
    """

    print("boxs: ", boxes)
    print("The total of boxes: ", len(boxes))
    setofkeys = []
    counter = 0
    Total_boxes = len(boxes)
    for key in boxes[0]: 
        if key < Total_boxes and key not in setofkeys and key > 0:
            setofkeys.append(key)
            counter +=1
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if key < Total_boxes and key not in setofkeys and key > 0:
                setofkeys.append(key)
                counter +=1
        index += 1
    print("Total keys: ", counter)
    if (counter == Total_boxes-1):
        return True 
    else: 
        return False