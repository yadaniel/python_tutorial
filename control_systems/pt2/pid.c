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

// PID controller design techniques
// zigler nichols method 1: use step response, find Kp critical and readout Tp => use table for Kp,Ki,Kd parameters
// zigler nichols method 2: use step response, find turn tangent in response, readout Tdel and a => use table for Kp,Ki,Kd parameters
// zigler nichols method 2a: use step response and wait until steady state, find DC-gain K, scale down to 0.63K and find out T63
// pole placement
// root locus

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

    // <debug>

    // e[k]
    printf("\ne[64]={");
    for(int i=0; i<64; i++) {
        printf("%i,", e[i]);
    }
    printf("}\n");

    // x[k]
    printf("x[64]={");
    for(int i=0; i<64; i++) {
        printf("%i,", x[i]);
    }
    printf("}\n");

    // xs
    printf("xs=%i\n", xs);

    // </debug>

    x[k] = xnew;
    e[k] = xset - x[k];
    //
    xs += Ki*e[k];
    /* yout = Kp*e[k] + xs + Kd*(e[k] - e[(k-1) & 63])*fs; */
    yout = Kp*e[k] + xs;
    if (yout > 0x03FF) {    // 10bit DAC
        yout = 0x03FF;      // yout = min(yout, 2**10)
    }
    if (yout < 0x00) {
        yout = 0;           // yout = max(yout, 0)
    }
    k = (k+1) & 63;         // 0x00 ... 0x3F
    return yout;            // write to DAC
}

// nanosleep
void test(void) {
    struct timespec t0, t1;
    t0.tv_sec = 3;
    t0.tv_nsec = 500000000;
    if(nanosleep(&t0, &t1) < 0) {
        printf("1 ");
    } else {
        printf("2 ");
    }
    printf("%lu:[+%0.4f]\n", t1.tv_sec, t1.tv_nsec);
}

int main(void) {
    struct timespec t;
    uint16_t yout;
    /* test(); */
    /* return 1; */
    while(1) {
        clock_gettime(CLOCK_REALTIME, &t);
        printf("%lu:[+%.04f]:%09lu:", t.tv_sec, t.tv_nsec/1e9, t.tv_nsec);
        //
        yout = pid_step(6, 1);
        printf("%i\n", yout);
        //
        /* usleep(100);        // 100us */
        /* usleep(1000);       // 1000us = 1ms */
        /* usleep(10000);      // 10_000us = 10ms */
        usleep(100000);     // 100_000us = 100ms
        /* usleep(1000000);    // 1000_000us = 1000ms */
    }
}

