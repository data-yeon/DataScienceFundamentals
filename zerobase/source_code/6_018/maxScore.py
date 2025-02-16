class MaxAlgorithm:
    # 클래스 초기화 메서드 (생성자)
    def __init__(self, ns):
        self.nums = ns  # 전달받은 리스트(ns)를 클래스 내부에서 사용할 변수(self.nums)에 저장
        self.maxNum = 0  # 최댓값을 저장할 변수 초기화 (0으로 설정)
        self.maxNumIdx = 0  # 최댓값이 위치한 인덱스를 저장할 변수 초기화 (0으로 설정)

    # 리스트에서 최댓값과 그 인덱스를 찾는 메서드
    def setMaxIdxAndNum(self):
        self.maxNum = self.nums[0]  # 우선 리스트의 첫 번째 값을 최댓값으로 설정
        self.maxNumIdx = 0  # 첫 번째 값의 인덱스를 최댓값 인덱스로 설정

        # 리스트의 모든 요소를 확인하면서 최댓값 찾기
        for i, n in enumerate(self.nums):  # i는 인덱스, n은 리스트의 값
            if self.maxNum < n:  # 현재 저장된 최댓값보다 더 큰 값이 발견되면
                self.maxNum = n  # 새로운 최댓값으로 업데이트
                self.maxNumIdx = i  # 최댓값의 위치(인덱스)도 업데이트

    # 최댓값을 반환하는 메서드
    def getMaxNum(self):
        return self.maxNum  # 최댓값 반환

    # 최댓값이 위치한 인덱스를 반환하는 메서드
    def getMaxNumIdx(self):
        return self.maxNumIdx  # 최댓값의 인덱스 반환