def solution(numbers, target):
    answer = 0
    #1 2 4 8
    arr = []
    for i in range(1, len(numbers)+1):
        temp = [0]*pow(2, i)
        arr.append(temp)
    #print(arr)
    for i in range(len(numbers)):
        if i == 0:
            arr[i][0] = -1*numbers[0]
            arr[i][1] = numbers[0]
        else:
            for j in range(0, len(arr[i])-1, 2):
                arr[i][j] = arr[i-1][j//2] - numbers[i]
                arr[i][j+1] = arr[i-1][j//2] + numbers[i]
    #print(arr)
    for i in arr[len(arr)-1]:
        if i == target:
            answer += 1
    return answer