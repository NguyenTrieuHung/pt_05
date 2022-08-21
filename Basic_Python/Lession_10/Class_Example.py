import datetime

#1 creat class
class Vehicle:
    def __init__(self, name,  max_speed, color, year):
        self.name=name             # Puplic
        self.max_speed=max_speed  # Protected _
        self.color=color         # Private  __
        self.year=year           # Private  __
    
    def get_name(self):
        return self.name

    def get_max_speed(self):
        return self.max_speed

    def get_year_old(self):
        return 2022 - self.year
    
    def get_color(self):
        return self.color
        
    def set_color(self, color):
        self.color=color

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed 
    
veh_x = Vehicle('toyota Fortuner',150, 'red', 2014)
veh_y = Vehicle('Huyndai Santafe', 200, 'black', 2016)

print(f'Vehicle infomation of X - /Name: {veh_x.name}, /Max Speed: {veh_x.max_speed},\
     /Year old: {veh_x.get_year_old()} ')

print(f'Vehicle infomation of X - /Name: {veh_x.name}, /Max Speed: {veh_x.max_speed},\
     /Year old: {veh_x.get_year_old()} ')

#print(f'Vehicle infomation of X - year old: {veh_x.year}, Max Speed: {veh_x.max_speed}')

#2 creat a new object for Motor class( la con cua thang Vehicle)

class Motor(Vehicle):
    def __init__(self, name, max_speed, color, year, engine):
        self.engine = engine
        super().__init__(name, max_speed, color, year)

    def get_color(self):
        return 'white Black'

Motorx = Motor('Air Blade','black', 200, 2017, 150)