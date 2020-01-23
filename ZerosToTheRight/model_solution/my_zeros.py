hm = [1, 4, 7, 23, 6, 8, 0, 0, 4, 6, 0, 4, 0, 9, 5, 0]

def zeros(arr):
    newarr = []
    for x in arr:
        if x > 0:
            newarr.append(x)
    count = len(newarr)
    for i in range((len(arr) - count)):
        newarr.append(0)

    print("Output count: ", count, "\nNew array: ", newarr)

    return count


zeros(hm)