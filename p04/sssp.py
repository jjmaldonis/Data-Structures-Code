import heapq
def single_source_shortlest_path(self,n):
    #A heap pops off the thing that is the lowest in the heap
    queue = []
    #queue = Heap()
    #Inserting as a tuple
    heapq.heappush(queue,(0,n))
    dist = {n:0}
    path = {n:None}
    visited = {}
    while(len(queue)):
        #The following line actually works in python because we are inserting tuples!
        weight, curnode = heapq.heappop( queue )
        if curnode in visited:
            continue
        visited[curnode] = True
        for nnode in self[curnode]:
            neighDist = dist[curnode] + self[curnode][nnode]
            if nnode not in dist or nieghDist < dist[nnode]:
                dist[nnode] = neighDist
                path[nnode] = curnode
                heapq.heappush(queue, (neighDist,nnode) )
    return dist


