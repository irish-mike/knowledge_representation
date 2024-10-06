from pathfinder_synth.synth_agents import agent_factory
from pathfinder_synth.synth_enviornment import SynthEnvironment
from pathfinder_synth.synth_graphs import graph_factory

def run(graph_type, agent, steps=20):
    print(f"\nRunning {agent.__name__} on {graph_type.replace('_', ' ').title()}")
    graph = graph_factory(graph_type)
    env = SynthEnvironment(graph)
    env.add_thing(agent)
    env.run(steps)

# Run Reflex Agent
run('ideal_path', agent_factory('Reflex'))
run('wrong_path', agent_factory('Reflex'))
run('dead_end', agent_factory('Reflex'))

# Run Model based Agent
run('ideal_path', agent_factory('Model'))
run('wrong_path', agent_factory('Model'))
run('dead_end', agent_factory('Model'))

# Run Utility based Agent
run('ideal_path', agent_factory('Utility'))
run('wrong_path', agent_factory('Utility'))
run('dead_end', agent_factory('Utility'))