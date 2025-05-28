#include <iostream>
#include <cuda.h>
#include <vector>
#include <chrono>

#define CHECK_CUDA_ERR(ans) { gpuAssert((ans), __FILE__, __LINE__); }
inline void gpuAssert(cudaError_t code, const char *file, int line, bool abort=true)
{
    if (code != cudaSuccess) 
    {
        fprintf(stderr,"GPUassert: %s %s %d\n", cudaGetErrorString(code), file, line);
        if (abort) exit(code);
    }
}

__global__ void saxpy(int n, float a, float *x, float *y)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) y[i] = a * x[i] + y[i];
}

void runSAXPY(int N) {
    float *x, *y, *d_x, *d_y;
    float a = 2.0f;

    x = (float*)malloc(N * sizeof(float));
    y = (float*)malloc(N * sizeof(float));
    for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    CHECK_CUDA_ERR(cudaMalloc(&d_x, N * sizeof(float)));
    CHECK_CUDA_ERR(cudaMalloc(&d_y, N * sizeof(float)));

    // Timing events
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    CHECK_CUDA_ERR(cudaMemcpy(d_x, x, N * sizeof(float), cudaMemcpyHostToDevice));
    CHECK_CUDA_ERR(cudaMemcpy(d_y, y, N * sizeof(float), cudaMemcpyHostToDevice));

    cudaEventRecord(start);

    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    saxpy<<<numBlocks, blockSize>>>(N, a, d_x, d_y);

    cudaEventRecord(stop);
    cudaEventSynchronize(stop);

    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);

    std::cout << "N = " << N << ", Time = " << milliseconds << " ms\n";

    cudaFree(d_x);
    cudaFree(d_y);
    free(x);
    free(y);
}

int main() {
    for (int exp = 15; exp <= 25; ++exp) {
        int N = 1 << exp;
        runSAXPY(N);
    }
    return 0;
}
