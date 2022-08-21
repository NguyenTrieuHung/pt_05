#1. Nhập thông tin cho n chiếc xe ô tô, danh sách ô tô lưu vào trong list. 
#   Sử dụng hàm filter để lọc ra các ô tô có màu đen và năm sản xuất kể từ 2015 đến nay.
#   Thông tin ô tô bao gồm: Mã, Nhãn hiệu, Dòng xe, Màu sắc 
#   (sử dụng kiểu int để lưu trữ: 1-đen, 2-trắng, 3-đỏ, 4-xanh nước biển), Năm sản xuất.




from sqlalchemy import true


class car:
    def __init__(self,code, label_effect, line_cart, color, year ):
        self.code = code
        self.label_effect = label_effect
        self.line_cart = line_cart
        self.color = color
        self.year = year

    def filter_car(self):


car1 = car(1, 'audi', 'sedan', 1, 2015)
car2 = car(2, 'toyota','pickup', 2, 2016)
car3 = car(3, 'lexus', 'sport', 3, 2017)
car4 = car(4, 'mercedes', 'race', 4, 2018)


    








#2. Từ câu 1, hiển thị danh sách ô tô, sử dụng hàm map để chuyển đổi Màu sắc từ dạng số
#   sang dạng văn bản. VD: ‘3’ chuyển thành ‘đỏ’.
