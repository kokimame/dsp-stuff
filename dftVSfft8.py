"""
Primitive implementation of FFT for 8 data (specifically)
"""


from math import exp, pi, cos, sin

N = 8
x = [1,1,-1,-1,1,1,-1,-1] # Signal in time domain
assert len(x) == N

def dft(x):
    X = [0] * N  # Signal in frequency domain
    for k in range(N):
        X[k] = sum([x[n]*(cos(2*pi*k*n/N) - 1j*sin(2*pi*k*n/N)) for n in range(N)])
    return X

def fft8(x):
    X = [0] * N  # Signal in frequency domain
    W8 = cos(2*pi/8) - 1j*sin(2*pi/8)

    s1 = [0] * N
    # STAGE 1
    s1[0] += x[0] + x[4]
    s1[1] += x[0] - x[4]
    s1[2] += x[2] + x[6]
    s1[3] += x[2] - x[6]
    s1[4] += x[1] + x[5]
    s1[5] += x[1] - x[5]
    s1[6] += x[3] + x[7]
    s1[6] += x[3] - x[7]

    s2 = [0] * N
    # STAGE 2
    s2[0] += s1[0] + W8**0 * s1[2]
    s2[2] += s1[0] - W8**0 * s1[2]
    s2[1] += s1[1] + W8**2 * s1[3]
    s2[3] += s1[1] - W8**2 * s1[3]
    s2[4] += s1[4] + W8**0 * s1[6]
    s2[6] += s1[4] - W8**0 * s1[6]
    s2[5] += s1[5] + W8**2 * s1[7]
    s2[7] += s1[5] - W8**2 * s1[7]

    # STAGE 3
    X[0] += s2[0] + W8**0 * s2[4]
    X[4] += s2[0] - W8**0 * s2[4]
    X[1] += s2[1] + W8**1 * s2[5]
    X[5] += s2[1] - W8**1 * s2[5]
    X[2] += s2[2] + W8**2 * s2[6]
    X[6] += s2[2] - W8**2 * s2[6]
    X[3] += s2[3] + W8**3 * s2[7]
    X[7] += s2[3] - W8**3 * s2[7]
    return X

print("FFT: ", [abs(X) for X in fft8(x)])
print("DFT: ", [abs(X) for X in dft(x)])



