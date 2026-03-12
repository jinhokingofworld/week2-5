# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

def removeDuplicates(self, nums):
    #오름차순 정렬된 배열이 인풋으로 들어옴
    #counter를 설정해놓고
    #for로 돌아가면서 같으면 삭제 후 append(_)추가. 다르면 새로운 counter.

    counter = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == counter:
            nums.remove(i)
            nums.append('_')
        else:
            counter = nums[i]
    
    return nums

removeDuplicates([1,1,2])
