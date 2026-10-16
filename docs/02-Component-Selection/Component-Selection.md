---
title: Component Selection Example
---
**H-Bridge Motor Driver**

1. Pololu DRV8874 single brushed DC motor driver carrier

    ![](image1.png)

    * $11.94/each
    * [link to product](https://www.pololu.com/product/4035)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | PH/EN mode controls speed and direction with one PWM pin plus one GPIO, which matches our pin map. | Most expensive of the three drivers. |
    | Integrated current sensing and regulation (IPROPI, VREF) limits motor current without an external shunt resistor. | Needs PMODE and nSLEEP wired, which adds two connections compared with a two-input driver. |
    | Undervoltage, overcurrent and thermal protection, plus an nFAULT output the firmware can read. |
    | Includes 0.1" breakaway headers, so it can be hand soldered and tested on a breadboard. |

1. CTX936TR-ND surface mount oscillator

    ![](image3.png)

    * $1/each
    * [Link to product](http://www.digikey.com/product-detail/en/636L3I001M84320/CTX936TR-ND/2292940)

    | Pros                                                              | Cons                |
    | ----------------------------------------------------------------- | ------------------- |
    | Outputs a square wave                                             | More expensive      |
    | Stable over operating temperature                                 | Slow shipping speed |
    | Direct interface with PSoC (no external circuitry required) range |

**Choice:** Option 2: CTX936TR-ND surface mount oscillator

**Rationale:** A clock oscillator is easier to work with because it requires no external circuitry in order to interface with the PSoC. This is particularly important because we are not sure of the electrical characteristics of the PCB, which could affect the oscillation of a crystal. While the shipping speed is slow, according to the website if we order this week it will arrive within 3 weeks.
