class hocvien:
    def __init__(self, Student_ID, Name, DoB ,Address, Mobile, Email):
        self.Student_ID = Student_ID
        self.Name = Name
        self.DoB = DoB
        self.Address = Address
        self.Mobile = Mobile
        self.Email = Email

    def xemhocvien(self):
        print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
            .format(self.Student_ID(), self.Name(), self.DoB(), self.Address(), self.Mobile(), self.Email()))


class Quanlyhocvien(hocvien):
    list_hocvien = []

    def soluonghocvien(self):
        return self.list_hocvien.__len__()

    # def xemhocvien(self):
    #     print('---THONG TIN HOC VIEN---\n')
    #     print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
    #         .format('ID', 'Name', 'Date of birth', 'Address', 'Mobile', 'Email'))
    #     print('\n')   
    #     for i in self.list_hocvien:
    #         print('{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}'
    #         .format(i.Student_ID(), i.Name(), i.DoB(), i.Address(), i.Mobile(), i.Email()))

    def themhocvien(self): #self, Student_ID, Name, DoB ,Address, Mobile, Email):
        
        hocvien1 = hocvien(1, 1, 1, 1, 1, 1)
        self.list_hocvien.append(hocvien1)

qlhv = Quanlyhocvien()


qlhv.themhocvien()

qlhv.xemhocvien()