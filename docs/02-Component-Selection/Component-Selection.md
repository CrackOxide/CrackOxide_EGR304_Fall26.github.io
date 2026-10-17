---
title: Component Selection
---
## H-Bridge Motor Driver

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

## DC Motor

1. 34:1 Metal Gearmotor 25Dx67L mm HP 12V with 48 CPR Encoder

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/ffc5b4e5-fdd3-4698-b380-6c9480c22d9c" />

    * $56.95/each
    * [link to product](https://www.pololu.com/product/4844)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | 11 kg·cm stall torque at 300 rpm no-load speed gives the most torque margin | Most expensive option |
    | Built-in two-channel Hall-effect quadrature encoder | Stall current is 5.0 A, above the driver's continuous rating |
    | Datasheet and dimension drawing are available for the mechanical design | Adds mass to the arm; the weight is not listed on the page and must be checked |
    | 4 mm D-shaft output. | The encoder needs a 3.5 V to 20 V supply and its outputs swing from 0 V to Vcc|

2. Pololu 250:1 Micro Metal Gearmotor MP 6V

    <img width="300" height="240" alt="image" src="https://github.com/user-attachments/assets/ff4376af-aee2-475e-b04b-c97b52344fd0" />

    * $23.95/each
    * [link to product](https://www.pololu.com/product/2370)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Very compact with metal gears, saves arm weight. | Stall torque is only 1.6 kg·cm, about one seventh of Option 1 |
    | Low stall current fits any of the three drivers. | Manufactor warns that stalling can damage the motor or gearbox |
    | The extended motor shaft allows a magnetic encoder to be added later. | No encoder included |
    | Datasheet available |

3. Adafruit DC gearbox "TT" motor, 200 rpm, 3 to 6 VDC

    <img width="320" height="243" alt="image" src="https://github.com/user-attachments/assets/7608b7b7-4eaf-4c45-afb4-52e9af9ec26d" />

    * $2.95/each
    * [link to product](https://www.adafruit.com/product/3777)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Lowest price | Stall torque is only 0.8 kg·cm at 6 V, too low for a loaded arm joint. |
    | Light with a 1:48 gearbox and 200 mm leads ending in 0.1" connectors. | Rated 3 V to 6 V, needs a separate lower-voltage rail. |
    | TLow current (1.5 A stall at 6 V).| No encoder included |The product sheet is only a basic specification sheet and there is no full datasheet, which the assignment warns against |
    <br>
**Choice:** Option 2: Pololu 250:1 Micro Metal Gearmotor MP 6V

**Rationale:** The 6 V rail keeps the whole system on one motor rail as the power budget guidance recommends. Its stall torque is about fourteen times that of the TT motor, which gives margin while the real torque requirement of the arm is still unknown. The higher price is acceptable because the lower-cost motors would have to be replaced if the arm load turns out to be heavier. 

## Position Sensor

1. Bourns 6639S-1-103, 10 kΩ single-turn conductive plastic precision potentiometer

    <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/e34d8ba1-1b92-40b1-bc82-2d9252d5a220" />

    * $24.77/each
    * [link to product](https://www.mouser.com/en/ProductDetail/Bourns/6639S-1-103/?qs=sGAEpiMZZMtygI3JAGOxU%2FcoYPJDRhcE)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Single analog output goes straight to RA0, using one pin and no driver code. | Highest price of the three position sensors |
    | The reading is still valid after power loss, so no homing routine is needed. | Mechanical contact wear over time. |
    | Not affected by the magnetic field of the motor. | The wiper can be noisy, so the firmware should average several ADC samples. |
    | Used as a divider between 3.3 V and GND, the ±15% resistance tolerance does not matter because the reading is ratiometric. |

2. Bourns 3590S-2-103L, 10 kΩ 10-turn wirewound precision potentiometer

    <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/ca09a138-dd53-4f1d-80ad-9da43b2df136" />


    * $17.78/each
    * [link to product](https://www.newark.com/bourns/3590s-2-103l/potentiometer-10kohm-5-linear/dp/62K3206)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Lower price than Option 1 | a joint that moves less than one revolution would use only a small part of the range, which wastes ADC resolution unless it is geared up. |
    | ±0.25% independent linearity, the best of the three. | Wirewound elements change resistance in small steps rather than continuously. |
    | 2 W power rating and a −40 °C to +125 °C operating range.| Larger body and a gear or pulley train would be needed, adding mechanical complexity |

3. Adafruit AS5600 magnetic angle sensor (STEMMA QT)

    <img width="210" height="200" alt="image" src="https://github.com/user-attachments/assets/1b8bd053-27db-4658-8aad-f540fbf11456" />


    * $5.95/each
    * [link to product](https://www.adafruit.com/product/6357)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Lowest cost | Needs a diametrically magnetized magnet centered on the shaft axis |
    | Contactless, so there is no wear | The motor's magnets and currents can disturb the magnetic reading |
    | 12-bit absolute angle (4096 steps per revolution) | Whether the analog OUT pin is available on this board must be confirmed |
    | Can be read over I2C or analog voltage. | More design work needed |
<br>
**Choice:** Option 1, Bourns 6639S-1-103.
<br>
**Rationale:** The potentiometer matches the block diagram exactly: one analog wire to RA0 and nothing else to configure. A single-turn part fits an arm joint that moves less than one revolution, while the 10-turn Option 2 would waste most of its range. Unlike the AS5600, it is immune to the magnetic fields next to the motor, and it needs no magnet alignment. The extra cost ($6.99 more than Option 2) buys the correct travel range. If wear or cost becomes an issue, the AS5600 is the planned fallback.
<br>
## Motor Power Source

1. Mean Well GST60A12-P1J, 12 V 5 A desktop AC adapter

    <img width="300" height="208" alt="image" src="https://github.com/user-attachments/assets/06a5bf69-9a9f-4ab7-9c72-06d2f406a843" />


    * $19.40/each
    * [link to product](https://www.mouser.com/en/ProductDetail/MEAN-WELL/GST60A12-P1J?qs=odmYgEirbwzBCeXKJrW1mg%3D%3D)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Regulated 12 V at 5 A with 120 mVp-p ripple, no extra voltage regulator is needed on the motor rail. | The AC inlet is IEC C14, so a power cord must be purchased separately |
    | Overload and over voltage protection. | At the motor's 5 A stall current the supply would be at 100% of its rating, no margin |
    | 2.1 × 5.5 mm barrel plug and 4,059 units in stock | Tethered to a wall outlet, not portable |
    | Full datasheet is available |

2. Adafruit 12 V 5 A switching power supply

    <img width="325" height="243" alt="image" src="https://github.com/user-attachments/assets/6c7829d7-de89-4691-91d4-b94ad93d739d" />


    * $24.95/each
    * [link to product](https://www.adafruit.com/product/352)

    | Pros                                      | Cons                                                             |
    | ----------------------------------------- | ---------------------------------------------------------------- |
    | Regulated 12 V at 5 A with 120 mVp-p ripple, no extra voltage regulator is needed on the motor rail. | The AC inlet is IEC C14, so a power cord must be purchased separately |
    | Overload and over voltage protection. | At the motor's 5 A stall current the supply would be at 100% of its rating, no margin |
    | 2.1 × 5.5 mm barrel plug and 4,059 units in stock | Tethered to a wall outlet, not portable |
    | Full datasheet is available |






   
