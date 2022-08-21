from Big_assiment import Quanlyhocvien
qlhv = Quanlyhocvien()
while (1==1):
    print(f'''\n----------- Select Operation -------------
            0. Thoat chuong trinh
            1. Man hinh quan ly hoc vien
            2. Man hinh quan ly mon hoc
            3. Man hinh quan ly dien thi
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
                    print("\n3. Xoa sinh vien.")
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
                    with open('text.txt','w') as file:
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
                ''')
            select2 = int(input('Chon chuc nang:'))
            if select2 == 0:
                break

            elif select2 == 1:
                print('1. Hien thi danh sach mon hoc')

            elif select2 == 2:
                print('2. Them mon hoc')

            elif select2 == 3:
                print('3. Xoa mon hoc')
            
            else:
                print('This task is not available !!')
                print('Please input number !!')
    elif key == 3:
        while (1==1):
            print(f'''\n----------- QUAN LY DIEM THI -------------
                0. Thoat chuong trinh
                1. Hien thi danh sach hoc vien va diem thi
                2. Them diem thi cho hoc vien theo ID
                3. Tim kiem diem thi theo ID
                4. Xoa hoc vien
                5. Xuat du lieu ra file(.txt)
                ''')
            select3 = int(input('Chon chuc nang:'))

            if select3 == 0:
                break

            elif select3 == 1:
                print('1. Hien thi danh sach hoc vien va diem thi')

            elif select3 == 2:
                print('2. Them diem thi cho hoc vien theo ID')

            elif select3 == 3:
                print('3. Tim kiem diem thi theo ID')

            elif select3 == 4:
                print('4. Xoa hoc vien')

            elif select3 == 5:
                print('5. Xuat du lieu ra file(.txt)')
            else:
                print('This task is not available !!')
                print('Please input number !!')
