import osmnx as ox
import pandas as pd
import geopandas as gpd
import networkx as nx
#%matplotlib inline
ox.config(log_console=True, use_cache=True)

# This function takes the road name and a 3-letter code for the language and it returns the colour
def colourcode(x, language):
    if (language=='GER'):
        if ('straße' in x): 
            return '#f6cf71'
        elif ('weg' in x):
            return '#019868'
        elif ('allee' in x):
            return '#ec0b88'
        elif ('damm' in x):
            return '#651eac'
        elif ('platz' in x):
            return '#e18a1e'
        elif ('chaussee' in x):
            return '#9dd292'
        elif ('see' in x):
            return '#2b7de5'
        elif ('ufer' in x):
            return '#2b7de5'
        elif ('steg' in x):
            return '#2b7de5'
        else:
            return '#c6c6c6'
    elif (language=='ENG'):
        if ('road' in x): 
            return '#019868'
        elif ('street' in x):
            return '#f6cf71'
        elif ('way' in x):
            return '#ec0b88'
        elif ('avenue' in x):
            return '#651eac'
        elif ('drive' in x):
            return '#e18a1e'
        elif ('lane' in x):
            return '#9dd292'
        else:
            return '#c6c6c6'
    elif (language=='FRA'):
        if ('rue' in x): 
            return '#019868'
        elif ('place' in x):
            return '#f6cf71'
        elif ('avenue' in x):
            return '#ec0b88'
        elif ('boulevard' in x):
            return '#651eac'
        elif ('passage' in x):
            return '#e18a1e'
        elif ('pont' in x):
            return '#9dd292'
        elif ('quai' in x):
            return '#2b7de5'
        else:
            return '#c6c6c6'
    else:
        return 'black'

# Set place and language; the place is basically a Nominatim query. It must return a POLYGON/POLYLINE, not a POINT, so you might have to play with it a little, or set which_result below accordingly    
place='Newbury, Berkshire, United Kingdom'
language='ENG'

# note the which_result parameter, as per comment above
G = ox.graph_from_place(place, network_type='all', which_result=2) 

# For the colouring, we take the attributes from each edge found extract the road name, and use the function above to create the colour array
edge_attributes = ox.graph_to_gdfs(G, nodes=False)
ec = [colourcode(str(row['name']).lower(), language) for index, row in edge_attributes.iterrows()]

# We can finally draw the plot
fig, ax = ox.plot_graph(G, bgcolor='white', axis_off=True, node_size=0, node_color='w', node_edgecolor='gray', node_zorder=2,
                        edge_color=ec, edge_linewidth=0.5, edge_alpha=1, fig_height=20, dpi=300)
