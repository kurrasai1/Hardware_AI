module lif_neuron (
    input wire clk,
    input wire reset,
    input wire [7:0] input_current, // synaptic input
    output reg spike
);

  parameter THRESHOLD = 100;
  parameter LEAK = 1;

  reg [7:0] potential;

  always @(posedge clk or posedge reset) begin
    if (reset) begin
      potential <= 0;
      spike <= 0;
    end else begin
      potential <= potential + input_current - LEAK;
      if (potential >= THRESHOLD) begin
        spike <= 1;
        potential <= 0; // reset after spike
      end else begin
        spike <= 0;
      end
    end
  end

endmodule

