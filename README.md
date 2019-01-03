# Distance_Vector
**1. Overview**
In this lab, we are asked to implement a routing algorithm, distance vector, under distributed, asynchronous scenario. The network use in this lab has topology shown figure 1.
  ![Alt text] (https://github.com/OscarLi9328/Distance_Vector/blob/master/topology.png "Optional title")

**2. Introduction**
Distance vector is a routing algorithm. Under this algorithm, each node maintain a table recording its connection cost to different nodes and update its table by calculating the cost sent from its neighboring nodes. Take node 0 for example, it should maintain a table recording its connection cost to node 1, 2, and 3 since they are all neighboring nodes connected by some link. The initial table of node 0 would look like this: 
  ![Alt text] (https://github.com/OscarLi9328/Distance_Vector/blob/master/D0.png?raw=true "Optional Title")

If the cost of  is infinite, node 0 cannot directly connect with node  via node  at this time. 
Each node will send its own table to its neighboring nodes and receive the table from its neighboring nodes to update the table. This procedure will be operating until no change of the value of one’s table is made. At this point, the routing algorithm converges and each node will have the same routing table. 

**3. Implementation**
I use python to implement this lab assignment. I initialized each entry of the cost table as , which is represented by 999. Initialize two arrays, one for recording the link cost, the other for recording the cost the one node.
![Alt text] (https://github.com/OscarLi9328/Distance_Vector/blob/master/initialization.png?raw=true "Optional Title")
The basic idea of how to implement the algorithm is shown in Figure 2. During the initialization process, the diagonal of the table will be the link cost to each neighboring node. Before the initial table is sent to neighbor nodes, it has to be wrapped into packets. The initialization process of each node is referenced as rtinit( ) in my codes. 
After initialization, the next process, rtupdate( ), is to update the table. The routine takes the received vector and recalculate the cost to the node who sends the vector. 
The updating rule is to find the minimum value between the new and old values. The old values are the original value that the node maintain. The new value is calculated by taking the cost to a neighbor and added with the corresponding entry of the received vector. If the table values change, send to its neighbors. 

