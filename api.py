# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, make_response, send_file, json
from flask_cors import CORS
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt
from io import BytesIO

# creating a Flask app
app = Flask(__name__)
CORS(app)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
@app.route('/addrelationship', methods=['POST'])

def addrelationship():
    details = request.data
    decoded = json.loads(details)
    testing = eval(decoded)
    G = nx.DiGraph()
    for i in range(len(testing)):
        G.add_node(testing[i]['fentity'],name=testing[i]['fentity'])
        G.add_node(testing[i]['sentity'],name=testing[i]['sentity'])
        G.add_edge(testing[i]['fentity'], testing[i]['sentity'], start=testing[i]['fentity'], end=testing[i]['fentity'],relation=testing[i]['fentity']+' '+testing[i]['relationship']+' '+testing[i]['sentity'])
    pos = nx.spring_layout(G)
    nx.draw(G,pos)
    node_labels = nx.get_node_attributes(G,'name')
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    # nx.draw(G,node_color='red',labels={node: node for node in G.nodes()})
    img = BytesIO()  # file-like object for the image
    plt.savefig(img)  # save the image to the stream
    img.seek(0)  # writing moved the cursor to the end of the file, reset
    plt.clf()  # clear pyplot
    return send_file(img, mimetype='image/png')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
