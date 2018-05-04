import itertools
import graphelements

author_set = set()
edges_dict = dict()

with open('./../cleaned_arXiv.txt', 'r') as infile:
	for row in infile:
		data = row.replace('\n', '').split('|')
		coauthors = data[1].split(',')
		divided_weight = 1 / len(coauthors)

		for author in coauthors:
			author_set.add(author)

		for pair in itertools.combinations(coauthors, 2):
			key = ''.join(sorted(pair))

			if key not in edges_dict:
				edges_dict[key] = graphelements.Edge(*pair, divided_weight)
			else:
				edges_dict[key].incrementWeight(divided_weight)

with open('./../new_coauthorship.graphml', 'w') as outfile:
	outfile.write(graphelements.HEADER_XML)

	for author in author_set:
		node = graphelements.Node(author)

		outfile.write(str(node))

	for key, edge in edges_dict.items():
		outfile.write(str(edge))

	outfile.write(graphelements.FOOTER_XML)
