# coding:utf-8

inf = float('inf')
"""
graph =[
	[131,673,234,103,18],
	[201,96,342,965,150],
	[630,803,746,422,111],
	[537,699,497,121,956],
	[805,732,524,37,331]
	]
"""

def getGraph(path):
	graph = []
	for line in open(path,"r"):
		row = map(int, line.split(','))
		graph.append(row)
	return graph

def getNeighbor(y,x):
	return [y-1,x],[y+1,x],[y,x-1],[y,x+1]

def getNowNode(check_table,scores, MAX_Y, MAX_X):
	min_node = inf
	node = [0,0]
	for y in range(0,MAX_Y):
		for x in range(0,MAX_X):
			if min_node>scores[y][x] and check_table[y][x] == 0:
					min_node = scores[y][x]
					node = [y,x]
	return node

def unChecked(check_table, MAX_Y, MAX_X):
	Y = len(check_table)
	X = len(check_table[0])
	for y in range(0,MAX_Y):
		for x in xrange(0,MAX_X):
			if check_table[y][x] == 0:
				return 1 #未処理がある
	return 0

def notIn(y, x, MAX_Y, MAX_X):
	if x<=-1 or MAX_X<=x:
		return 1
	if y<=-1 or MAX_Y<=y:
		return 1
	return 0

def dijkstra(graph):
	MAX_X = len(graph[0])
	MAX_Y = len(graph)
	scores = [[inf]*MAX_X for i in range(0,MAX_Y)]
	scores[0][0] = graph[0][0]
	check_table = [[0]*MAX_X for i in range(0,MAX_Y)]

	while unChecked(check_table,MAX_Y, MAX_X):
		#現在のノード = 最小ノード
		(now_y,now_x) = getNowNode(check_table,scores, MAX_Y, MAX_X)
		neighbor = getNeighbor(now_y,now_x)
		for (y,x) in neighbor:
			if notIn(y,x,MAX_Y,MAX_X):
				continue
			prescore = scores[now_y][now_x] + int(graph[y][x])
			if scores[y][x] > prescore:
				scores[y][x] = prescore
		check_table[now_y][now_x] = 1
	print scores[-1][-1]

if __name__=="__main__":
	graph = getGraph("p083_matrix.txt")
	dijkstra(graph)
