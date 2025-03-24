#Intution: Creta a hashmap for tracking frequency of Each ELement in the given array
#Solution:1 Create a hashmap for tracking frequency of Each ELement in the given array
def TopKFreqElements(arr, k):
    freqMap  = {}
    for num in arr:
        freqMap[num]= freqMap.get(num,0)+1 
        #Decoding Get Method:syntax: get(KeyName, value)
        #KeyName: Required. The keyname of the item you want to return the value from
        #value: Optional. A value to return if the specified key does not exist.Default value None
        #because we are assigning this to freqMap[num] if num is not present in the dictionary it will return 0
        #otherwise if you make z = freqMap[num] then z will have the value of freqMap[num] like 1.
    #Now we have the frequency of each element in the array we cant sort the dictionary because it will make complexity O(nlogn)
    #So we will make dictionary with frequency as Key
    Buckets = [[] for _ in range(len(arr)+1)]
    res = []
    #ading extra 1 element to the bucket cbacause i case of edge cases like when we have only 1 element in the array 
    #then we will have only 1 bucket which maps to 0 frequency so we will create buckets with adding 1 extra element
    for num, freq in freqMap.items():
        Buckets[freq].append(num)
    
    for i in range(len(Buckets)-1,0,-1):
        # we are traversing from len(Buckets to 0 not -1 because , if ar full of same number then we will len(arr) bucket will be filled
        # 0 is not possible in frequency so we will start from len(arr) to 0
        for num in Buckets[i]:
            res.append(num)
            if len(res)==k:
                return res
            


if __name__ == "__main__":
    arr = [1,1,1,2,2,3]
    k = 2
    print(TopKFreqElements(arr,k))