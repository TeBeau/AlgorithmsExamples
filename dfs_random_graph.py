import random

def make_graph(n, p):
    adjlist=[]
    for i in range(0,n):
        ilist=[]
        adjlist.append(ilist)
    for i in range(0,n):
        for j in range(0,n):
            if random.random() >= p:
                if j not in adjlist[i]:
                    adjlist[i].append(j)
                if i not in adjlist[j]:
                    adjlist[j].append(i)
    return adjlist

def connected(graph, n):
    queue=[n]
    connected= []
    while len(queue) > 0:
        i=queue[0]
        for j in graph[i]:
            if j not in connected:
                queue.append(j)
                connected.append(j)
        queue.remove(i)
    return len(connected)

def check_size(graph, t, n):
    largest=0
    for i in range(0,n):
        size= connected(graph, i)
        if size>largest: 
            largest= size
    if largest >= t:
        return True 
    else:
        return False 

def make_test_graph(n, p):
    adjlist=[]
    for i in range(0,n):
        ilist=[]
        adjlist.append(ilist)
    for i in range(0,n):
        for j in range(0,n):
            if random.random() <= p:
                if j not in adjlist[i]:
                    adjlist[i].append(j)
                if i not in adjlist[j]:
                    adjlist[j].append(i)
    return adjlist
n= int(input("Enter number of nodes: "))
p= float(input("Enter a probability: "))
t= int(input("Enter size of largest connected componant: "))

#Part a
graph= make_graph(n, p)
print("Graph made: ")
for l in range(0,n):
    print("node ", l, ": ", graph[l])

#Part b
is_con= check_size(graph, t, n)
print("Is this graph's connections large enough? ", is_con, "!!!")

#Part c
graphs=[]
n= 40
t=30
c=.2
while c <= 3.0:
    newp= c/n 
    numt=0
    for g in range(0, 500):
        graph = make_test_graph(n,newp)
        graphs.append(graph)
        if check_size(graph, t, n) == True:
            numt= numt+1
      
    print("c= ", c, " Percent t = ", (numt/500)*100)
    c = c+.2






