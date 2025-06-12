`timescale 1ns / 1ps

module test_cnn_top_tb;

    parameter DATA_WIDTH = 16;

    // Inputs to top_module
    reg clk, rst;
    reg  [DATA_WIDTH-1:0] in00, in01, in02;
    reg  [DATA_WIDTH-1:0] in10, in11, in12;
    reg  [DATA_WIDTH-1:0] in20, in21, in22;

    reg  [DATA_WIDTH-1:0] kernel00, kernel01, kernel02;
    reg  [DATA_WIDTH-1:0] kernel10, kernel11, kernel12;
    reg  [DATA_WIDTH-1:0] kernel20, kernel21, kernel22;

    reg  [DATA_WIDTH-1:0] pool0, pool1, pool2, pool3;

    // Output from top_module
    wire [DATA_WIDTH-1:0] pooled_out;

    // Instantiate the top_module
    top_module #(
        .DATA_WIDTH(DATA_WIDTH)
    ) uut (
        .clk(clk),
        .rst(rst),
        .in00(in00), .in01(in01), .in02(in02),
        .in10(in10), .in11(in11), .in12(in12),
        .in20(in20), .in21(in21), .in22(in22),
        .kernel00(kernel00), .kernel01(kernel01), .kernel02(kernel02),
        .kernel10(kernel10), .kernel11(kernel11), .kernel12(kernel12),
        .kernel20(kernel20), .kernel21(kernel21), .kernel22(kernel22),
        .pool0(pool0), .pool1(pool1),
        .pool2(pool2), .pool3(pool3),
        .pooled_out(pooled_out)
    );

    // Clock generation
    always #5 clk = ~clk;

    initial begin
        $display("Starting CNN Accelerator TB");
        $dumpfile("cnn_top_tb.vcd");
        $dumpvars(0, test_cnn_top_tb);

        clk = 0;
        rst = 1;

        // Initial delay for reset
        #10;
        rst = 0;

        // Input image (3x3) sample values
        in00 = 1;  in01 = 2;  in02 = 3;
        in10 = 4;  in11 = 5;  in12 = 6;
        in20 = 7;  in21 = 8;  in22 = 9;

        // Kernel (3x3) sample values (e.g., edge detection)
        kernel00 = -1; kernel01 = -1; kernel02 = -1;
        kernel10 =  0; kernel11 =  0; kernel12 =  0;
        kernel20 =  1; kernel21 =  1; kernel22 =  1;

        // Pooling inputs (ReLU output window)
        pool0 = 5; pool1 = 8;
        pool2 = 2; pool3 = 4;

        #20;

        $display("The Final Pooled Output = %0d", pooled_out);

        #10;
        $finish;
    end

endmodule

