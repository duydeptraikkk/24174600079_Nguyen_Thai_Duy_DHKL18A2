def xem_danh_sach(mat_hang_list):
    for mh in mat_hang_list:
        thanh_tien = mh['don_gia'] * mh['so_luong']
        thue_vat = thanh_tien * 0.1
        print(f"ma hang: {mh['ma_hang']}, ten hang: {mh['ten_hang']}, don vi: {mh['don_vi_tinh']}, don gia: {mh['don_gia']}, so luong: {mh['so_luong']}, thanh tien: {thanh_tien}, thue vat: {thue_vat}")
def nhap_thong_tin():
    ma_hang = input("nhap ma hang: ")
    ten_hang = input("nhap ten hang: ")
    don_vi_tinh = input("nhap don vi tinh: ")
    don_gia = float(input("nhap don gia: "))
    so_luong = int(input("nhap so luong: "))
    return {'ma_hang': ma_hang, 'ten_hang': ten_hang, 'don_vi_tinh': don_vi_tinh, 'don_gia': don_gia, 'so_luong': so_luong}
def tim_kiem(mat_hang_list, ma_hang):
    for mh in mat_hang_list:
        if mh['ma_hang'] == ma_hang:
            return mh
        return None
def xoa_mat_hang(mat_hang_list, ma_hang):
    mat_hang = tim_kiem(mat_hang_list, ma_hang)
    if mat_hang:
        mat_hang_list.remove(mat_hang)
        print(f"da xoa mat hang co ma {ma_hang}")
    else:
        print(f"ko tim thay mat co ma {ma_hang}")
def sua_mat_hang(mat_hang_list, ma_hang):
    mat_hang = tim_kiem(mat_hang_list, ma_hang)
    if mat_hang:
        mat_hang['ten_hang'] = input("nhap ten hang moi: ")
        mat_hang['don vi tinh'] = input("nhap don vi tinh moi: ")
        mat_hang['don gia'] = float(input("nhap don gia moi: "))
        mat_hang['so luong'] = int(input("nhap so luong moi: "))
        print(f"da cap nhat mat hang co ma {ma_hang}")
    else:
        print(f"khong tim thay mat hang co ma {ma_hang}")

def sap_xep_theo_ten(mat_hang_list):
    def lay_ten_hang(mat_hang):
        return mat_hang['ten_hang']
    
    mat_hang_list.sort(key=lay_ten_hang)
    print("danh sach mat hang sau khi sap xep theo ten: ")
    xem_danh_sach(mat_hang_list)

def main():
    mat_hang_list = []

    while True:
        print("\nchon chuc nang:")
        print("1. xem danh sach mat hang")
        print("2. nhap thong tin mat hang")
        print("3. tim kiem va xoa mat hang")
        print("4. tim kiem va chinh sua thong tin mat hang")
        print("5. xem danh sach mat hang sap xep theo ten")
        print("6. thoat")
        
        choice = input("nhap lua chon: ")

        if choice == '1':
            xem_danh_sach(mat_hang_list)
        elif choice == '2':
            mat_hang_list.append(nhap_thong_tin())
        elif choice == '3':
            ma_hang = input("nhap ma hang can xoa: ")
        elif choice == '4':
            ma_hang = input("nhap ma mat hang can sua: ")
        elif choice == '5':
            sap_xep_theo_ten(mat_hang_list)
        elif choice == '6':
            break
if __name__ == "__main__":
    main()