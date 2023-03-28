"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
import datetime
Todo.objects.create(content='실습 제출', priority=5, completed=False, deadline=datetime.datetime.now())

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
Todo.objects.create(content='데일리 설문(오후) 제출', deadline=datetime.datetime.now())

"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='설거지', deadline='2023-03-28')
Todo.objects.create(content='빨래', deadline='2023-03-29')
Todo.objects.create(content='복습', priority=5, deadline='2023-03-28')
Todo.objects.create(content='화장실 청소', priority=4, deadline='2023-03-31')
Todo.objects.create(content='장보기', deadline='2023-03-29')

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('pk')

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by(-'priority')

"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
first = Todo.objects.get(pk=1)
print(first.pk)
print(first.content)
print(first.priority)
print(first.deadline)
print(first.created_at)