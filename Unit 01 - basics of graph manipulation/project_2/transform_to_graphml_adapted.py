'''
The followig code is a little adaptation of the script found at Alvaro's repository:

https://github.com/alvarofpp/dataset-flights-brazil/blob/main/transform_to_graphml.py

There, beyond what he has done, the region and state were added as attributes on the graph's nodes.
'''
import numpy as np
import nxviz as nv
import pandas as pd
import networkx as nx



df_airports = pd.read_csv('data/airports.csv')
df_flights = pd.read_csv('data/anac.csv')

# Create graph
G = nx.Graph()

# Add nodes
for index, row in df_airports.iterrows():
    if row['country'] == 'BRASIL':
        G.add_node(row['code'],
                name=row['name'],
                country=row['country'],
                region=row['region'],
                state=row['state'],
                latitude=row['lat_geo_point'],
                longitude=row['lon_geo_point']
        )

# Add edges
df_edges = df_flights[[
    'origin_airport_abbreviation',
    'destination_airport_abbreviation',
]].dropna()
df_edges = df_edges.groupby(df_edges.columns.tolist(), as_index=False).size()
for index, row in df_edges.iterrows():
    if row['origin_airport_abbreviation'] == row['destination_airport_abbreviation']:
        continue
    G.add_edge(row['origin_airport_abbreviation'], row['destination_airport_abbreviation'], flight_count=row['size'])

# filtering by country='BRASIL'
nodes = (node for node, attributes in G.nodes(data=True) if attributes.get('country') == 'BRASIL')
G = G.subgraph(nodes)

# Export to graphml
nx.write_graphml(G, 'data/air_traffic.graphml')