import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)

print("Kiểu dữ liệu:", type(diem_list), type(diem_array))
print("Điểm cộng thêm (NumPy):", diem_array + 0.5)
print("Trung bình:", np.mean(diem_array))
print("Lớn nhất:", np.max(diem_array))
print("Nhỏ nhất:", np.min(diem_array))
print("Độ lệch chuẩn:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma trận:\n", ma_tran)
print("Kích thước (shape):", ma_tran.shape)
print("Ma trận nhân 2:\n", ma_tran * 2)