import vpython as vp
import numpy as np
import urllib.request
import urllib.parse
import time  # ✅ NEW

# --- Configuration ---
COLORS = {'H': vp.color.white, 'C': vp.color.gray(0.4), 'O': vp.color.red, 
          'N': vp.color.blue, 'S': vp.color.yellow, 'P': vp.color.orange, 'Cl': vp.color.green}

RADII = {'H': 0.3, 'C': 0.6, 'O': 0.5, 'N': 0.55, 'S': 0.7, 'P': 0.7, 'Cl': 0.65}

ATOMIC_WEIGHTS = {
    'H': 1.008, 'C': 12.01, 'O': 16.00, 'N': 14.01,
    'S': 32.06, 'P': 30.97, 'Cl': 35.45
}

# --- Classes ---
class Atom:
    def __init__(self, symbol, x, y, z):
        self.symbol = symbol
        self.base_pos = np.array([x, y, z], dtype=float)
        self.current_pos = np.copy(self.base_pos)
        
        self.mesh = vp.sphere(
            pos=vp.vector(x, y, z),
            radius=RADII.get(symbol, 0.5),
            color=COLORS.get(symbol, vp.color.magenta)
        )

    def update_position(self, new_pos):
        self.current_pos = new_pos
        self.mesh.pos = vp.vector(*new_pos)

    def destroy(self):
        self.mesh.visible = False

class Bond:
    def __init__(self, atom1, atom2):
        self.atom1 = atom1
        self.atom2 = atom2
        self.mesh = vp.cylinder(
            pos=atom1.mesh.pos,
            axis=atom2.mesh.pos - atom1.mesh.pos,
            radius=0.15,
            color=vp.color.gray(0.7)
        )

    def update_visuals(self):
        self.mesh.pos = self.atom1.mesh.pos
        self.mesh.axis = self.atom2.mesh.pos - self.atom1.mesh.pos

    def length(self):
        return np.linalg.norm(self.atom1.current_pos - self.atom2.current_pos)

    def destroy(self):
        self.mesh.visible = False

class MoleculeViewer:
    def __init__(self):
        self.atoms = []
        self.bonds = []
        self.center_of_mass = np.zeros(3)
        self.is_simulating = False
        self.time_elapsed = 0.0

    def clear_current_molecule(self):
        for a in self.atoms: a.destroy()
        for b in self.bonds: b.destroy()
        self.atoms.clear()
        self.bonds.clear()

    def load_from_xyz(self, xyz_data):
        self.clear_current_molecule()
        lines = xyz_data.strip().split('\n')
        if len(lines) < 3: return
        
        positions = []
        for line in lines[2:]:
            parts = line.split()
            if len(parts) == 4:
                s, x, y, z = parts
                x, y, z = float(x), float(y), float(z)
                self.atoms.append(Atom(s, x, y, z))
                positions.append([x, y, z])

        self.center_of_mass = np.mean(positions, axis=0)
        self._auto_detect_bonds()

    def _auto_detect_bonds(self, threshold=1.6):
        for i in range(len(self.atoms)):
            for j in range(i+1, len(self.atoms)):
                if np.linalg.norm(self.atoms[i].base_pos - self.atoms[j].base_pos) < threshold:
                    self.bonds.append(Bond(self.atoms[i], self.atoms[j]))

    def simulate_step(self, dt):
        if not self.is_simulating: return
        self.time_elapsed += dt
        
        for atom in self.atoms:
            direction = atom.base_pos - self.center_of_mass
            if np.linalg.norm(direction) > 0:
                direction /= np.linalg.norm(direction)
            displacement = direction * np.sin(self.time_elapsed*10)*0.05
            atom.update_position(atom.base_pos + displacement)

        for bond in self.bonds:
            bond.update_visuals()

# --- INFO PANEL ---
def update_info_panel(viewer, name="Unknown"):
    if not viewer.atoms:
        info_panel.text = "No Data"
        return

    counts = {}
    total_weight = 0
    for a in viewer.atoms:
        counts[a.symbol] = counts.get(a.symbol, 0) + 1
        total_weight += ATOMIC_WEIGHTS.get(a.symbol, 0)

    formula = "".join([f"{k}{v if v>1 else ''}" for k,v in sorted(counts.items())])

    info_panel.text = f"""

<b>MOLECULE DASHBOARD</b>

Name: {name}
Formula: {formula}

Atoms: {len(viewer.atoms)}
Bonds: {len(viewer.bonds)}

Unique Elements: {len(counts)}
Composition: {counts}

Molecular Weight: {round(total_weight,2)} u

Dominant Element: {max(counts, key=counts.get)}
Element Types: {list(counts.keys())}
"""

# --- DOUBLE CLICK LOGIC (NEW) ---
last_click_time = 0
selected_label = None

def handle_mouse_click(evt):
    global last_click_time, selected_label

    current_time = time.time()
    dt = current_time - last_click_time

    if dt < 0.3:  # double click threshold
        picked = scene.mouse.pick

        if picked is not None:
            for atom in viewer.atoms:
                if picked is atom.mesh:
                    
                    # remove old label
                    if selected_label:
                        selected_label.visible = False
                    
                    pos = atom.mesh.pos
                    
                    selected_label = vp.label(
                        pos=pos,
                        text=f"{atom.symbol}",
                        xoffset=20,
                        yoffset=20,
                        height=12,
                        border=4
                    )

                    break

    last_click_time = current_time

# --- Fetch ---
def fetch_from_pubchem(name):
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{urllib.parse.quote(name)}/SDF?record_type=3d"
        data = urllib.request.urlopen(url).read().decode()
        lines = data.split('\n')
        
        count = int(lines[3][0:3])
        xyz = f"{count}\n{name}\n"
        
        for i in range(4, 4+count):
            p = lines[i].split()
            xyz += f"{p[3]} {p[0]} {p[1]} {p[2]}\n"
        
        return xyz
    except:
        return "ERROR"

# --- UI ---
scene = vp.canvas(title="Molecular Visualizer Pro", width=1040, height=450)
scene.bind('click', handle_mouse_click)  # ✅ bind event

viewer = MoleculeViewer()

# 🔹 SEARCH
vp.wtext(text="\n🔍 Search Molecule: ")
status = vp.wtext(text=" Ready\n\n")

def search(box):
    q = box.text
    status.text = f" Searching {q}...\n"
    data = fetch_from_pubchem(q)
    
    if "ERROR" not in data:
        viewer.load_from_xyz(data)
        update_info_panel(viewer, q)
        status.text = f" Loaded {q}\n"
    else:
        status.text = " Error loading molecule\n"

vp.winput(bind=search)

# 🔹 BUTTON
def toggle(btn):
    viewer.is_simulating = not viewer.is_simulating
    btn.text = "Pause" if viewer.is_simulating else "Vibrate"
    update_info_panel(viewer)

vp.button(text="Vibrate", bind=toggle)

# 🔹 INFO PANEL
info_panel = vp.wtext(text="\n\nLoading...\n")

# Initial Load
data = fetch_from_pubchem("water")
viewer.load_from_xyz(data)
update_info_panel(viewer, "Water")

# Loop
while True:
    vp.rate(60)
    viewer.simulate_step(0.016)