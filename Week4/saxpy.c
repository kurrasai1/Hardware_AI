#include <iostream>
#include <cuda.h>
#include <chrono>

#define CHECK_CUDA(call) \
    if ((call) != cudaSuccess) { \
        std::cerr << "CUDA error at " << __LINE__ << std::endl; exit(1); \
    }

__global__ void saxpy(int n, float a, float *x, float *y) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) y[i] = a * x[i] + y[i];
}

void run_saxpy(int N) {
    float *x, *y, *d_x, *d_y;
    float a = 2.0f;

    x = new float[N];
    y = new float[N];

    for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    CHECK_CUDA(cudaMalloc(&d_x, N * sizeof(float)));
    CHECK_CUDA(cudaMalloc(&d_y, N * sizeof(float)));

    // CUDA events for precise timing
    cudaEvent_t start, stop, kernel_start, kernel_stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);
    cudaEventCreate(&kernel_start);
    cudaEventCreate(&kernel_stop);

    cudaEventRecord(start);
    CHECK_CUDA(cudaMemcpy(d_x, x, N * sizeof(float), cudaMemcpyHostToDevice));
    CHECK_CUDA(cudaMemcpy(d_y, y, N * sizeof(float), cudaMemcpyHostToDevice));

    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;

    cudaEventRecord(kernel_start);
    saxpy<<<numBlocks, blockSize>>>(N, a, d_x, d_y);
    cudaEventRecord(kernel_stop);

    CHECK_CUDA(cudaMemcpy(y, d_y, N * sizeof(float), cudaMemcpyDeviceToHost));
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    cudaEventSynchronize(kernel_stop);

    float total_ms = 0.0f, kernel_ms = 0.0f;
    cudaEventElapsedTime(&total_ms, start, stop);
    cudaEventElapsedTime(&kernel_ms, kernel_start, kernel_stop);

    std::cout << "N = " << N
              << ", Total time (ms) = " << total_ms
              << ", Kernel time (ms) = " << kernel_ms << std::endl;

    delete[] x;
    delete[] y;
    cudaFree(d_x);
    cudaFree(d_y);
}

