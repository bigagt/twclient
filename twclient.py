from graph_tool.all import *
import telnetlib

graph = Graph()

v1 = graph.add_vertex()
v2 = graph.add_vertex()
v3 = graph.add_vertex()

e1 = graph.add_edge(v1, v3)
e2 = graph.add_edge(v2, v3)
e3 = graph.add_edge(v3, v1)

graph_draw(graph, vertex_text=graph.vertex_index, vertex_font_size=18, output_size=(200,200), output="twclientgraph.png")