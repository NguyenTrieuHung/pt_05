from typing import List
class diemthi:
    def __init__(self, Student_ID, Subject_ID, Midel_Score, Final_Score):
        self.Student_ID = Student_ID
        self.Subject_ID = Subject_ID
        self.Midel_Score = Midel_Score
        self.Final_Score = Final_Score
        self.DiemTB = 0
        self.DTK = ''

class Quanlydiemthi():
    List_diemthi = []

    def xemdiemthi(self,list):
        # hien thi tieu de cot
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("Student_ID", "Subject_ID", "Midel_Score", "Final_Score", 'Diem trung binh', 'Diem tong ket'))
        # hien thi danh sach sinh vien
        for hv in list:
            print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}" 
            .format(hv.Student_ID, hv.Subject_ID, hv.Midel_Score, hv.Final_Score, hv.DiemTB, hv.DTK))
        print("\n")

    def themdiemthi(self): #self, Student_ID, Name, DoB ,Address, Mobile, Email):
        ID = int(input('Nhap ID hoc vien'))
        name = int(input('Nhap ID mon hoc:'))
        Midel_Score = input('Midel_Score:')
        Final_Score = input('Final_Score:')
        dt = diemthi(ID, name, Midel_Score, Final_Score)
        self.tinhDTB(dt)
        self.xepLoaiHocLuc(dt)
        self.List_diemthi.append(dt)

    def suadiemthi(self,id):
        for hv in self.List_diemthi:
            if id == hv.Student_ID:
                Midel_Score = (input('Nhap Midel_Score can sua:'))
                Final_Score = (input('Nhap Final_Score can sua:'))
                hv.Midel_Score = Midel_Score
                hv.Final_Score = Final_Score
                print(' Sua thong tin thanh cong')
            else:
                print("Hoc vien co ID = {} khong ton tai.".format(id))

    def xoadiemthi(self,id):
        for hv in self.List_diemthi:
            if id == hv.Student_ID:
                self.list_monhoc.remove(hv)
                print(' Xoa hoc vien thanh cong')
            else:
                print("Hoc vien co ID = {} khong ton tai.".format(id))

    def timdiemthi_id(self,id):
        list_mh = []
        for mh in self.List_diemthi:
            if id == mh.Student_ID:
                list_mh.append(mh)
        return list_mh

    def tinhDTB(self, mh:monhoc):
        DiemTB = (mh.Midel_Score + mh.Final_Score + mh.Final_Score) / 3
        return DiemTB

    def diemtongket(self, mh:monhoc):
        if (mh.DiemTB >= 9):
            mh.DTK = "A"
        elif (mh.DiemTB >= 7):
            mh.DTK = "B"
        elif (mh.DiemTB >= 5):
            mh.DTK = "C"
        else:
            mh.DTK = "D"

    