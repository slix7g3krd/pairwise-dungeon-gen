import pytest
from gameplay import dungeon_generation as mod

CASES = [
    ("overlap", 'm.room_overlap((0, 0, 2, 2), (1, 1, 2, 2)) is True'),
    ("corridor", 'm.corridor_cells((0, 0), (2, 0)) == 3'),
    ("seed", 'm.rng_seed(10, 2) == 1002'),
    ("connect", 'm.connectivity([0, 0, 1, 2]) == 2'),
    ("key", 'm.key_before_door(1, 2) is True'),
    ("difficulty", 'm.depth_difficulty(3, 1) == 4'),
    ("navmesh", 'm.navmesh_door_cells(2, 3) == 6'),
    ("stair", 'm.stair_pair(3, 1) == (1, 3)'),
    ("done", 'm.generation_done(1.0) is True'),
    ("digest", 'm.layout_digest(7, 5) == "7:5"'),
    ("deadend", 'm.dead_end_keep(True, False) is True'),
    ("bounds", 'm.room_bounds((0, 0), (4, 2), 90) == (4, 2)'),
    ("grid", 'm.grid_index(3, 4, 8) == 35'),
    ("steps", 'm.step_limit(10, 3) == 4'),
    ("seedkey", 'm.seed_key(7, 2) == "7:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
