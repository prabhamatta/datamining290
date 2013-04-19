import networkx as nx
import matplotlib.pyplot as plt

#Graph1 is a directed graph
node_list1 = [2,3,5,7,8,9,10,11]
edges_list1 = [(3,8),(3,10),(5,11),(7,11),(7,8),(8,9),(11,2),(11,9),(11,10)]

#Creating Directed Graph  
print "*************"
print "Graph1"
print "*************"
G1=nx.DiGraph()
G1.add_nodes_from(node_list1)
G1.add_edges_from(edges_list1)
print "Adjacency Matrix for Graph1:"
print nx.adjacency_matrix(G1)
print "\nAdjacency List for Graph1:"
for line in nx.generate_adjlist(G1,delimiter=','):
    print line
print "\nMy own representation of Adjacency List for Graph1:"
for line in nx.generate_adjlist(G1, ):
    print"{}===>{}".format(line.strip().split()[0], line.strip().split()[1:])
print "\nAnother representation of Graph1:"
for n,adj_nodes in G1.adjacency_iter():
    print "{}, {}".format(n,adj_nodes.keys())
#drawing graph using matplotlib    
nx.draw(G1)
plt.draw()
plt.savefig("graph1.png")
plt.close()

#Graph2 is an undirected graph
print "\n\n"
print "*************"
print "Graph2"
print "*************"
node_list2 = [1,2,3,4,5,6]
edge_list2 = [(1,2),(1,5),(2,5),(2,3),(3,4),(4,5),(4,6)]
G2= nx.Graph()
G2.add_nodes_from(node_list2)
G2.add_edges_from(edge_list2)
print "Adjacency Matrix for Graph2:"
print nx.adjacency_matrix(G2)
print "Adjacency List for Graph2:"
for n,adj_nodes in G2.adjacency_iter():
    print "{}, {}".format(n,adj_nodes.keys())

#drawing graph using matplotlib    
nx.draw(G2)
plt.draw()
plt.savefig("graph2.png")
plt.close()
print "\n\nPlease open graph1.png(directed graph of G1) and graph2.png(undirected graph of G2) to see the graphs..\n"





