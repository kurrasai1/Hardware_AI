module conv2d #(
    parameter DATA_WIDTH = 8,
    parameter KERNEL_WIDTH = 8
)(
    input clk,
    input rst,
    input valid_in,
    input [DATA_WIDTH-1:0] pixel_in,
    output reg valid_out,
    output reg [DATA_WIDTH+KERNEL_WIDTH+3:0] conv_out  // extra bits to prevent overflow
);

    // Line buffer to store 3x3 pixels
    reg [DATA_WIDTH-1:0] window[0:8];  // 3x3 = 9 pixels
    integer i;

    // Predefined 3x3 kernel weights (signed)
    reg signed [KERNEL_WIDTH-1:0] kernel[0:8];
    initial begin
        // Example: Sobel X
        kernel[0] = -1; kernel[1] = 0; kernel[2] = 1;
        kernel[3] = -2; kernel[4] = 0; kernel[5] = 2;
        kernel[6] = -1; kernel[7] = 0; kernel[8] = 1;
    end

    // Shift window and insert new pixel
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            for (i = 0; i < 9; i = i + 1)
                window[i] <= 0;
            valid_out <= 0;
            conv_out <= 0;
        end else if (valid_in) begin
            // Shift left all pixels
            for (i = 8; i > 0; i = i - 1)
                window[i] <= window[i-1];
            window[0] <= pixel_in;

            // Only compute output once window is full
            if (&window[8:0]) begin
                conv_out <=
                    $signed(window[0]) * kernel[0] +
                    $signed(window[1]) * kernel[1] +
                    $signed(window[2]) * kernel[2] +
                    $signed(window[3]) * kernel[3] +
                    $signed(window[4]) * kernel[4] +
                    $signed(window[5]) * kernel[5] +
                    $signed(window[6]) * kernel[6] +
                    $signed(window[7]) * kernel[7] +
                    $signed(window[8]) * kernel[8];
                valid_out <= 1;
            end else begin
                conv_out <= 0;
                valid_out <= 0;
            end
        end else begin
            valid_out <= 0;
        end
    end

endmodule

