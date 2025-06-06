module tb;
    reg clk = 0, reset = 0;
    reg [7:0] input_current [3:0];
    wire [3:0] spike;

    lif_array #(4) lif(.clk(clk), .reset(reset), .input_current(input_current), .spike(spike));

    always #5 clk = ~clk;

    initial begin
        reset = 1; #10;
        reset = 0;
        input_current[0] = 20; input_current[1] = 25;
        input_current[2] = 30; input_current[3] = 40;
        #200 $finish;
    end
endmodule
