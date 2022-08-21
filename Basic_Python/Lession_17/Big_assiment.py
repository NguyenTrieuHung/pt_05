# Chương trình:
# Viết chương trình quản lý thông tin điểm thi của Học viên với các đối tượng sau:
# + Học viên: Mã học viên, Họ tên, Ngày sinh, Giới tính, Địa chỉ, Số điện thoại, Email.
# + Môn học: Mã môn học, Tên môn học
# + Điểm thi: Mã học viên, Mã môn học, Điểm quá trình, Điểm kết thúc

# Yêu cầu chức năng:
# + Tạo các giao diện người dùng trong terminal(người dùng có thể di chuyển qua lại giữa các màn hình):
# 	- Màn hình Menu chính: hiển thị danh sách các chức năng của chương trình
# 	- Màn hình Quản lý thông tin Học viên
# 	- Màn hình Quản lý thông tin Môn học
# 	- Màn hình Quản lý thông tin Điểm thi
# + Quản lý thông tin Học viên: Xem/Thêm/Sửa/Xoá/Tìm kiếm học viên theo ten va ma
# + Quản lý thông tin Môn học: Xem/Thêm/Sửa/Xoá/Tìm kiếm môn học theo ma va ten
# + Quản lý thông tin Điểm thi: Xem/Thêm/Sửa điểm/Xoá điểm/Tra cứu điểm theo Mã học viên hoặc Họ tên học viên/Thống kê danh sách các Học viên theo các mức Điểm tổng kết (A (90 <= điểm <= 100), B (70 <= điểm < 90), C (50 <= điểm < 70), D (điểm < 50)). Điểm tổng kết tính bằng công thức: Điểm tổng kết = (Điểm quá trình + Điểm kết thúc * 2) / 3
# + Xuất bảng điểm ra tệp tin txt. Thông tin kết xuất bao gồm: Mã học viên, Họ tên, Ngày sinh, Giới tính, Địa chỉ, Số điện thoại, Email, Tên môn học, Điểm quá trình, Điểm kết thúc

# Note:
# + Dữ liệu ban đầu được lưu trong 3 file json:
# students.json: File chứa thông tin học viên
# subjects.json: File chưa thông tin môn học
# scores.json: File chưa thông tin điểm
# + Kiểm tra dữ liệu đầu vào nhập từ bàn phím (Validate input data), nếu không hợp lệ sẽ thông báo lỗi và yêu cầu nhập lại
# + Bắt lỗi (Handle Exception) với những xử lý có thể gây lỗi trong quá trình chạy chương trình (runtime)
# + Phân nhóm các đối tượng vào các package/module phù hợp (package là thư mục, module là tệp tin .py). Khi cần sử dụng thì import vào.

import re
from typing_extensions import Self


class hocvien:
    def __init__(self, Student_ID, Name, DoB ,Address, Mobile, Email):
        self.Student_ID = Student_ID
        self.Name = Name
        self.DoB = DoB
        self.Address = Address
        self.Mobile = Mobile
        self.Email = Email
    
<<<<<<< HEAD
    
=======
    def get_id(self):
        return self.Student_ID

    def get_name(self):
        return self.Name

    def get_DoB(self):
        return self.DoB
    
    def get_email(self):
        return self.Email
    
    def get_mobile(self):
        return self.Mobile

    def get_address(self):
        return self.Address

    def show_info():
        print('\nInfo employee:\n')
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
        .format('ID', 'Name', 'Date of birth', 'Address', 'Mobile', 'Email'))
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'.format(Self.Student_ID, Self.Name, Self.DoB, Self.Address, Self.Mobile, Self.Email))
>>>>>>> 56fc1a1725762f770df2eaf8368a499f761fdd17



# class monhoc:
#     def __init__(self, Subject_ID, Subject_Name):
#         self.Subject_ID = Subject_ID
#         self.Subject_Name = Subject_Name

# class diemthi:
#     def __init__(self, Student_ID, Subject_ID, Midel_Score, Final_Score):
#         self.Student_ID = Student_ID
#         self.Subject_ID = Subject_ID
#         self.Midel_Score = Midel_Score
#         self.Final_Score = Final_Score

class Quanlyhocvien:
    list_hocvien = []

    def soluonghocvien(self):
        return self.list_hocvien.__len__()

    def xemhocvien_list(self,list):
        # hien thi tieu de cot
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}"
              .format("ID", "Name", "DoB", "Address", "Mobile", "Email"))
        # hien thi danh sach sinh vien
        for hv in list:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}" 
            .format(hv.Student_ID, hv.Name, hv.DoB, hv.Address, hv.Mobile, hv.Email))
        print("\n")
        


    def themhocvien(self): #self, Student_ID, Name, DoB ,Address, Mobile, Email):
        id = int(input('Input ID:'))
        name = input('Input Name:')
        dob = input("Enter the date of birth (dd/mm/yyy) : ")
        address = input('Input Address:')
        mobileNumber = input('Input MobileNumber:')
        email = input('Input Email:')
        hv = hocvien(id, name, dob, address, mobileNumber, email)
        self.list_hocvien.append(hv)

    def suahocvien_id(self,ID):
        hv:hocvien = self.timhocvien_id(ID)
        if  (hv != None):
            St_ID = int(input('Input ID:'))
            Name = input('Input Name:')
            DoB = input("Enter the date of birth (dd/mm/yyy) : ")
            Address = input('Input Address:')
            Mobile = input('Input MobileNumber:')
            Email = input('Input Email:')
            hv.Student_ID = St_ID
            hv.Name = Name
            hv.DoB = DoB
            hv.Address = Address
            hv.Mobile = Mobile
            hv.Email = Email
            print(' Sua thong tin thanh cong')
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))


    def xoahocvien_id(self,ID):
        # if (self.soluonghocvien() > 0):
        #     for hv in self.list_hocvien:
        #         if hv.Student_ID == ID:
        #             self.list_hocvien.remove(hv)
        isDeleted = False
        # tìm kiếm sinh viên theo ID
        hv = self.timhocvien_id(ID)
        if (hv != None):
            self.list_hocvien.remove(hv)
            isDeleted = True
        return isDeleted
        



    def timhocvien_id(self,id):
        searchResult = None
        if (self.soluonghocvien() > 0):
            for hv in self.list_hocvien:
                if (hv.Student_ID == id):
                    searchResult = hv
        return searchResult

    def timhocvien_name(self,name): #tim hoc vien theo ten tra ve danh sach hoc vien
        list_hv = []
        if (self.soluonghocvien() > 0):
            for hv in self.list_hocvien:
                if name.upper() in hv.Name.upper():
                    list_hv.append(hv)
        return list_hv


# class Quanlymonhoc:
#     list_monhoc = []

#     def xemmonhoc(self):
#         pass
    
#     def themmonhoc(self):
#         pass

#     def suamonhoc_id(self,id):
#         pass

#     def suamonhoc_name(self,name):
#         pass

#     def xoamonhoc_id(self,id):
#         pass

#     def xoamonhoc_name(self,name):
#         pass

#     def timmonhoc_id(self,id):
#         pass

#     def timmonhoc_name(self,name):
#         pass

# class Quanlydiemthi_hocvien(hocvien,monhoc,diemthi):
#     def __init__(self, Student_ID, Name, DoB, Address, Mobile, Email, Subject_Name, Subject_ID, Midel_Score, Final_Score):
#         super().__init__(Student_ID, Name, DoB, Address, Mobile, Email)
#         self.Subject_Name = Subject_Name
#         self.Subject_ID = Subject_ID
#         self.Midel_Score = Midel_Score
#         self.Final_Score = Final_Score

#     def xemdiemthi(self):
#         pass
    
#     def themdiemthi(self):
#         pass

#     def suadiemthi_id(self,id):
#         pass

#     def suadiemthi_name(self,name):
#         pass

#     def xoadiemthi_id(self,id):
#         pass

#     def xoadiemthi_name(self,name):
#         pass

#     def timdiemthi_id(self,id):
#         pass

#     def timdiemthi_name(self,name):
#         pass
<<<<<<< HEAD
=======
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
>>>>>>> 56fc1a1725762f770df2eaf8368a499f761fdd17



        
    








    

        

