class Solution:   
    # Reverse an array 
    def reverseArray(self, arr1, n):
        for i in range(n - 1, -1, -1):
            print(arr1[i], end=" ")

if __name__ == '__main__':
    n = int(input())
    arr1 = list(map(int, input().split()))
    Obj = Solution()
    Obj.reverseArray(arr1, n)
