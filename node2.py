from utils import TRACE, YES, NO, Rtpkt, tolayer2


class DistanceTable:
    costs = [[999 for j in range(4)] for i in range(4)]

dt = DistanceTable()

# students to write the following two routines, and maybe some others

# modify this statement for different node
edges = [3, 1, 0, 2]
cost = [3, 1, 0, 2]
node_id = 2

def rtinit2():
    for i in range(4):
        if i == node_id:  
            continue
        dt.costs[i][i] = edges[i]

    printdt2(dt)

    tolayer2(Rtpkt(node_id, 0, edges))
    tolayer2(Rtpkt(node_id, 1, edges))
    tolayer2(Rtpkt(node_id, 3, edges))


def rtupdate2(rcvdpkt):
    change = False
    srcid = rcvdpkt.sourceid
    table = rcvdpkt.mincost

    for i in range(4):
        tmp = edges[srcid] + table[i]
        dt.costs[i][srcid] = min(dt.costs[i][srcid], tmp)
        if tmp < cost[i]:
            change = True
            cost[i] = tmp

    printdt2(dt)
    if change:
        tolayer2(Rtpkt(node_id, 0, cost))
        tolayer2(Rtpkt(node_id, 1, cost))
        tolayer2(Rtpkt(node_id, 3, cost))


def printdt2(dtptr):
  print("                via     \n")
  print("   D2 |    0     1    3 \n")
  print("  ----|-----------------\n")
  print("     0|  %3d   %3d   %3d\n" %
        (dtptr.costs[0][0], dtptr.costs[0][1], dtptr.costs[0][3]))
  print("dest 1|  %3d   %3d   %3d\n" %
        (dtptr.costs[1][0], dtptr.costs[1][1], dtptr.costs[1][3]))
  print("     3|  %3d   %3d   %3d\n" %
        (dtptr.costs[3][0], dtptr.costs[3][1], dtptr.costs[3][3]))

# rtinit2()
# printdt2(dt)