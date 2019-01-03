from utils import TRACE, YES, NO, Rtpkt, tolayer2


class DistanceTable:
    costs = [[999 for j in range(4)] for i in range(4)]

dt = DistanceTable()

# students to write the following two routines, and maybe some others

# modify this statement for different node
edges = [0, 1, 3, 7]
cost = [0, 1, 3, 7]
node_id = 0

def rtinit0():
    for i in range(4):
        if i == node_id:
            continue
        dt.costs[i][i] = edges[i]
    printdt0(dt)

    tolayer2(Rtpkt(node_id, 1, edges))
    tolayer2(Rtpkt(node_id, 2, edges))
    tolayer2(Rtpkt(node_id, 3, edges))


def rtupdate0(rcvdpkt):
    change = False
    srcid = rcvdpkt.sourceid
    table = rcvdpkt.mincost

    for i in range(4):
        tmp = edges[srcid] + table[i]
        dt.costs[i][srcid] = min(dt.costs[i][srcid], tmp)
        if tmp < cost[i]:
            change = True
            cost[i] = tmp

    printdt0(dt)

    if change:
        tolayer2(Rtpkt(node_id, 1, cost))
        tolayer2(Rtpkt(node_id, 2, cost))
        tolayer2(Rtpkt(node_id, 3, cost))


def printdt0(dtptr):
    print("                via     \n")
    print("   D0 |    1     2    3 \n")
    print("  ----|-----------------\n")
    print("     1|  %3d   %3d   %3d\n" %
          (dtptr.costs[1][1], dtptr.costs[1][2], dtptr.costs[1][3]))
    print("dest 2|  %3d   %3d   %3d\n" %
          (dtptr.costs[2][1], dtptr.costs[2][2], dtptr.costs[2][3]))
    print("     3|  %3d   %3d   %3d\n" %
          (dtptr.costs[3][1], dtptr.costs[3][2], dtptr.costs[3][3]))


def linkhandler0(linkid, newcost):
    '''called when cost from 0 to linkid changes from current value to newcost
    You can leave this routine empty if you're an undergrad. If you want
    to use this routine, you'll need to change the value of the LINKCHANGE
    constant definition in prog3.c from 0 to 1
    '''
    pass
# 
# rtinit0()
# printdt0(dt)