meat = ["ham", 3.99, 50, "sliced"] # Type, price, 
cheese = ["Cheddar", 5.49, 100, "Sharp"]

deli_dept = [meat,cheese]
print("Initial deli list:", deli_dept)
if meat[2] < 100:
    meat[2] = 100

deli_dept.sort()
print("Updated Deli List:", deli_dept)
