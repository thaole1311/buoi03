import pandas as pd

# Bài tập 2.1 – Đọc CSV & xem tổng quan
df = pd.read_csv("diem_sinh_vien.csv")
print("--- 5 dòng đầu ---")
print(df.head())
print("Số dòng, số cột:", df.shape)
print("Danh sách cột:", df.columns.tolist())

# Bài tập 2.2 – Thống kê theo môn học
print("\n--- Điểm trung bình theo môn ---")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()
print(diem_trung_binh_mon)
print("Điểm trung bình toàn bộ:", df["diem"].mean())
print("Điểm cao nhất:", df["diem"].max())
print("Điểm thấp nhất:", df["diem"].min())

# Bài tập 2.3 – Tính DTB từng sinh viên & lọc đạt/không đạt
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh viên đạt:")
print(sinh_vien_dat)
print("\nSinh viên không đạt:")
print(sinh_vien_khong_dat)