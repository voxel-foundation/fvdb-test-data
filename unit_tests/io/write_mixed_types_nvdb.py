import nanovdb
from nanovdb.math import Coord, CoordBBox, Vec3f

OUT_PATH = "mixed_types.nvdb"

single_voxel_bbox = CoordBBox(Coord(0, 0, 0), Coord(0, 0, 0))

grids = [
    nanovdb.tools.createFloatGrid(
        background=0.0,
        name="density",
        gridClass=nanovdb.GridClass.FogVolume,
        func=lambda ijk: 1.5,
        bbox=single_voxel_bbox,
    ),
    nanovdb.tools.createDoubleGrid(
        background=0.0,
        name="pressure",
        gridClass=nanovdb.GridClass.FogVolume,
        func=lambda ijk: 2.25,
        bbox=single_voxel_bbox,
    ),
    nanovdb.tools.createInt32Grid(
        background=0,
        name="label",
        gridClass=nanovdb.GridClass.Unknown,
        func=lambda ijk: 7,
        bbox=single_voxel_bbox,
    ),
    nanovdb.tools.createVec3fGrid(
        background=Vec3f(0.0, 0.0, 0.0),
        name="velocity",
        gridClass=nanovdb.GridClass.Unknown,
        func=lambda ijk: Vec3f(1.0, 2.0, 3.0),
        bbox=single_voxel_bbox,
    ),
]

nanovdb.io.writeGrids(OUT_PATH, grids, codec=nanovdb.io.Codec.NONE)

print(f"wrote {OUT_PATH}")
for i in range(len(grids)):
    h = nanovdb.io.readGrid(OUT_PATH, i)
    print(f"  [{i}] type={h.gridType()}  size={h.gridSize()}")
