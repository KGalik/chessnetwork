#Chess Network

###Data Retrieval

The program uses python's urllib module to retrieve html data from the https://en.wikipedia.org/wiki/Chess_World_Cup_2017 wikipedia page. The page contains tables displaying the matches and outcomes of the 2017 Chess World Cup along with a list of participants.

###Regular Expressions

The python regular expressions module (re) is then used to extract the data from the tables and the participants from the list of players.

###Network Visualization

The data is then arranged as edges in a undirected network and plotted using the matplotlib and networkx python modules. Because the tournament features elimination matches, the network inherits acyclicity. Due to tournament circumstances caused by the dress code controversy, the network is missing an edge and takes the form of two trees. Yaroslav Zherebukh did not participate in the tournament and is not included in the network.
