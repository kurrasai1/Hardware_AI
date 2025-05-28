import pyNN.brainscales2 as sim

sim.setup()

# Define populations
input_pop = sim.Population(4, sim.SpikeSourceArray(spike_times=[[1.0] for _ in range(4)]))
neuron_pop = sim.Population(2, sim.IF_cond_exp())

# Define matrix as projection weights
weights = [(0, 0, 1.0, 1.0), (1, 0, 1.0, 1.0), (2, 1, 1.0, 1.0), (3, 1, 1.0, 1.0)]
syn = sim.Projection(input_pop, neuron_pop, sim.FromListConnector(weights))

# Run simulation
sim.run(5.0)

print("Neuron outputs:", neuron_pop.get_data().segments[0].spiketrains)

sim.end()
