my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)
print(set(my_list))
print(len(set(my_list)))