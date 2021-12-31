#include <msp432p401r.h>

int main(void) {
    // disable watchdog
    WDT_A->CTL = WDT_A_CTL_PW | WDT_A_CTL_HOLD;

    P1DIR |= BIT0;  // P1_0

    volatile int i;
    while(1){
        for (i = 0; i < 100000; i++);  // Delay
        P1OUT ^= BIT0;  // toggle the LED
    }

    return 0;
}