
class monhoc:
    def __init__(self, Subject_ID, Subject_Name):
        self.Subject_ID = Subject_ID
        self.Subject_Name = Subject_Name

class Quanlymonhoc:
    list_monhoc = []

    def soluongmonhoc(self):
        return self.list_monhoc.__len__()

    def xemmonhoc(self,list):
        # hien thi tieu de cot
        print("{:<8} {:<8}"
              .format("Subject_ID", "Subject_Name"))
        # hien thi danh sach sinh vien
        for mh in list:
            print("{:<8} {:<8}" 
            .format(mh.Subject_ID, mh.Subject_Name))
        print("\n")
        
    
    def themmonhoc(self):
        print('Them mon hoc:')
        id = int(input('Nhap ID mon hoc:'))
        namemh = input('Nhap ten mon hoc:')
        mh = monhoc(id, namemh)
        self.list_monhoc.append(mh)
    

    def suamonhoc_id(self,id):
        id = int(input('Nhap ID mon hoc can tim:'))
        for mh in self.list_monhoc:
            if id == mh.Subject_ID:
                mh_name = (input('Nhap ten mon hoc can sua:'))
                mh.Subject_Name = mh_name
                print(' Sua thong tin thanh cong')
            else:
                print("Mon hoc co ID = {} khong ton tai.".format(id))

    def xoamonhoc_id(self,id):
        id = int(input('Nhap ID mon hoc can xoa:'))
        for mh in self.list_monhoc:
            if id == mh.Subject_ID:
                self.list_monhoc.remove(mh)
                print(' Xoa mon hoc thanh cong')
            else:
                print("Mon hoc co ID = {} khong ton tai.".format(id))

    def timmonhoc_name(self,name):
        list_mh = []
        name = input('Nhap ten mon hoc can tim:')
        for mh in self.list_monhoc:
            if name == mh.Subject_Name:
                list_mh.append(mh)
        return list_mh