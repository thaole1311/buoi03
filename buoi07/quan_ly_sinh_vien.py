# ====================================================
# BÀI TẬP TỰ THỰC HIỆN: QUẢN LÝ SINH VIÊN
# File: quan_ly_sinh_vien.py
# ====================================================

# 1. Khai báo dữ liệu ban đầu
danh_sach_sv = [
    {"ma_sv": "SV01", "ten": "Nguyen Van A", "lop": "CNTT1", "diem_tb": 8.5},
    {"ma_sv": "SV02", "ten": "Tran Thi B", "lop": "CNTT1", "diem_tb": 6.8},
    {"ma_sv": "SV03", "ten": "Le Van C", "lop": "CNTT2", "diem_tb": 4.5},
    {"ma_sv": "SV04", "ten": "Pham Minh D", "lop": "CNTT2", "diem_tb": 9.2}
]

# 2. Hàm tìm kiếm sinh viên (Chuẩn hóa mã SV để tránh lỗi nhập lệch hoa/thường hay dấu cách)
def tim_sv_theo_ma(ma_sv):
    ma_chuan = str(ma_sv).strip().upper()
    for sv in danh_sach_sv:
        if sv["ma_sv"].strip().upper() == ma_chuan:
            return sv
    return None

# 3. Hàm nhập số thực an toàn bằng try-except
def nhap_so_thuc(loi_nhac, diem_min=0.0, diem_max=10.0):
    while True:
        try:
            val = float(input(loi_nhac).strip())
            if diem_min <= val <= diem_max:
                return val
            print(f"-> Điểm phải nằm trong khoảng từ {diem_min} đến {diem_max}. Vui lòng nhập lại!")
        except ValueError:
            print("-> Dữ liệu không hợp lệ! Vui lòng nhập một số (ví dụ: 7.5 hoặc 8).")

# 4. Hiển thị danh sách sinh viên & Xếp loại
def hien_thi_danh_sach():
    if not danh_sach_sv:
        print("-> Danh sách sinh viên hiện đang rỗng.")
        return
    print("\n" + "=" * 65)
    print(f"{'Mã SV':<10}{'Họ và Tên':<22}{'Lớp':<12}{'Điểm TB':<10}{'Xếp loại':<12}")
    print("-" * 65)
    for sv in danh_sach_sv:
        dtb = sv["diem_tb"]
        xep_loai = "Xuất sắc" if dtb >= 9 else ("Giỏi" if dtb >= 8 else ("Khá" if dtb >= 6.5 else ("TB" if dtb >= 5 else "Yếu")))
        print(f"{sv['ma_sv']:<10}{sv['ten']:<22}{sv['lop']:<12}{dtb:<10.1f}{xep_loai:<12}")
    print("-" * 65)

# 5. Các hàm nghiệp vụ chính
def them_sinh_vien(ma_sv, ten, lop, diem_tb):
    ma_chuan = ma_sv.strip().upper()
    if tim_sv_theo_ma(ma_chuan) is not None:
        print(f"-> Mã sinh viên '{ma_chuan}' đã tồn tại! Không thể thêm.")
        return
    danh_sach_sv.append({
        "ma_sv": ma_chuan,
        "ten": ten.strip().title(),
        "lop": lop.strip().upper(),
        "diem_tb": diem_tb
    })
    print(f"-> Đã thêm sinh viên {ten.strip().title()} ({ma_chuan}) thành công.")

def cap_nhat_diem(ma_sv, diem_moi):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Không tìm thấy sinh viên có mã '{ma_sv.strip().upper()}'.")
        return
    diem_cu = sv["diem_tb"]
    sv["diem_tb"] = diem_moi
    print(f"-> Đã cập nhật điểm cho SV {sv['ten']} ({sv['ma_sv']}): {diem_cu} -> {diem_moi}")

def xoa_sinh_vien(ma_sv):
    sv = tim_sv_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Không tìm thấy sinh viên có mã '{ma_sv.strip().upper()}'.")
        return
    danh_sach_sv.remove(sv)
    print(f"-> Đã xóa sinh viên {sv['ten']} ({sv['ma_sv']}) khỏi hệ thống.")

def thong_ke():
    if not danh_sach_sv:
        print("-> Không có dữ liệu để thống kê.")
        return
    
    sv_max = max(danh_sach_sv, key=lambda x: x["diem_tb"])
    tong_diem = sum(sv["diem_tb"] for sv in danh_sach_sv)
    dtb_chung = tong_diem / len(danh_sach_sv)
    
    print("\n====== THỐNG KÊ KẾT QUẢ ======")
    print(f"- Tổng số sinh viên: {len(danh_sach_sv)}")
    print(f"- Điểm trung bình chung: {dtb_chung:.2f}")
    print(f"- Sinh viên thủ khoa: {sv_max['ten']} ({sv_max['ma_sv']}) - Điểm TB: {sv_max['diem_tb']}")

# 6. Giao diện Menu điều khiển chính
def hien_thi_menu():
    print("\n====== CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ======")
    print("1. Hiển thị danh sách sinh viên")
    print("2. Tìm kiếm sinh viên theo mã")
    print("3. Thêm sinh viên mới")
    print("4. Cập nhật điểm trung bình")
    print("5. Xóa sinh viên")
    print("6. Thống kê kết quả")
    print("0. Thoát chương trình")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach()
        elif lua_chon == "2":
            ma_sv = input("Nhập mã SV cần tìm: ")
            sv = tim_sv_theo_ma(ma_sv)
            if sv:
                dtb = sv['diem_tb']
                xep_loai = "Xuất sắc" if dtb >= 9 else ("Giỏi" if dtb >= 8 else ("Khá" if dtb >= 6.5 else ("TB" if dtb >= 5 else "Yếu")))
                print(f"-> Tìm thấy: {sv['ma_sv']} | {sv['ten']} | Lớp: {sv['lop']} | Điểm TB: {dtb} | Xếp loại: {xep_loai}")
            else:
                print(f"-> Không tìm thấy sinh viên có mã '{ma_sv.strip().upper()}'.")
        elif lua_chon == "3":
            ma_sv = input("Nhập mã SV mới: ")
            ten = input("Nhập họ tên SV: ")
            lop = input("Nhập lớp: ")
            diem_tb = nhap_so_thuc("Nhập điểm trung bình (0-10): ")
            them_sinh_vien(ma_sv, ten, lop, diem_tb)
        elif lua_chon == "4":
            ma_sv = input("Nhập mã SV cần cập nhật điểm: ")
            diem_moi = nhap_so_thuc("Nhập điểm trung bình mới (0-10): ")
            cap_nhat_diem(ma_sv, diem_moi)
        elif lua_chon == "5":
            ma_sv = input("Nhập mã SV cần xóa: ")
            xoa_sinh_vien(ma_sv)
        elif lua_chon == "6":
            thong_ke()
        elif lua_chon == "0":
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("-> Lựa chọn không hợp lệ! Vui lòng chọn lại.")

if __name__ == "__main__":
    chay_chuong_trinh()