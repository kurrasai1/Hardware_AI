module tb_mac3x3;
    reg clk = 0;
    reg rst;
    reg [7:0] data[0:8];
    reg [7:0] weight[0:8];
    wire [15:0] out;

    mac3x3 uut(.clk(clk), .rst(rst), .data(data), .weight(weight), .out(out));

    always #5 clk = ~clk;

    initial begin
        rst = 1; #10;
        rst = 0;

        data[0] = 1; data[1] = 2; data[2] = 3;
        data[3] = 4; data[4] = 5; data[5] = 6;
        data[6] = 7; data[7] = 8; data[8] = 9;

        weight[0] = 1; weight[1] = 0; weight[2] = -1;
        weight[3] = 1; weight[4] = 0; weight[5] = -1;
        weight[6] = 1; weight[7] = 0; weight[8] = -1;

        #20;
        $display("MAC Output = %d", out);
        $finish;
    end
endmodule
