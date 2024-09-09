num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
set_a = set(map(int,input().split()))
if num_set.issuperset(set_a):
    print("Superset")
elif num_set.issubset(set_a):
    print("Subset")
elif num_set.isdisjoint(set_a):
    print("Disjoint Set")
