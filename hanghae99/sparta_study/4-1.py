def merge_and_sort(arr1, arr2):
    # 배열을 합침
    merged_array = arr1 + arr2

    # 합쳐진 배열을 오름차순으로 정렬
    merged_array.sort()

    return merged_array

# 테스트 예시
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_and_sort(arr1, arr2))  # [1, 2, 3, 4, 5, 6]

arr3 = [10, 5, 15]
arr4 = [4, 11, 2]
print(merge_and_sort(arr3, arr4))  # [2, 4, 5, 10, 11, 15]