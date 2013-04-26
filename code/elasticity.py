#!/usr/bin/env python
__author__ = 'Prabhavathi Matta'
__email__ = 'prabha.matta@ischool.berkeley.edu'
__python_version = '2.7'

import sys
from math import log, exp
from scipy.stats import linregress

if __name__ == '__main__':
    data = open('price-elasticity.csv').read().strip().split('\n')
    
    # Cleaning and formating data
    data = data[1:]
    data = [x.split(',') for x in data] 
    data = [[int(x[0]), int(x[1]), float(x[2].replace('$', ''))] for x in data]
    weekday_Y  = [x[1] for x in data if x[0]<6]
    weekday_X = [x[2] for x in data if x[0]<6]
    weekend_Y  = [x[1] for x in data if x[0] in [6,7]]
    weekend_X = [x[2] for x in data if x[0] in [6,7]]  
    from pprint import pprint as pp
   
    
    # calculating log y and x
    weekday_log_y = [log(i) for i in weekday_Y]
    weekday_log_x = [log(i) for i in weekday_X]
    weekend_log_y = [log(i) for i in weekend_Y]
    weekend_log_x = [log(i) for i in weekend_X]    
    
    #pp(weekday_log_y)
    
    # elasticity = slope of log_y and log_x
    weekday_slope, weekday_intercept, weekday_r_value, weekday_p_value, weekday_std_err = linregress(weekday_log_x,weekday_log_y )
    weekend_slope, weekend_intercept, weekend_r_value, weekend_p_value, weekend_std_err = linregress(weekend_log_x,weekend_log_y)
    print 'Ques 1: Price elasticity of weekday prices == ',weekday_slope
    print 'Ques 2: Price elasticity of weekend prices == ',weekend_slope
    
    
    """Ques3 : what price should we set to optimize max revenue
    
    revenue = num of rooms * price
    num of rooms = Y
    price = X
    revenue = X*Y
    
    Linear Regression eqn, Y=AX^bu
    intercept = a = log(A)
    slope = b 
    y = a + bx
    x  = (y-a)/b
    
    """
    # For Weekday
    weekday_list = []
    for num_weekday_rooms in range(1,101):
        log_weekday_rooms = log(num_weekday_rooms)
        log_weekday_price = (log_weekday_rooms - weekday_intercept) /weekday_slope
        real_weekday_price = exp(log_weekday_price)
        weekday_revenue = num_weekday_rooms * real_weekday_price
        weekday_list.append((weekday_revenue,num_weekday_rooms,real_weekday_price))
    sorted_weekday = sorted(weekday_list, reverse = True)
    #pp(sorted_weekday)
    
    max_rev_weekday = sorted_weekday[0][0]
    optimum_price_weekday =  sorted_weekday[0][2]
    #print " Revenue for {0} rooms = {1} with price = {2} ".format(sorted_weekday[0][1],max_rev_weekday,optimum_price_weekday)
    print "***************************"
    print "Ques 3a: What weekday price should we set to optimize max revenue??\n"
     
    print "Optimum revenue = ",max_rev_weekday
    print "Optimum price = ",optimum_price_weekday
    print "Num of rooms to be rented = ",sorted_weekday[0][1]
        
    # For WeekEnd
    weekend_list = []
    for num_weekend_rooms in range(1,101):
        log_weekend_rooms = log(num_weekend_rooms)
        log_weekend_price = (log_weekend_rooms - weekend_intercept) /weekend_slope
        real_weekend_price = exp(log_weekend_price)
        weekend_revenue = num_weekend_rooms * real_weekend_price
        weekend_list.append((weekend_revenue,num_weekend_rooms,real_weekend_price))
    sorted_weekend = sorted(weekend_list, reverse = True)
    #pp(sorted_weekend)
    
    max_rev_weekend = sorted_weekend[0][0]
    optimum_price_weekend =  sorted_weekend[0][2]
    print "***************************"
    print "Ques 3b: What weekend price should we set to optimize max revenue??\n"  
    
    print "Optimum revenue = ",max_rev_weekend
    print "Optimum price = ",optimum_price_weekend
    print "Num of rooms to be rented = ",sorted_weekend[0][1]    
    #print max_rev_weekend,optimum_price_weekend
 