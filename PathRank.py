from Node import *

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

trust01 = 0.4
trust03 = 0.1
trust14 = 0.1
trust24 = 0.1
trust32 = 0.2
trust34 = 0.9

connections0 = [[node1, trust01], [node3, trust03]]
connections1 = [[node4, trust14]]
connections2 = [[node4, trust24]]
connections3 = [[node2, trust32], [node4, trust34]]
connections4 = []

node0.setConnections(connections0)
node1.setConnections(connections1)
node2.setConnections(connections2)
node3.setConnections(connections3)
node4.setConnections(connections4)

def __main__():
    path = rank(node0, node4)
    print("PATH: ", end="")
    for i in range(len(path)):
        print(path[i].label, end = ", ")

def rank(trusted:Node, target:Node):
    path = dijikstra(trusted, target)
    return path

def dijikstra(start:Node, end:Node):
    path = [start]
    path = calculatePath(start, end, path)
    return path

def calculatePath(current:Node, end:Node, prevPath:list):
    smallest = 7112002
    smallestIndex = -1
    path = prevPath

    for i in range(len(current.connections)):
        if (current.connections[i][1] < smallest):
            smallest = current.connections[i][1]
            smallestIndex = i

    path.append(current.connections[smallestIndex][0])

    if(path[len(path) - 1] != end):
        calculatePath(current.connections[smallestIndex][0], end, path)

    return path

if(__name__ == '__main__'):
    __main__();