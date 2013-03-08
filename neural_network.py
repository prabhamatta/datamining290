def calculate_outputlayer_err(true_val,out_val):
    return out_val*(1-out_val)*(true_val-out_val)

def calculate_node_err(node_j,err_wt_list):
    sum_err_wt = 0
    for err,wt in err_wt_list:
        sum_err_wt += err*wt
    return node_j*(1-node_j)*sum_err_wt

def calculate_wt(wt_ij,l,err_j,node_i):
    return wt_ij + (l*err_j*node_i)
 
if __name__ == "__main__":
    l = 10
    true_val = 0
    inputNodes = [1,2]
    hiddenNodes = [0.7311, 0.0179, 0.9933]
    outputNodes = [0.8386]
    nodes = {'n1':1,'n2':2,'n3':0.7311, 'n4': 0.0179, 'n5': 0.9933, 'n6':0.8387 }
    weights = {'w13':-3,'w14':2,'w15':4,'w23':2,'w24':-3,'w25':0.5,'w36':0.2,'w46':0.7 ,'w56':1.5}
    print "\nNodes and Weights..."
    for k,v in nodes.items():
        print "node %s: %s"%(k,v)
    for k,v in weights.items():
         print "Weight %s: %s"%(k,v) 
         
    #Calculating Error at Nodes 
    err_6 = calculate_outputlayer_err(true_val, nodes['n6'])
    
    err_wt_list_5 = [(err_6,weights['w56'])]    
    err_5 = calculate_node_err(nodes['n5'],err_wt_list_5)
    
    err_wt_list_4 = [(err_6,weights['w46'])]
    err_4 = calculate_node_err(nodes['n4'],err_wt_list_4)
    
    
    err_wt_list_3 = [(err_6,weights['w36'])]
    err_3 = calculate_node_err(nodes['n3'],err_wt_list_3)
    
    # Input nodes are actual nodes, therefore the error at Node 1 and 2 would be zero
    err_2 = 0
    err_1 = 0
 
    #Calculating Error in Weights
    w_56 = calculate_wt(weights['w56'],l,err_6,nodes['n5'])
    
    w_46 = calculate_wt(weights['w46'],l,err_6,nodes['n4'])
   
    w_36 = calculate_wt(weights['w36'],l,err_6,nodes['n3'])
    
    w_23 = calculate_wt(weights['w23'],l,err_3,nodes['n2'])
    
    w_24 = calculate_wt(weights['w24'],l,err_4,nodes['n2'])
    
    w_25 = calculate_wt(weights['w25'],l,err_5,nodes['n2'])
    
    w_15 = calculate_wt(weights['w15'],l,err_5,nodes['n1'])
    
    w_14 = calculate_wt(weights['w14'],l,err_4,nodes['n1'])
    
    w_13 = calculate_wt(weights['w13'],l,err_3,nodes['n1'])
    
    print "\n\nErrors at Nodes and Weights..."
    print "err_1 = %s"%(err_1) 
    print "err_2 = %s"%(err_2)    
    print "err_3 = %s"%(err_3)    
    print "err_4 = %s"%(err_4)
    print "err_5 = %s"%(err_5)
    print "err_6 = %s"%(err_6)
    print "wt_13 = %s"%(w_13)  
    print "wt_14 = %s"%(w_14)  
    print "wt_15 = %s"%(w_15)  
    print "wt_23 = %s"%(w_23)  
    print "wt_24 = %s"%(w_24)  
    print "wt_25 = %s"%(w_25)  
    print "wt_36 = %s"%(w_36)  
    print "wt_46 = %s"%(w_46)    
    print "wt_56 = %s"%(w_56)
    
    
  