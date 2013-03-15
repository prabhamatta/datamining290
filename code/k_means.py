import random

###
# Implement simple k-means clustering using 1 dimensional data
#
##/


dataset = [-13.65089255716321, -0.5409562932238607, -88.4726466247223, 39.30158828358612, 4.066458182574449, 64.64143300482378, 38.68269424751338, 33.42013676314311, 31.18603331719732, -0.2027616409406292, 45.13590038987272, 30.791899783552395, 61.1727490302448, 18.167220741624856, 88.88077709786394, -1.3808002119514704, 50.14991362212521, 55.92029956281276, -6.759813255299466, 34.28290084421072]
k = 2 # number of clusters

###
# Helper functions
# Fill in TODOs where needed
##/
# ectra credit
#1) use random data set
#2) do some visualtion on an axis
#3) calcualte usign different k


def pick_centroids(xs, num):
    """Return list of num centroids given a list of numbers in xs"""
    ###
    
    # Randomly choosing num elements from the data set   
    return random.sample(xs,num)
        
    ##/

def distance(a, b):
    """Return the distance of numbers a and b"""
    ##to find which centroid this pt is closest to
    ###
    # TODO return correct expression
    return abs(a-b)
    ##/

def centroid(xs):
    """Return the centroid number given a list of numbers, xs"""
    # calcuatin the new centroid for the cluster
    #centroid= avg of the cluster - it is a 1-dimensional no.
    ###
    # TODO calculate and return centroid
    return sum(xs)/len(xs)
    ##/

def cluster(xs, centroids):
    """Return a list of clusters centered around the given centroids.  Clusters
    are lists of numbers."""
    ## dont do anything here - 
    ##to find which cluster it belongs to

    clusters = [[] for c in centroids]

    for x in xs:
        # find the closest cluster to x
        dist, cluster_id = min((distance(x, c), cluster_id)
                for cluster_id, c in enumerate(centroids))
        # place x in cluster
        clusters[cluster_id].append(x)

    return clusters

def iterate_centroids(xs, centroids):
    """Return stable centroids given a dataset and initial centroids"""

    err = 0.001  # minimum amount of allowed centroid movement
    observed_error = 1  # Initialize: maxiumum amount of centroid movement
    new_clusters = [[] for c in centroids]  # Initialize: clusters

    while observed_error > err:
        new_clusters = cluster(xs, centroids)
        new_centroids = map(centroid, new_clusters)

        observed_error = max(abs(new - old) for new, old in zip(new_centroids, centroids))
        centroids = new_centroids

    return (centroids, new_clusters)


###
# Main part of program:
# Pick initial centroids
# Iterative to find final centroids
# Print results
##/
print ("*****************")
initial_centroids = pick_centroids(dataset, k)
##clusters----->list of no.s
final_centroids, final_clusters = iterate_centroids(dataset, initial_centroids)
## pair the centroid
for centroidpt, finalcluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroidpt
    print "Cluster contents: %r" % finalcluster
    
    
print("\n****************")
print("Removing outliers -88.4726466247223, 88.88077709786394 and finding centroids again...")
newdataset = dataset[:]
newdataset.remove(-88.4726466247223)
newdataset.remove(88.88077709786394)
initial_centroids = pick_centroids(newdataset, k)
final_centroids, final_clusters = iterate_centroids(newdataset, initial_centroids)
for centroidpt, finalcluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroidpt
    print "Cluster contents: %r" % finalcluster
print("\n** Observation: Centroids and Clusters are greatly affected by outliers **")


print("\n****************")
print("Calculating 2 centroids and clusters using random dataset of 25 numbers choosen between -100 and 100")
rand_dataset = [ random.uniform(-100,100) for i in range(1,25)]
initial_centroids = pick_centroids(rand_dataset, k)
final_centroids, final_clusters = iterate_centroids(rand_dataset, initial_centroids)
for centroidpt, finalcluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroidpt
    print "Cluster contents: %r" % finalcluster
    
print("\n****************")
print("Calculating 2 centroids and clusters using random dataset of 50 numbers choosen between -100 and 100")
rand_dataset = [ random.uniform(-100,100) for i in range(1,50)]
initial_centroids = pick_centroids(rand_dataset, k)
final_centroids, final_clusters = iterate_centroids(rand_dataset, initial_centroids)
for centroidpt, finalcluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroidpt
    print "Cluster contents: %r" % finalcluster    
    

print("\n****************")
print("Calculating 3 centroids and clusters for the given dataset using k = 3...")

new_k = 3
initial_centroids = pick_centroids(dataset, new_k)
final_centroids, final_clusters = iterate_centroids(dataset, initial_centroids)
for centroidpt, finalcluster in zip(final_centroids, final_clusters):
    print "Centroid: %s" % centroidpt
    print "Cluster contents: %r" % finalcluster