import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from([
    ('RMUTT', 'NBU', {'distance': 9.5}),
    ('RMUTT', 'EAU', {'distance': 4.5}),
    ('RMUTT', 'VRU', {'distance': 35.9}),
    ('RMUTT', 'TU', {'distance': 16.8}),
    ('EAU', 'TU', {'distance': 20.3}),
    ('EAU', 'BU', {'distance': 19.7}),
    ('EAU', 'NBU', {'distance': 9.2}),
    ('BU', 'TU', {'distance': 3.7}),
    ('BU', 'NBU', {'distance': 17.5}),
    ('BU', 'PTU', {'distance': 16.2}),
    ('BU', 'RSU', {'distance': 18}),
    ('TU', 'VRU', {'distance': 13.8}),
    ('TU', 'PTU', {'distance': 15}),
    ('TU', 'MRU', {'distance': 34.8}),
    ('VRU', 'MRU', {'distance': 35.9}),
    ('PTU', 'MRU', {'distance': 22}),
    ('PTU', 'RPU', {'distance': 27.4}),
    ('MRU', 'RPU', {'distance': 20.7}),
    ('RPU', 'RSU', {'distance': 34.7}),
    ('RSU', 'NBU', {'distance': 13.7}),
    ('KMUTNB', 'RSU', {'distance': 30.3}),
    ('KMUTNB', 'RPU', {'distance': 43.5}),
    ('KMUTNB', 'MU', {'distance': 24.6}),
    ('KMUTNB', 'CU', {'distance': 17.5}),
    ('KMUTNB', 'NBU', {'distance': 18.1}),
    ('MU', 'CU', {'distance': 29.2}),
    ('MU', 'KMUTT', {'distance': 33.8}),
    ('CU', 'KMUTT', {'distance': 15.1}),
    ('CU', 'KMITL', {'distance': 33.3}),
    ('KMITL', 'KMUTT', {'distance': 46.6}),
    ('KMITL', 'NBU', {'distance': 39.2}),
])
pos = {'BU':(7,6.4),'RMUTT':(10.4,6),'TU':(7,8),'NBU':(9.5,4.3),'PTU':(5,6.5),'MRU':(2.5,8.8),'RSU':(6.5,4.5),
       'RPU':(3,6.5),'VRU':(9,9),'EAU':(8.6,6),'MU':(1,3),'KMUTNB':(3,3.5),'CU':(4.5,2),'KMUTT':(3.5,0.5),'KMITL':(8.5,1),}

# Define a function to execute the code when the button is clicked
def search_nodes():
    global shortest_path
    valid_nodes = ['BU', 'RMUTT', 'TU', 'NBU', 'PTU', 'MRU', 'RSU', 'RPU', 'VRU', 'EAU', 'MU', 'KMUTNB', 'CU', 'KMUTT', 'KMITL']
    source = source_entry.get()
    while source not in valid_nodes:
        source = input(f"{source} is not a valid node. Please enter a valid source node: ")
    dest = dest_entry.get()
    while dest not in valid_nodes:
        dest = input(f"{dest} is not a valid node. Please enter a valid destination node: ")
    shortest_path = nx.shortest_path(G, source=source, target=dest, weight='distance')
    shortest_path_length = nx.shortest_path_length(G, source=source, target=dest, weight='distance')
    shortest_path_length = ("%.2f"%(shortest_path_length))
    node_color_map = []
    for node in G.nodes():
        if node == shortest_path[0]:
            node_color_map.append('green')
        elif node == shortest_path[-1]:
            node_color_map.append('red')
        elif node in shortest_path:
            node_color_map.append('yellow')
        else:
            node_color_map.append('gray')

    nx.draw_networkx(G, pos, with_labels=True, node_color=node_color_map, node_size=1000)
    edge_labels = nx.get_edge_attributes(G, 'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edge_list = list(zip(shortest_path, shortest_path[1:]))
    plt.title("Distance of University", size=12)
    plt.show()

# Create the Tkinter window
root = tk.Tk()
root.title("Shortest Path Calculator")

# Add labels and entry boxes for source and destination
source_label = tk.Label(root, text="Enter beginning from: ")
source_label.pack()
source_entry = tk.Entry(root)
source_entry.pack()

dest_label = tk.Label(root, text="Enter destination: ")
dest_label.pack()
dest_entry = tk.Entry(root)
dest_entry.pack()

# Add a button to initiate the search
search_button = tk.Button(root, text="Search", command=search_nodes)
search_button.pack()

# Start the Tkinter event loop
root.mainloop()
