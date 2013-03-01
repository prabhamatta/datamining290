#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
import collections as coll

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures
cand_nm_counter = coll.Counter()
zipcodeDict = coll.defaultdict(list)
total_records = 0
sum_frac = 0
amt_name_list = []

############### Read through files 
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        #first time does not go inside this
        cand_nm_counter[row[cand_nm]] += 1
        total_records +=1
        #zipcodeDict willbe of the form have {'zip1': ['ob', 'ob', 'ro'], 'zip2': ['ob']}
        zipcodeDict[row[contbr_zip]].append(row[cand_nm])
        amt_name_list.append((float(row[contb_receipt_amt]),row[cand_nm]))
        
def get_gini(item_counter, total=0):
    sum_frac = 0
    if total == 0:
        for k,v in item_counter.items():
            total += v
        print "total in gini..",total,item_counter
            
    sum_sqr = sum(v*v for v in item_counter.values())
    gini = 1- float(sum_sqr)/pow(total,2)
    return gini
    

#### Q1.Calculating the Gini Index for the Candidate Names for the enitre data set
gini = get_gini(cand_nm_counter,total_records)



#### Q2. Partition by zip code, calculate the weighted average Gini Index score over all partitions
zip_gini_dict = coll.defaultdict(float)
test = 0
weighted_avg_gini = 0
for k,v in zipcodeDict.items():
    test += 1
    #print k,v
    zip_total = len(v)
    #converting v into Counter
    gini_zip = get_gini(coll.Counter(v),zip_total)
    #print "zip = %s, total_zip=%s , gini_zip = %s"%(k,zip_total,gini_zip)
    weighted_avg_gini += (float(zip_total)/total_records)*gini_zip

        
split_gini = weighted_avg_gini  # weighted average of the Gini Indexes using candidate names, split up by zip code

def get_gini_for_partition(partition,amt_name_list):
    records_below,records_above = 0,0
    counter_below, counter_above = coll.Counter(), coll.Counter()
    gini_below, gini_above = 0, 0
    for amt,name in amt_name_list:
        if amt <= partition:
            counter_below[name] += 1
            records_below += 1
        else:
            counter_above[name] += 1
            records_above += 1
    gini_below = get_gini(counter_below,records_below)
    gini_above = get_gini(counter_above, records_above)    
    gini_of_partition = (float(records_above)/(records_above+records_below))*gini_above + (float(records_below)/(records_above+records_below))*gini_below
    return gini_of_partition
        

##### Q3 Find a best split of a continuous field
### I am using contribution amount as the continuous field


###Method1: using mean of the contibution amt as the partition
mean = sum(float(tup[0]) for tup in amt_name_list)/total_records
gini_partition = get_gini_for_partition(mean,amt_name_list)

###Method2: splitting contribution amount as the partition
def best_gini_meth2(amt_name_list,total_records):
    """Finding minimum gini with  each pair of contribution amounts as partition"""
    sorted_amt_name_list = sorted(amt_name_list)
    partition_gini_list = []
    counter_below, counter_above = coll.Counter(), coll.Counter((sorted_amt_name_list[x][1] for x in xrange(total_records)))
    mingini = 1
    minpartition = 0
    
    for i in range(total_records-1):
        #print "-------"
        
        if i%10000 == 0:
            print "here...",i
        records_below = i+1
        records_above = total_records-(i+1)
        counter_below.update([sorted_amt_name_list[i][1]])
        counter_above.subtract([sorted_amt_name_list[i][1]])
        gini_below = get_gini(counter_below,records_below)
        gini_above = get_gini(counter_above, records_above)            
        
        gini_of_partition = (float(records_above)/total_records)*gini_above + (float(records_below)/total_records)*gini_below
        if gini_of_partition < mingini:
            mingini = gini_of_partition
            minpartition = sorted_amt_name_list[i][0]

    return mingini,minpartition


#print cand_nm_counter
print "Total Records: %s"%(total_records)
print "Q1: Gini Index: %s" % gini
print "Q2: Gini Index after split: %s" % split_gini
print "**********************************"
print "Extra Credit Method1 ==> Mean as partition: %s"%(mean)
print "Gini Index for Method1: %s" %(gini_partition)
print "**********************************"
print "Extra Credit Method2 ==> Finding minimum gini with  each pair as partition"
min_gini = best_gini_meth2(amt_name_list,total_records)
print "Gini Index for Method2: %s with partition at: %s" %(min_gini[0], min_gini[1])
