import networkx as nx
import matplotlib.pyplot as plt
import scipy as spy
from networkx.algorithms import tournament
G= nx.Graph()

G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
G.add_node('F')
G.add_node('G')
G.add_node('H')
G.add_node('I')
G.add_node('J')
G.add_node('K')
G.add_node('L')
G.add_node('M')
G.add_node('N')
G.add_node('O')

G.add_edge('A','B')
G.add_edge('B','C')
G.add_edge('B','D')
G.add_edge('C','D')
G.add_edge('D','E')
G.add_edge('A','F')
G.add_edge('B','G')
G.add_edge('F','G')
G.add_edge('C','H')
G.add_edge('G','H')
G.add_edge('D','I')
G.add_edge('H','I')
G.add_edge('E','J')
G.add_edge('I','J')
G.add_edge('C','J')
G.add_edge('F','K')
G.add_edge('K','L')
G.add_edge('G','L')
G.add_edge('H','M')
G.add_edge('L','M')
G.add_edge('F','M')
G.add_edge('I','N')
G.add_edge('M','N')
G.add_edge('L','N')
G.add_edge('J','O')
G.add_edge('N','O')

print('''
\t--- Main Menu ---
PRESS '1' to Display Nodes Lists of the Graph
      '2' to Display Edge  Lists of the Graph
      '3' to Count Connected Components of the Graph
      '4' to Print Connected Components of the Graph
      '5' to Display Incidence Matrix of a Graph
      '6' to Display the Nodes Degrees
      '7' to Count Number of Edges
      '8' to Visualize the Graph
      '9' to Check if...
''')
optn= input("ENTER your Option-> ")

if optn =='1':
    print("Listed Nodes-> ",list(G.nodes))
elif optn=='2':
    print("Listed Edges-> ",list(G.edges))
elif optn=='3':
    print("Total Connected Components-> ", nx.number_connected_components(G))
elif optn=='4':
    print("Listed Connected Components->")
    for components in nx.connected_components(G):
        print(components)
elif optn=='5':
    print("Incidence Matrix-> \n", nx.incidence_matrix(G).todense())
elif optn=='6':
    vertex= input("ENTER a Node(from A-O) Name to View its Degree-> ")
    print("Degree of ",vertex,"-> ", G.degree[vertex])
elif optn=='7':
    print("Total Edges-> ", G.size())
elif optn=='8':
    nx.draw(G, with_labels = True, node_color ="black", font_color="white")
    plt.show()
elif optn=='9':
    print('''
    PRESS '1' to Check if Euler Circuit Exists or Not, and if Graph is Eulerian 
          '2' to Check if Euler  Path   Exists or Not                         
          '3' to Check if Hamilton Path Exists
          '4' Perform Depth First and Breadth First Traversal on Graph
    ''')

    optn2= input("ENTER your Option-> ")
    if optn2=='1':
        print("Euler Circuit Exists-> ", bool(nx.eulerian_circuit(G)))
    elif optn2=='2':
        print("Euler Path Exists-> ", bool(nx.eulerian_path(G)))
    elif optn2=='3':
        var= nx.to_directed(G)
        print("Hamilton Path Exists-> ", bool(nx.tournament.hamiltonian_path(var)))
    elif optn2=='4':
        print("BFS->", list(nx.bfs_edges(G,"A")))
        nx.draw(nx.bfs_tree(G,'A'))
        plt.show()
        print("DFS->", list(nx.dfs_edges(G,"A")))
        nx.draw(nx.dfs_tree(G,'A'))
        plt.show()
else:
    print("\t(INVALID OPTION!!)")
