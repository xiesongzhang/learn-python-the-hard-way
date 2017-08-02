# -*- coding:utf-8 -*-
#有100辆车
cars=100
#每个车做的人数
space_in_a_car=4.0
#驾驶员人数
drivers=30
#乘客人数
passengers=90
#停运的车辆数量
cars_not_driven=cars-drivers
#行驶的车辆数量
cars_driven=drivers
#可以运输的乘客数量
carpool_capacity=cars_driven*space_in_a_car
#每辆车乘坐的乘客人数
average_passengers_per_car=passengers/cars_driven


print"there are",cars,"cars available."
print"there are only",drivers,"drivers available."
print"there will be",cars_not_driven,"emty cars today"
print"we can transport",carpool_capacity,"people today."
print"we have",passengers,"to carpoll today"
print"we need to put about",average_passengers_per_car,"in each car"