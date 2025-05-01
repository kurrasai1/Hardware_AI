module relu_sync #(
    parameter DATA_WIDTH = 16
)(
    input  clk,
    input  rst,
    input  valid_in,
    input  signed [DATA_WIDTH-1:0] data_in,
    output reg signed [DATA_WIDTH-1:0] data_out,
    output reg valid_out
);

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            data_out  <= 0;
            valid_out <= 0;
        end else if (valid_in) begin
            data_out  <= (data_in < 0) ? 0 : data_in;
            valid_out <= 1;
        end else begin
            valid_out <= 0;
        end
    end

endmodule
