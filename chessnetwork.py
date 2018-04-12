#!/usr/bin/python
# coding: utf-8
import urllib
import re
import matplotlib.pyplot as plt
import networkx as nx

def main():
    uf = urllib.urlopen("https://en.wikipedia.org/wiki/Chess_World_Cup_2017") #opens wikipedia data
    webstring = uf.read() #reads data into string
    webstring = webstring.replace("½",".5") #replaces unicode fractions
    
    #finds player names on page
    #includes some unicode characters found in names
    rankings = re.findall(r'>([\w -.łÉáčễọườơőí]+)</a>[, \w]*&#160;<span style="font-size:90%;">\(<abbr title="[\w ()]+">\w+</abbr>\)</span>, \d+', webstring, re.U)

    #finds information about matches played in two searches
    games1 = re.findall(r'<td rowspan="2" style="text-align:center;background-color:#f2f2f2;border-color:#aaa;border-style:solid;border-top-width:1px;border-left-width:1px;border-right-width:1px;border-bottom-width:1px">(\d+)</td>', webstring, re.U)
    games2 = re.findall(r'<td rowspan="2" style="text-align:center;border-color:#aaa;border-style:solid;border-top-width:1px;border-left-width:1px;border-right-width:1px;border-bottom-width:1px;background-color:#f9f9f9">[<b>]*([\d.]+)[<b>/]*</td>', webstring, re.U)
    del games1[173], games1[172], games1[29], games1[28] #deletes walkover games
    games1[248] = 51 #fixes typo on webpage
    #generates list of match scores
    games = [(rankings[int(games1[i])-1], rankings[int(games1[i+1])-1], float(games2[i]), float(games2[i+1])) for i in range(len(games1)) if i % 2 == 0]
    
    #arranges matches in order of loser number first for potential use with directed networks
    for i in range(len(games)):
        if games[i][2] > games[i][3]:
            games[i] = (games[i][1], games[i][0], games[i][3], games[i][2])
    
    #produces a graph of the games played between players (ignores player that did not attend)
    #effects of dress code controversy can be seen in graph as the separate connected component containing only 4 nodes
    G = nx.Graph()
    G.add_edges_from([(games[i][0], games[i][1]) for i in range(len(games))]) #uses player number for nodes
    pos = nx.spring_layout(G,k=0.1,iterations=50)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 10)
    nx.draw_networkx_edges(G, pos, arrow=True)
    plt.show()

if __name__ == '__main__':
    main()