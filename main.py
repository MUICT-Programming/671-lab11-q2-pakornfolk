# YOUR CODE HERE
n = int(input())
lst1=[]
lst2 = []
upgrade_list=[]
def summation (n):
    for i in range(n):
        list1 = int(input())
        lst1.append(list1)
    for i in range(n):
        list2 = int(input())
        lst2.append(list2)
        upgrade_list.append(lst1[i]+lst2[i])
    return upgrade_list
def find_min_max(upgrade_list):
    min_value = min(upgrade_list)
    max_value = max(upgrade_list)
    return min_value,max_value
print(summation(n))
print(find_min_max(upgrade_list))
