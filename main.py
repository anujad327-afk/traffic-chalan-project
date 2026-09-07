from database import violation_fine,user_data
from violation_detection import detect_violation
from number_plate_recognition import num_plt
from chalan_generation import chalan_gen
violation = detect_violation('no_parking1.jpg')
chalan = violation_fine(violation)
vehicle_num =  num_plt()
info = user_data(vehicle_num)
notice = chalan_gen(violation,info,chalan)
print(notice)

