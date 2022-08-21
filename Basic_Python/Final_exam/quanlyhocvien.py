
class hocvien:
    def __init__(self, Student_ID, Name, DoB , Sex, Address, Mobile, Email): #Student_ID, `name`, DoB, Sex, Address, Mobile, Email
        self.Student_ID = Student_ID
        self.Name = Name
        self.DoB = DoB
        self.Sex = Sex
        self.Address = Address
        self.Mobile = Mobile
        self.Email = Email

class Quanlyhocvien:
    list_hocvien = []

    def soluonghocvien(self):
        return self.list_hocvien.__len__()

    def xemhocvien_list(self,list):
        # hien thi tieu de cot
        print("{:<8} {:<8} {:<8} {:<8}{:<8} {:<8} {:<8}"
              .format("ID", "Name", "DoB", 'Sex', "Address", "Mobile", "Email"))
        # hien thi danh sach sinh vien
        for hv in list:
            print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8}" 
            .format(hv.Student_ID, hv.Name, hv.DoB, hv.Sex, hv.Address, hv.Mobile, hv.Email))
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