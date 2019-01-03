from utils import TRACE, YES, NO, Rtpkt, tolayer2


class DistanceTable:
    costs = [[999 for j in range(4)] for i in range(4)]

dt = DistanceTable()

# students to write the following two routines, and maybe some others

# modify this statement for different node
edges = [1, 0, 1, 999]
cost = [1,  0,  1, 999]
node_id = 1

def rtinit1():
    for i in range(4):
        if i == node_id:
            continue
        dt.costs[i][i] = edges[i]
        
    printdt1(dt)
    tolayer2(Rtpkt(node_id, 0, edges))
    tolayer2(Rtpkt(node_id, 2, edges))
 

def rtupdate1(rcvdpkt):
    change = False
    srcid = rcvdpkt.sourceid
    table = rcvdpkt.mincost

    for i in range(4):
        tmp = edges[srcid] + table[i]
        dt.costs[i][srcid] = min(dt.costs[i][srcid], tmp)
        if tmp < cost[i]:
            change = True   
            cost[i] = tmp 
    
    printdt1(dt)

    if change:
        tolayer2(Rtpkt(node_id, 0, cost))
        tolayer2(Rtpkt(node_id, 2, cost))


def printdt1(dtptr):
    print("             via   \n")
    print("   D1 |    0     2 \n")
    print("  ----|-----------\n")
    print("     0|  %3d   %3d\n" % (dtptr.costs[0][0], dtptr.costs[0][2]))
    print("dest 2|  %3d   %3d\n" % (dtptr.costs[2][0], dtptr.costs[2][2]))
    print("     3|  %3d   %3d\n" % (dtptr.costs[3][0], dtptr.costs[3][2]))


def linkhandler1(linkid, newcost):
    '''called when cost from 1 to linkid changes from current value to newcost
    You can leave this routine empty if you're an undergrad. If you want
    to use this routine, you'll need to change the value of the LINKCHANGE
    constant definition in prog3.c from 0 to 1
    '''
    pass

# rtinit1()
# printdt1(dt)