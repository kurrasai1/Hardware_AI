# Challenge #19 – Binary LIF Neuron

**Course:** ECE 410/510  
**Student:** Megha Sai Sumanth Kurra  
**Instructor:** Prof. Christof Teuscher  
**Date:** Spring 2025

## Objective
Implement a simplified binary Leaky Integrate-and-Fire neuron using Verilog. Simulate and test its response to various input scenarios.

## Design
The LIF neuron maintains a `potential` value which decays over time (`λ leak`) and increases with input spikes. When the threshold is crossed, the neuron spikes and resets.

## Testbench Scenarios
1. Constant zero input
2. Repeated input accumulation
3. Leakage without input
4. Strong input burst

## Tools
- Icarus Verilog for simulation
- GTKWave for waveform viewing

## Results
The neuron:
- Properly accumulated input
- Spiked when reaching threshold
- Reset after spiking
- Leaked as expected with no input

## Key Learning
This hands-on hardware simulation deepened understanding of neuromorphic behavior using basic digital design principles.
