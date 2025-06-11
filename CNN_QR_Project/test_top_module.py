import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_cnn_accelerator(dut):
    """Test CNN Top Module that includes conv2d + maxpool"""

    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())  # 100MHz Clock

    # Reset
    dut.rst.value = 1
    await Timer(20, units='ns')
    dut.rst.value = 0

    # Provide 3x3 input pixels (e.g., image)
    pixel_vals = [1, 2, 3,
                  4, 5, 6,
                  7, 8, 9]

    kernel_vals = [-1, -1, -1,
                    0,  0,  0,
                    1,  1,  1]

    # Feed image pixels
    for val in pixel_vals:
        dut.pixel_in.value = val
        dut.valid_in.value = 1
        await RisingEdge(dut.clk)

    dut.valid_in.value = 0
    await RisingEdge(dut.clk)

    # Wait for convolution output
    for _ in range(10):
        await RisingEdge(dut.clk)
        if dut.valid_out.value:
            print(f"Convolution result: {dut.conv_out.value.integer}")
            break

    # Pooling test (optional if in top_module)
    print("Cocotb test complete.")
