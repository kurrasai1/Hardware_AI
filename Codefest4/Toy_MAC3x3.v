module mac3x3 (
    input clk,
    input rst,
    input [7:0] data[0:8],
    input [7:0] weight[0:8],
    output reg [15:0] out
);
    integer i;
    reg [15:0] mac_sum;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            mac_sum <= 0;
        end else begin
            mac_sum = 0;
            for (i = 0; i < 9; i = i + 1) begin
                mac_sum = mac_sum + data[i] * weight[i];
            end
            out <= mac_sum;
        end
    end
endmodule
