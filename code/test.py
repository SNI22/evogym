import os
from evogym import EvoWorld, EvoSim, EvoViewer, sample_robot, get_full_connectivity
import numpy as np

world = EvoWorld.from_json(os.path.join("world_data", "simple_environment.json"))
# robot_structure, robot_connections = sample_robot((5, 5))
robot_structure = np.array(
[[0, 0, 4, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 3, 0, 0],
 [0, 1, 1, 1, 0],
 [0, 0, 0, 0, 0]]
)

robot_connections = get_full_connectivity(robot_structure)

print(robot_structure)
print(robot_connections)
world.add_from_array(
    name="robot", structure=robot_structure, x=3, y=2, connections=robot_connections
)

world.pretty_print()
sim = EvoSim(world)
sim.reset()
viewer = EvoViewer(sim)
viewer.track_objects("robot",'box')
for i in range(500):
    sim.set_action(
        "robot",
        np.random.uniform(low=0.6, high=1.6, size=(sim.get_dim_action_space("robot"),)),
    )
    sim.step()
    viewer.render("screen")
