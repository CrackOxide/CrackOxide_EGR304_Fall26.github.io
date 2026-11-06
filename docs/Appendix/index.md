---
title: Appendix - Datasheets
---

## Datasheets

Local copies of the datasheets for every part on the [Bill of Materials](../03-BOM/BOM.md), saved in this repository so they stay available if a vendor page changes. Reference designators match the [schematic](../04-Schematic/schematic.md).

| Part | Manufacturer / Part Number | Reference Designators | Datasheet |
|---|---|---|---|
| Dual H-bridge motor driver | onsemi (Fairchild) FAN8100N | U1 | [FAN8100N, MTC](Datasheets/FAN8100N,MTC.pdf) |
| MCU board | Microchip PIC18F57Q43 Curiosity Nano (DM164150) | A1 | [Hardware User Guide](Datasheets/PIC18F57Q43-Curiosity-Nano-HW-UserGuide-DS40002186B.pdf) |
| DC gearmotor 6 V, 50 rpm, 298:1 | DFRobot FIT0579 | B1 | [Specifications (RobotShop)](https://www.robotshop.com/products/dfrobot-micro-metal-dc-geared-motor-6v-50rpm-250gcm); no full datasheet is published |
| Adjustable regulator (6 V rail) | STMicroelectronics LM317T | VR1 | [LM217, LM317](Datasheets/DS_lm217.pdf) |
| 5 V regulator | STMicroelectronics L7805CV | VR2 | [L78](Datasheets/DS_l78.pdf) |
| TO-220 heat sink | Aavid (Boyd) 577102B00000G | VR1 heat sink | [Board-level heat sinks](Datasheets/Aavid_Board_Level_Heatsinks_Cat_1_-3044572.pdf) |
| Schottky diode 1 A 40 V | onsemi 1N5819RLG | D1 | [1N5817 – 1N5819](Datasheets/1N5817-D.PDF) |
| Fuse 1 A slow-blow, 5 × 20 mm | Littelfuse 0218001.MXP | F1 | [218 series](Datasheets/Littelfuse-Fuse-218-Datasheet.pdf) |
| Fuse clip | Keystone 3517 | F1 holder | [3517](Datasheets/3517.pdf) |
| DC power jack 2.1 × 5.5 mm | Same Sky PJ-102A | J1 | [PJ-102A](Datasheets/pj_102a.pdf) |
| 9 V 2.55 A wall adapter | MEAN WELL GST25A09-P1J | External (J1) | [GST25A series](Datasheets/GST25A-SPEC.pdf) |
| AC power cord | Same Sky AC-C13-R NA | External (adapter) | [AC-C13-R NA](Datasheets/ac-c13-r-na.pdf) |
| Ceramic capacitors 0.33 µF / 0.1 µF | Vishay K334K20X7RF5TH5 / K104K15X7RF5WH5 | C1–C6, C8 | [K series](Datasheets/kseries.pdf) |
| Electrolytic capacitor 47 µF 16 V | Panasonic EEU-FC1C470H | C7 | [FC series](Datasheets/ABA0000C1209.pdf) |
| Carbon film resistors 1/4 W | Stackpole CF14 series | R1–R10 | [CF / CFM series](Datasheets/SEI_CF_CFM.pdf) |
| LED 3 mm green | Kingbright WP710A10SGD | DS1 | [WP710A10SGD](Datasheets/WP710A10SGD.pdf) |
| LED 3 mm yellow | Kingbright WP710A10YD | DS2 | [WP710A10YD](Datasheets/WP710A10YD.pdf) |
| Tactile switch | Omron B3F-1000 | SW1 | [B3F](Datasheets/en_b3f.pdf) |
| Test point | Keystone 5001 | TP1, TP2 | [5000 – 5004](Datasheets/5000_5004.pdf) |
| Terminal block 2-position | Phoenix Contact 1935161 | J2 | [1935161](Datasheets/phoenix_contact_1935161_en.pdf) |

Generic stock parts (DIP socket, 1 × 40 male and female headers, the 2 × 4 pin header J3 and the female-to-female jumper wires) have no part-specific datasheet.
