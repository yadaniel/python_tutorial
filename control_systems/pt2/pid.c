#include <stdint.h>
#include <unistd.h>

const int16_t Kp = 1;
const int16_t Ki = 1;
const int16_t Kd = 1;
const int16_t fs = 1000;   // 1kHz sample rate

uint16_t pid_step(int16_t xset) {
    static int16_t x[64] = {0};
    static int16_t e[64] = {0};
    static uint8_t k = 0;
    static int16_t xs = 0;
    uint16_t xsample = 0;  // from 10bit ADC, range 0x00 ... 0x3FF
    int16_t yout = 0;
    x[k] = xsample;
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
    while(1) {
        pid_step(1);
        sleep(1);
    }
}

