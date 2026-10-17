---
title: Component Selection
---
**H-Bridge Motor Driver**

1. Pololu DRV8874 single brushed DC motor driver carrier

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/38b76673-50e1-4af0-a5eb-e566417c6706" />

    * $11.94/each
    * [link to product](https://www.pololu.com/product/4035)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | PH/EN mode controls speed and direction with one PWM pin plus one GPIO, which matches our pin map. | Most expensive of the three drivers. |
    | Integrated current sensing and regulation (IPROPI, VREF) limits motor current without an external shunt resistor. | Needs PMODE and nSLEEP wired, which adds two connections compared with a two-input driver. |
    | Undervoltage, overcurrent and thermal protection, plus an nFAULT output the firmware can read. |
    | Includes 0.1" breakaway headers, so it can be hand soldered and tested on a breadboard. |

2. Adafruit DRV8871 DC motor driver breakout

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/9b804e04-1f90-4262-ad4d-f8481fda9566" />


    * $7.50/each
    * [Link to product](https://www.adafruit.com/product/3190)

    | Pros                                                              | Cons                |
    | ----------------------------------------------------------------- | ------------------- |
    | Lower price                                             | Changing the current limit means swapping a resistor, not changing a reference voltage.      |
    | Current limit set by a resistor, so the motor is protected without firmware. | No current-sense output for the firmware to read |
    | Simple two-input interface and well documented by Adafruit. |

3. TB6612FNG Dual Motor Driver Carrier

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/cc13847f-4e7c-4454-8a69-3a6c4c355763" />


    * $4.95/each
    * [Link to product](https://www.pololu.com/product/713)

    | Pros                                                              | Cons                |
    | ----------------------------------------------------------------- | ------------------- |
    | Lowest price                                            | No current sensing or regulation.      |
    | Two channels, so the second channel could be paralleled for 2 A continuous or kept as a spare. | Three control inputs per channel plus a shared STBY pin, it uses more GPIO than our pin map |
    | 3 A peak current and PWM frequencies up to 100 kHz. |
   <br>
**Choice:** Option 1: Pololu DRV8874 single brushed DC motor driver carrier

**Rationale:** The PH/EN interface is the only one of the three that matches the pin map already shared with the team (one PWM pin and one direction pin), so no firmware or wiring changes are needed. Its 37 V range leaves a large margin on the 12 V rail, while the TB6612FNG is near its 13.5 V limit. Built-in current regulation matters here because the selected motor can draw a much higher stall current (about 5 A, extrapolated) than the carrier's continuous rating, so a driver that can limit current in hardware protects both the motor and the supply. The extra $4.44 over the DRV8871 buys these features.

**DC Motor**
<br>
1. 34:1 Metal Gearmotor 25Dx67L mm HP 12V with 48 CPR Encoder

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/ffc5b4e5-fdd3-4698-b380-6c9480c22d9c" />

    * $56.95/each
    * [link to product](https://www.pololu.com/product/4844)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | 11 kg·cm (150 oz·in) stall torque at 300 rpm no-load speed gives the most torque margin | Most expensive option |
    | Built-in two-channel Hall-effect quadrature encoder | Stall current is 5.0 A, above the driver's continuous rating |
    | Datasheet and dimension drawing are available for the mechanical design | Adds mass to the arm; the weight is not listed on the page and must be checked |
    | 4 mm D-shaft output. | The encoder needs a 3.5 V to 20 V supply and its outputs swing from 0 V to Vcc|




