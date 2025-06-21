# Dynamic Array implementation
# Note: Python lists are dynamic arrays by default,
# but this is an example of what's going on under the hood.
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0 ## 最初は要素が0個
        self.arr = [0] * self.capacity ## 指定した数だけ0で埋めた配列を作る→メモリ領域の確保

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.arr[i]

    # Set n at i-th index
    ## 指定したインデックスの値を上書きする, 要素があってもnullを返す
    ### set(1, 3)なら、arr[1]を3にする
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    ## pushbackは要素があってもnullを返す
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
            
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity 
        
        # Copy elements to new_arr
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
