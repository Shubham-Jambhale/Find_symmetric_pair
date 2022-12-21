def findSymPairs(arr):
    dicti = {}
    result=[]
    
    for i in range(len(arr)):

        firstEle= arr[i][0]
        secondEle = arr[i][1]
        if secondEle in dicti.keys() and dicti[secondEle]==firstEle:
            result.append([secondEle,firstEle])
        else: 
            dicti[firstEle] = secondEle
    return result