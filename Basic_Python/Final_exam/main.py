 
from quanlyhocvien import Quanlyhocvien
from quanlymonhoc import Quanlymonhoc
from quanlydiemthi import Quanlydiemthi


qlhv = Quanlyhocvien()
qlmh = Quanlymonhoc()
qldt = Quanlydiemthi()
while (1==1):
    print(f'''\n----------- CHUONG TRINH QUAN LY THONG TIN HOC VIEN -------------
            0. Thoat chuong trinh
            1. Man hinh quan ly thong tin hoc vien
            2. Man hinh quan ly thong tin mon hoc
            3. Man hinh quan ly thong tin dien thi
            ''')
    key = int(input('Chon chuc nang:'))
    if key == 1:

        while (1==1):
            print(f'''\n----------- QUAN LY HOC VIEN -------------
                0. Thoat chuong trinh
                1. Hien thi danh sach hoc vien
                2. Tim kiem hoc vien theo ten
                3. Them hoc vien
                4. Sua thong tin hoc vien theo ID
                5. Xoa hoc vien
                6. Xuat danh sach hoc vien ra file(.txt)
                ''')
            select = int(input('Chon chuc nang:'))

            if select == 0:
                break

            elif select == 1: 
                print('1. Hien thi danh sach hoc vien')
                qlhv.xemhocvien_list(qlhv.list_hocvien)
                    
            elif select == 2:
                print('2. Tim hoc vien theo ten:')
                print('Nhập tên:')
                name = input()
                search = qlhv.timhocvien_name(name)
                qlhv.xemhocvien_list(search)       

            elif select == 3:
                print('3. Them hoc vien')
                qlhv.themhocvien()
                print('Input hoc vien successful !!!')
                
            elif select == 4:
                if (qlhv.soluonghocvien() > 0):
                    print('4. Sua thong tin hoc vien theo ID:')
                    ID = int(input('Nhap ID:'))
                    qlhv.suahocvien_id(ID)
                else:
                    print('Danh sach hoc vien trong !')

            elif select == 5:
                if (qlhv.soluonghocvien() > 0):
                    print("\n3. Xoa hoc vien.")
                    print("\nNhap ID: ")
                    ID = int(input())
                    if (qlhv.xoahocvien_id(ID)):
                        print("\nSinh vien co id = ", ID, " da bi xoa.")
                    else:
                        print("\nSinh vien co id = ", ID ," khong ton tai.")
                else:
                    print("\nSanh sach sinh vien trong!")

            elif select == 6:
                    list = []
                    for hv in qlhv.list_hocvien:
                        L = "ID: {} Name: {} Dob: {} Address: {} Mobile: {} Email: {}".format(hv.Student_ID, hv.Name, hv.DoB, hv.Address, hv.Mobile, hv.Email)
                        list.append(L)
                    print(list)
                    with open('list_hv.txt','w') as file:
                        file.writelines(str(list))

                    
            else:
                print('This task is not available !!')
                print('Please input number !!')

    elif key == 2:
        while (1==1):
            print(f'''\n----------- QUAN LY MON HOC -------------
                0. Thoat chuong trinh
                1. Hien thi danh sach mon hoc
                2. Them mon hoc
                3. Xoa mon hoc
                4. Tim mon hoc
                5. Sua mon hoc
                ''')
            select2 = int(input('Chon chuc nang:'))
            if select2 == 0:
                break

            elif select2 == 1:
                print('1. Hien thi danh sach mon hoc')
                qlmh.xemmonhoc(qlmh.list_monhoc)

            elif select2 == 2:
                print('2. Them mon hoc')
                qlmh.themmonhoc()
                print('Them mon hoc thanh cong !!!')

            elif select2 == 3:
                print('3. Xoa mon hoc')
                id = int(input('Nhap ID mon hoc can xoa:'))
                qlmh.xoamonhoc_id(id)
            
            elif select2 == 4:
                print('3. Tim mon hoc')
                name = input('Nhap ten mon hoc can tim:')
                timkiem = qlmh.timmonhoc_name(name)
                qlmh.xemmonhoc(timkiem)

            elif select2 == 5:
                print('3. Sua mon hoc')
                id = int(input('Nhap ID mon hoc can sua:'))
                qlmh.suamonhoc_id(id)

            else:
                print('This task is not available !!')
                print('Please input number !!')
    elif key == 3:
        while (1==1):
            print(f'''\n----------- QUAN LY DIEM THI -------------
                0. Thoat chuong trinh
                1. Hien thi danh sach hoc vien va diem thi
                2. Them diem thi 
                3. Tim kiem diem thi theo ID
                4. Xoa diem thi
                5. Sua diem thi
                ''')
            select3 = int(input('Chon chuc nang:'))

            if select3 == 0:
                break

            elif select3 == 1:
                print('1. Hien thi danh sach hoc vien va diem thi')
                qldt.xemdiemthi(qldt.List_diemthi)

            elif select3 == 2:
                print('2. Them diem thi ')
                qldt.themdiemthi()

            elif select3 == 3:
                print('3. Tim kiem diem thi theo ID')
                id = input('Nhap ID hoc vien can tim:')
                timkiem = qldt.timdiemthi_id(id)
                qlmh.xemdiemthi(timkiem)

            elif select3 == 4:
                print('4. Xoa hoc vien')
                id = input('Nhap ID hoc vien can xoa:')
                qlmh.xoadiemthi(id)

            elif select3 == 5:
                print('5. Sua hoc vien')
                id = input('Nhap ID hoc vien can Sua:')
                qlmh.suadiemthi(id)

            else:
                print('This task is not available !!')
                print('Please input number !!')