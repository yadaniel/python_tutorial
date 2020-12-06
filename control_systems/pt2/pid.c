#include <stdio.h>
#include <stdint.h>
#include <unistd.h>
#include <time.h>

// Ts = sample interval
// yout[0] = Kp*e[0] + Ki/(N*Ts) sum (k=-N+1 to 0) {e[k]*Ts} + Kd*(e[0]-e[-1])/Ts
//
// Ki/(N*Ts) sum (k=-N+1 to 0) {e[k]*Ts} = Ki/N sum (k=-N+1 to 0) {e[k]} = Ki * average {e[-N+1] ... e[0]}
//
// when Ts' = 0.1*Ts then pid_step() called 10 times so often
// Kp*e[0] will contribute 10 times to yout
// Ki*average { e[-N+1] ... e[0] } will contribute ~10 times to yout ... assuming linear e[k] less error in the integral approximation
// Kd*(e[0]-e[-1])/Ts will contribute 10 times to yout ... assuming linear e[k]
// yout' = yout/10

const int16_t Kp = 1;
const int16_t Ki = 1;
const int16_t Kd = 1;
const int16_t fs = 1000;   // 1kHz sample rate

// xset [0..100]
// xnew [0..100]
uint16_t pid_step(int16_t xset, int16_t xnew) {
    static int16_t x[64] = {0};
    static int16_t e[64] = {0};
    static int16_t xs = 0;
    static uint8_t k = 0;
    int16_t yout = 0;

    x[k] = xnew;
    e[k] = xset - x[k];
    //
    xs += Ki*e[k];
    yout = Kp*e[k] + xs + Kd*(e[k] - e[(k-1) & 63])*fs;
    if (yout > 0x03FF) {    // 10bit DAC
        yout = 0x03FF;      // yout = min(yout, 2**10)
    }
    if (yout < 0x00) {
        yout = 0;           // yout = max(yout, 0)
    }
    k = (k+1) & 63;         // 0x00 ... 0x3F
    return yout;            // write to DAC
}

int main(void) {
    struct timespec t;
    uint16_t yout;
    while(1) {
        clock_gettime(CLOCK_REALTIME, &t);
        printf("%lu:[+%.04f]:%09lu:", t.tv_sec, t.tv_nsec/1e9, t.tv_nsec);
        //
        yout = pid_step(1, 0);
        printf("%i\n", yout);
        //
        /* usleep(100);        // 100us */
        /* usleep(1000);       // 1000us = 1ms */
        usleep(10000);      // 10_000us = 10ms
        /* usleep(100000);     // 100_000us = 100ms */
        /* usleep(1000000);    // 1000_000us = 1000ms */
    }
}

