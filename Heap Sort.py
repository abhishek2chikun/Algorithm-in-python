class HeapSort:
    def __init__(self,array):
        self.arr=self.build_heap(array)
#Time Complexity O(N)
    def build_heap(self,array):
        height=(len(array)-2)//2
        for i in reversed(range(height)):
            self.HeapDown(i,len(array)-1,array)
        return array
#Time Complexity O(logN)
    def HeapDown(self,curr,end,array):
        left=curr*2+1
        while left<=end:
            right=curr*2+2 if curr*2+2<=end else -1
            if right!=-1 and array[right]<array[left]:
                toswap=right
            else:
                toswap=left
            if array[toswap]<array[curr]:
                self.swap(curr,toswap,array)
                curr=toswap
                left=curr*2+1
            else:
                break
    def swap(self,x,y,array):
        array[x],array[y]=array[y],array[x]

#Time Complexity O(NlogN)
    def Heap_sort(self):
        for i in reversed(range(len(self.arr))):
            self.arr[0],self.arr[i]=self.arr[i],self.arr[0]
            self.HeapDown(0,i-1,self.arr)
        return f"{self.arr}"
    
arr1=[2,13,1,20,49,56,50,100]
arr2=[100,20,30,40,500,60,200,1,90,30,1000]
h1=HeapSort(arr1)
print(h1.arr)
print(h1.Heap_sort())
print()
h2=HeapSort(arr2)
print(h2.arr)
print(h2.Heap_sort())
