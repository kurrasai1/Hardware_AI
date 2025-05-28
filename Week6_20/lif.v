module lif_neuron #(
    parameter WIDTH = 16,
    parameter LEAK = 16'd32768, // λ = 0.5 in Q1.15 fixed-point
    parameter THRESHOLD = 16'd49152 // θ = 1.5 in Q1.15 fixed-point
)(
    input clk,
    input rst,
    input spike_in,              // I(t): 1-bit binary input
    output reg spike_out         // S(t): neuron spike output
);

    reg [WIDTH-1:0] potential;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            potential <= 0;
            spike_out <= 0;
        end else begin
            // Update potential: P(t) = λ*P(t-1) + I(t)
            potential <= (potential * LEAK >> 15) + (spike_in ? 16'd32768 : 16'd0); // 1.0 input in Q1.15

            // Threshold check
            if (potential >= THRESHOLD) begin
                spike_out <= 1;
                potential <= 0;  // reset on spike
            end else begin
                spike_out <= 0;
            end
        end
    end

endmodule
