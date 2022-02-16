# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 00:58:55 2022

@author: mehme
"""


   
def formul():
    disp = int(input("Write the Displacement: "))
    t = int(input("Write the Time: "))
    m = int(input("Write the Mass: "))
    spd = disp / t
    a = spd / t
    F = m*a
    print("Speed: ", spd)
    print("Acceleration: ", a)
    print("Force: ", F)
    
formul()

   ######################     Mehmet Emin Kaya  ####################### 
