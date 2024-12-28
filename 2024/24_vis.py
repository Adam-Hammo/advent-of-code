from graphviz import Digraph

# Shoutout to chatgpt for this one

# Your multiline string of gates:
gates_text = """\
REDACTED
"""

SWAPS = {"z11": "wpd", "jqf": "skh", "z19": "mdd", "z37": "wts"}
SWAPS |= {v: k for k,v in SWAPS.items()}
# SWAPS = {}

def parse_gate_line(line):
    """
    Example line: 'y33 AND x33 -> bfn'
    Returns: (input1='y33', operator='AND', input2='x33', output='bfn')
    """
    # Split at '->'
    left, out_wire = line.split('->')
    left = left.strip()
    out_wire = out_wire.strip()

    # left is something like 'y33 AND x33'
    parts = left.split()
    inp1, op, inp2 = parts[0], parts[1], parts[2]
    return inp1, op, inp2, SWAPS.get(out_wire, out_wire)

def wire_color(name):
    """
    Return a color string based on the wire's prefix:
      x* -> red
      y* -> blue
      z* -> green
      otherwise -> black
    """
    if name.startswith('x'):
        return 'red'
    elif name.startswith('y'):
        return 'blue'
    elif name.startswith('z'):
        return 'green'
    else:
        return 'black'

# Create a Digraph
dot = Digraph(comment="Logic Circuit Example")
dot.attr(rankdir='LR')  # Left-to-right layout (optional)

lines = gates_text.strip().split('\n')

# Keep track of which wire nodes we've already created
wire_nodes_added = set()

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    
    inp1, op, inp2, out_wire = parse_gate_line(line)
    
    # Create a unique name for the gate
    gate_name = f"gate_{i}"
    
    # Add the gate node (shape=box, light gray fill)
    dot.node(
        gate_name,         # node ID
        label=op,          # label to show (AND, XOR, OR, etc.)
        shape="box",
        style="filled",
        fillcolor="lightgray"
    )
    
    # For each wire (input1, input2, and output), add a node if not already present
    for w in (inp1, inp2, out_wire):
        if w not in wire_nodes_added:
            dot.node(w, label=w, shape="ellipse", color=wire_color(w))
            wire_nodes_added.add(w)
    
    # Draw edges:  input1 -> gate, input2 -> gate, gate -> output
    dot.edge(inp1, gate_name)
    dot.edge(inp2, gate_name)
    dot.edge(gate_name, out_wire)

# Render to a .gv file and also produce a PDF (change format to 'png' if you prefer)
dot.render('logic_circuit.gv', view=True, format='pdf')