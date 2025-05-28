module tb_lif_neuron();

    reg clk = 0;
    reg rst;
    reg spike_in;
    wire spike_out;

    lif_neuron uut (
        .clk(clk),
        .rst(rst),
        .spike_in(spike_in),
        .spike_out(spike_out)
    );

    always #5 clk = ~clk;

    initial begin
        $dumpfile("lif_neuron.vcd");
        $dumpvars(0, tb_lif_neuron);
        
        rst = 1; spike_in = 0;
        #10 rst = 0;

        // Case 1: Constant input below threshold
        #50 spike_in = 0;
        #50;

        // Case 2: Repeated input causes spike after accumulation
        spike_in = 1;
        repeat (10) #10;
        
        // Case 3: No input, leak causes decay
        spike_in = 0;
        repeat (10) #10;

        // Case 4: Strong input causes immediate spike
        spike_in = 1;
        repeat (2) #10;

        $finish;
    end

endmodule
