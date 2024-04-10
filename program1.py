def rotate_array(arr, K):
    # Rotate array
    N = len(arr)
    rotated = [0] * N
    
    K = K % N
    
    for i in range(N):
        rotated[(i + N - K) % N] = arr[i]
    
    return rotated

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

rotated_array = rotate_array(arr, K)

print(*rotated_array)