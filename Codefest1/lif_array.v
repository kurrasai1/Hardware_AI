module lif_array #(parameter N=4)(
    input clk, reset,
    input [7:0] input_current [N-1:0],
    output reg spike [N-1:0]
);
    reg [7:0] v [N-1:0];
    parameter THRESH = 100;

    integer i;
    always @(posedge clk) begin
        if (reset) begin
            for (i = 0; i < N; i = i + 1)
                v[i] <= 0;
        end else begin
            for (i = 0; i < N; i = i + 1) begin
                v[i] <= v[i] + input_current[i] - 1; // leak = 1
                if (v[i] >= THRESH) begin
                    spike[i] <= 1;
                    v[i] <= 0;
                end else
                    spike[i] <= 0;
            end
        end
    end
endmodule
