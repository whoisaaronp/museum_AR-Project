# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'project/gltf_to_glb'))
    print(os.getcwd())
except:
    pass

# %%
from pygltflib import GLTF2
from pygltflib.utils import glb2gltf, gltf2glb
from pygltflib import GLTF2, Scene
from pygltflib.utils import glb2gltf, gltf2glb


gltf = GLTF2()

# %%
filename = "/project/gltf_to_glb/files/coffecup.gltf"
gltf = GLTF2().load(filename)

# %%
# convert glb to gltf
gltf2glb("/project/gltf_to_glb/files/coffecup.gltf")

# %%
