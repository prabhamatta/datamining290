#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

total = 0
amts =[]
candidates_list = []
candidates_dict ={}

for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        total += float(row[9])  
        amts.append(float(row[9]))
        #if float(row[9])==-30000:
            #print row
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
        if row[2] in candidates_dict.keys():
            candidates_dict[row[2]].append(float(row[9]))
        else:
            candidates_dict[row[2]] = [float(row[9])]


###
# aggregate any stored numbers here
print "********************************"
print " Calculating for all the candidates in CA file"
print "********************************"        

length = len(amts)
minimum = min(amts)
maximum = max(amts)
mean = total/length
sorted_amts = sorted(amts)
print "No.of Records ",length

# calculation median
if length%2!=0:
    median = sorted_amts[length/2]
else:
    median =  (sorted_amts[length/2] +sorted_amts[(length/2)+1])/2

#calculating variance
summation = 0 
sqrd = 0
for x in amts:
    summation = summation + ((x-mean)**2)
    #another way
    #sqrd = sqrd + pow(x,2)
#print (sqrd/length) - pow(mean,2) 
variance = summation/length
#print "variance==",variance
std_dev = pow(variance,0.5)
##/

##### Print out the stats
print "Total Amount: %s" % total
print "Minimum: %s " %minimum
print "Maximum: %s" %maximum
print "Mean: %s" %mean
print "Median: %s" %median
# square root can be calculated with N**0.5
print "Standard Deviation: ", std_dev

##### Comma separated list of unique candidate names
#print "Candidates: ",','.join([str(x) for x in candidates_list])
print "Candidates: ",candidates_list

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    #norm = (value - minimum)/(maximum-minumum) (1 - 0) + 0
    norm = (value - minimum)/(maximum-minimum)
    ###/
    return norm

def zscore_normalize(value):
    """ Z score is used when the actual min and max are unknown, or when there are outliers that dominate min-max normalization"""
    norm = (value - mean)/std_dev
    return norm



def calculate_foreach(candidates):
    print "\n"
    for k,v in candidates.items():
        print "********************************"        
        print "candidate===",k
        print "********************************"        
        
        amts = v
        total = sum(v)
        length = len(amts)
        minimum = min(amts)
        maximum = max(amts)
        mean = total/length
        sorted_amts = sorted(amts)
        print "No.of Records: ",length
        
        # calculation median
        if length%2!=0:
            median = sorted_amts[length/2]
        else:
            median =  (sorted_amts[length/2] +sorted_amts[(length/2)+1])/2
        
        #calculating variance
        summation = 0 
        sqrd = 0
        for x in amts:
            summation = summation + ((x-mean)**2)
        variance = summation/length
        std_dev = pow(variance,0.5)
        ##/        
        print "Total Amount: %s" % total
        print "Minimum: %s " %minimum
        print "Maximum: %s" %maximum
        print "Mean: %s" %mean
        print "Median: %s" %median
        # square root can be calculated with N**0.5
        print "Standard Deviation: ", std_dev 
        print "\n"        
    return


calculate_foreach(candidates_dict)

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])
print "Z-Score normalized values: %r" % map(zscore_normalize, [2500, 50, 250, 35, 8, 100, 19])