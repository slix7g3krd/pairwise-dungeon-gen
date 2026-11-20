import math

def room_overlap(a, b):
    """房间包围盒相交。"""
    raise NotImplementedError("TODO: room_overlap")

def corridor_cells(a, b):
    """走廊格数。"""
    raise NotImplementedError("TODO: corridor_cells")

def rng_seed(base, room_id):
    """房间独立种子。"""
    raise NotImplementedError("TODO: rng_seed")

def connectivity(parents):
    """连通分量。"""
    raise NotImplementedError("TODO: connectivity")

def key_before_door(key_room, door_room):
    """钥匙门拓扑。"""
    raise NotImplementedError("TODO: key_before_door")

def depth_difficulty(depth, base):
    """可达深度难度。"""
    raise NotImplementedError("TODO: depth_difficulty")

def navmesh_door_cells(width, height):
    """门洞 navmesh。"""
    raise NotImplementedError("TODO: navmesh_door_cells")

def stair_pair(floor_a, floor_b):
    """楼梯双向。"""
    raise NotImplementedError("TODO: stair_pair")

def generation_done(progress):
    """生成完成。"""
    raise NotImplementedError("TODO: generation_done")

def layout_digest(seed, rooms):
    """布局摘要。"""
    raise NotImplementedError("TODO: layout_digest")

def dead_end_keep(dead_end, critical):
    """死路保护。"""
    raise NotImplementedError("TODO: dead_end_keep")

def room_bounds(center, size, rotation):
    """旋转房包围盒。"""
    raise NotImplementedError("TODO: room_bounds")

def grid_index(x, y, width):
    """网格索引。"""
    raise NotImplementedError("TODO: grid_index")

def step_limit(distance, step):
    """步数上限。"""
    raise NotImplementedError("TODO: step_limit")

def seed_key(seed, version):
    """存档种子键。"""
    raise NotImplementedError("TODO: seed_key")
