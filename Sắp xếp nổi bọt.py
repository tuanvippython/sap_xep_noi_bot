# Sử dụng hàm split để nhập dãy số
list = input("Nhập dãy số nguyên, cách nhau bằng dấu cách: ").split()
a = [int(num) for num in list]
print("Dãy số vừa nhập là: ",a)

print("----Dãy số sau khi sắp xếp tăng dần----")

# Sử dụng vòng lặp for với biến i chạy từ vị trí đầu tiên đến cuối danh sách 
for i in range(len(a)):
    # Sử dụng vòng lặp for với biến j chạy từ vị trí đâu tiên đến giá trị gần cuối (vì giá trị cuối đã được sắp xếp và là giá trị lớn nhất nên không xếp nữa)
    for j in range(len(a) - i - 1):
        # Nếu giá trị đứng trước lớn hơn giá trị phía sau nó thì đổi chỗ cho nhau
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)

print("----Dãy số sau khi sắp xếp giảm dần----")

# Sử dụng vòng lặp for với biến i chạy từ vị trí đầu tiên đến cuối danh sách 
for i in range(len(a)):
    # Sử dụng vòng lặp for với biến j chạy từ vị trí đâu tiên đến giá trị gần cuối (vì giá trị cuối đã được sắp xếp và là giá trị lớn nhất nên không xếp nữa)
    for j in range(len(a) - i - 1):
        # Nếu giá trị đứng trước nhỏ hơn giá trị phía sau nó thì đổi chỗ cho nhau
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
