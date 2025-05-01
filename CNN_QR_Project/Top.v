module top_module #(
    parameter DATA_WIDTH = 16
)(
    input clk,
    input rst,

    input  [DATA_WIDTH-1:0] in00, in01, in02,
    input  [DATA_WIDTH-1:0] in10, in11, in12,
    input  [DATA_WIDTH-1:0] in20, in21, in22,

    input  [DATA_WIDTH-1:0] pool0, pool1,
    input  [DATA_WIDTH-1:0] pool2, pool3,

    input  [DATA_WIDTH-1:0] kernel00, kernel01, kernel02,
    input  [DATA_WIDTH-1:0] kernel10, kernel11, kernel12,
    input  [DATA_WIDTH-1:0] kernel20, kernel21, kernel22,

    output [DATA_WIDTH-1:0] pooled_out
);

    wire [DATA_WIDTH-1:0] conv_out;
    wire [DATA_WIDTH-1:0] relu_out;

    // 2D Convolution block
    conv2d #(
        .DATA_WIDTH(DATA_WIDTH)
    ) conv_layer (
        .in00(in00), .in01(in01), .in02(in02),
        .in10(in10), .in11(in11), .in12(in12),
        .in20(in20), .in21(in21), .in22(in22),
        .kernel00(kernel00), .kernel01(kernel01), .kernel02(kernel02),
        .kernel10(kernel10), .kernel11(kernel11), .kernel12(kernel12),
        .kernel20(kernel20), .kernel21(kernel21), .kernel22(kernel22),
        .out(conv_out)
    );

    // ReLU activation block
    relu #(
        .DATA_WIDTH(DATA_WIDTH)
    ) relu_layer (
        .in(conv_out),
        .out(relu_out)
    );

    // Max Pooling block
    maxpool #(
        .DATA_WIDTH(DATA_WIDTH)
    ) pool_layer (
        .in0(pool0),
        .in1(pool1),
        .in2(pool2),
        .in3(pool3),
        .out(pooled_out)
    );

endmodule

