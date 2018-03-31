class Node:
	next_id = 0
	NODE_XML = """<node id="{0}">
			 <data key="label">{1}</data>
			 </node>\n"""
	
	def __init__(self, name):
		self._name = name
		self._id = Node.next_id 
		Node.next_id += 1

	def getName(self):
		return self._name

	def getId(self):
		return self._id

	def __str__(self):
		return Node.NODE_XML.format(self._id, self._name).replace('\t', '')

class Edge:
	EDGE_XML = """<edge source="{0}" target="{1}">
				<data key="weight">{2}</data>
				</edge>\n"""
	
	def __init__(self, source, target):
		self._source = source
		self._target = target
		self._weight = 1	

	def incrementWeight(self):
		self._weight += 1

	def __str__(self):
		return Edge.EDGE_XML.format(self._source, self._target, self._weight).replace('\t', '')

HEADER_XML = """<?xml version="1.0" encoding="UTF-8"?>
				<graphml xmlns="http://graphml.graphdrawing.org/xmlns">
				<key attr.name="label" attr.type="string" for="node" id="label"/>
				<key attr.name="weight" attr.type="int" for="edge" id="weight"/>
				<graph edgedefault="undirected">\n""".replace('\t', '')

FOOTER_XML = """</graph>\n</graphml>\n"""

				
