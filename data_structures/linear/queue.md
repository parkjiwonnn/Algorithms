# 큐

선입선출(First In First Out): 가장 먼저 들어온 데이터가 먼저 나가는 구조

### 큐 종류

#### 리스트

구현이 간단하지만 요소가 많아질수록 성능 저하

```
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.pop(0)) # 1
print(queue) # [2, 3]
```

#### collections.deque

deque(double-ended queue): 양쪽 끝에서 빠르게 삽입과 삭제를 할 수 있는 자료구조  
큐와 스택으로 모두 사용 가능하며 삽입과 삭제가 매우 빠름  
하지만 다른 데이터 구조에 비해 메모리 사용이 많을 수 있음

```
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft()) # 1
print(queue) # deque([2, 3])

queue.appendleft(0)
print(queue) # deque([0, 2, 3])
queue.extend([4,5]) # 주어진 iterable의 모든 요소를 덱의 오른쪽 끝에 추가
print(queue) # deque([0, 2, 3, 4, 5])
queue.rotate(2) # 덱을 n만큼 회전시킴, n이 양수이면 오른쪽, 음수이면 왼쪽으로 회전
print(queue) # deque([4, 5, 0, 2, 3])
queue.clear() # 덱의 모든 요소 제거
print(queue) # deque([])
```
