module maxpool #(
    parameter DATA_WIDTH = 16
)(
    input  [DATA_WIDTH-1:0] in0,  // top-left
    input  [DATA_WIDTH-1:0] in1,  // top-right
    input  [DATA_WIDTH-1:0] in2,  // bottom-left
    input  [DATA_WIDTH-1:0] in3,  // bottom-right
    output [DATA_WIDTH-1:0] out   // max of in0 to in3
);

    wire [DATA_WIDTH-1:0] max0;
    wire [DATA_WIDTH-1:0] max1;

    assign max0 = (in0 > in1) ? in0 : in1;
    assign max1 = (in2 > in3) ? in2 : in3;
    assign out  = (max0 > max1) ? max0 : max1;

endmodule

