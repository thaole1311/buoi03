#Hoạt động 1: Dictionary cơ bản - khai báo, truy xuất, thêm/sửa/xóa

#Bài tập 1.1 - Khai báo & truy xuất:
sinh_vien = {
"ho_ten": "Nguyen Van A",
"nam_sinh": 2004,
"diem_tb": 8.5
}
print(sinh_vien["ho_ten"]) # truy xuat theo khoa
print(sinh_vien.get("diem_tb")) # truy xuat an toan bang get()
print(sinh_vien.get("lop", "Chua co")) # get() voi gia tri mac dinh neu khong co khoa


"""
Yêu cầu: Giải thích vì sao dùng sinh_vien["lop"] (khi "lop" chưa tồn tại) sẽ gây lỗi KeyError, còn  sinh_vien.get("lop", "Chua co") thì không. 
Trả lời: Khi bạn sử dụng sinh_vien["lop"], Python sẽ cố gắng truy cập giá trị của khóa "lop" trong từ điển sinh_vien. Nếu khóa này không tồn tại, Python sẽ ném ra một lỗi KeyError, vì nó không tìm thấy khóa đó trong từ điển.
"""

# Bài tập 1.2 - Thêm/sửa/xóa:
sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["diem_tb"] = 9.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc
print(sinh_vien)
#Bài tập 1.2 - Thêm/sửa/xóa:
sinh_vien["lop"] = "CNTT01" # them khoa moi
sinh_vien["diem_tb"] = 9.0 # sua gia tri khoa da co
print(sinh_vien)
diem_cu = sinh_vien.pop("diem_tb") # xoa theo khoa, tra ve gia tri vua xoa

print(sinh_vien, "- diem da xoa:", diem_cu)
sinh_vien.update({"nam_sinh": 2003, "email": "a@example.com"}) # cap nhat/them nhieu khoa cung luc
print(sinh_vien)
#Hoạt động 2: Duyệt Dictionary bằng for - keys/values/items
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
for mon in diem_mon_hoc.keys():
  print(mon)
for diem in diem_mon_hoc.values():
  print(diem)
for mon, diem in diem_mon_hoc.items():
  print(f"{mon}: {diem}")
tong_diem = 0
for diem in diem_mon_hoc.values():
  tong_diem = tong_diem + diem
print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))

#Hoạt động 3: Dictionary comprehension & giới thiệu Set

#Bài tập 3.1 - Dictionary comprehension:
diem_mon_hoc = {"Toan": 8.0, "Ly": 7.5, "Hoa": 9.0, "Van": 6.5}
diem_cong_diem = {mon: round(diem + 0.5, 2) for mon, diem in diem_mon_hoc.items()}
print(diem_cong_diem)
ten_mon_viet_hoa = {mon.upper(): diem for mon, diem in diem_mon_hoc.items()}
print(ten_mon_viet_hoa)

#Bài tập 3.2 - So sánh nhanh với Set:
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}
print(mon_hoc_ky1 & mon_hoc_ky2) # giao: mon hoc chung 2 hoc ky
print(mon_hoc_ky1 | mon_hoc_ky2) # hop: tat ca mon hoc ca 2 hoc ky

print(mon_hoc_ky1 - mon_hoc_ky2) # mon chi co o hoc ky 1
"""
Yêu cầu: So sánh Set với Dictionary - Set có lưu cặp khóa-giá trị không? Vì sao Set không cho  phép phần tử trùng lặp?
Giải thích: Set là một tập hợp các phần tử duy nhất, không lưu trữ cặp khóa-giá trị như Dictionary. Set không cho phép phần tử trùng lặp vì nó được thiết kế để đảm bảo rằng mỗi phần tử chỉ xuất hiện một lần, giúp dễ dàng kiểm tra sự tồn tại của phần tử và thực hiện các phép toán tập hợp như giao, hợp, hiệu.
"""