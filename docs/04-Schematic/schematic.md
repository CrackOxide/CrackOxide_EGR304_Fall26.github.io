---
title: Schematic
---

## Overview

This schematic is the Arm Motion Control subsystem of Team 107 Simple Educational Robotic Arm. It is drawn in KiCad 9 with US/ANSI symbols, and parts are joined by wires rather than net labels wherever possible, so the signal path can be followed by eye. The sheet has five blocks:

* **Power:** a 9 V DC barrel jack feeds a 1 A slow-blow fuse and a 1N5819 reverse-polarity Schottky diode, giving VIN_PROT of about 8.55 V. VR1 is an LM317T set to 6.0 V by R11 = 240 Ω and R12 = 910 Ω, using Vout = 1.25 V × (1 + 910 / 240) = 6.0 V. This 6 V rail is the motor rail. VR2 makes the +5 V logic rail for the H-bridge VCC and the power LED DS1. Each regulator has 0.33 µF on its input and 0.1 µF on its output. Test points TP1 and TP2 are on the 6 V and 5 V rails.
* **Microcontroller:** PIC18F57Q43 Curiosity Nano, powered from its own USB port with 3.3 V logic.
* **Motor drive:** an onsemi FAN8100N H-bridge drives the 6 V DFRobot FIT0579 gearmotor (298:1, 430 mA maximum at stall) through M+ and M−. The motor has only these two pins. RC4 and RC5 supply PWM (PWM1 outputs 1 and 2, routed with PPS; PWM1 cannot be routed to PORTB on this PIC). The motor supply has 47 µF and 0.1 µF bulk and decoupling capacitors.
* **Debug and expansion:**
    * A status LED on RE0.
    * A push button on RE1, using the weak pull-up.
    * J4, a 6-pin expansion header carrying 3.3 V, GND, RA0, RA2, RB2 and RB3.
    * J5, a 6-pin test header (0.1 in pitch) carrying PWM1, PWM2, SPEED_SET, ARM_IN_POS and two GND pins for a scope or logic analyser.
    * Test points TP1 (+6 V), TP2 (+5 V) and TP3 (GND).
* **Team link (J3):** an unshrouded 2 × 4 pin header (2.54 mm). The other boards connect with eight female-to-female jumper wires, one per signal. Pins 1 to 8 carry, in order:
    * SAFE_OK (in)
    * RUN_REQ (in)
    * GRIP_CMD (out)
    * OBJ_HELD (in)
    * ARM_IN_POS (out)
    * SPEED_SET (analog in)
    * pin 7, which is not used on this board
    * GND

  The three digital inputs have 10 kΩ pull-downs, so an unplugged cable reads 0, which means stop. The two outputs have 330 Ω series resistors. SPEED_SET has a 1 kΩ / 0.1 µF RC filter.

![Arm Motion Control schematic](Arm_Motion_Control_page-0001.png)
**Figure 1:** Arm Motion Control schematic (click the image to enlarge).

**Revision 2.5 (2026-11-06), test points for PCB bring-up:**

* **J5** test header (1 × 6, 2.54 mm): pin 1 PWM1 (RC4), 2 PWM2 (RC5), 3 SPEED_SET (RA1), 4 ARM_IN_POS (RD4, before R6), 5–6 GND. The nets have named labels (PWM1, PWM2, SPEED_SET, ARM_IN_POS).
* **TP3**: a GND test point next to TP1 and TP2, so both rails can be measured against a nearby ground.

**Revision 2.4 (2026-11-06), footprints checked for PCB layout:** no circuit changes; the netlist is the same as rev 2.3.

* **A1:** new footprint `YR_Curiosity_Nano_PIC18F57Q43` (2 × 28 pins, 2.54 mm pitch, rows 15.24 mm apart). The symbol pin numbers were changed to the Curiosity Nano's edge-pin numbers (for example RC4 = pin 11, RD0 = pin 20, VTG = pin 51), so the schematic and the board use the same numbers.
* **U1:** the FAN8100N footprint was corrected to the 12-DIPH-300 drawing: pins 4–6 sit at 12.70–17.78 mm, and each side has one 5.1 mm heat-sink fin lead (pad 13, GND) centred at 8.89 mm with a slotted hole. U1 is soldered directly, because the fin leads do not fit a DIP socket.
* **C1, C3** (0.33 µF, size code 20, 5.0 × 3.2 mm body): `C_Disc_D5.1mm_W3.2mm_P5.00mm`. **C7** (5 × 11 mm, 2.0 mm lead pitch): `CP_Radial_D5.0mm_P2.00mm`.
* **J2** (Phoenix 1935161, PT 1,5/2-5,0-H): `TerminalBlock_Phoenix_PT-1,5-2-5.0-H`. **TP1, TP2** (Keystone 5001): `TestPoint_Keystone_5000-5004_Miniature`.

**Revision 2.3 (2026-11-06):**

* **Motor:** B1 changed from the Pololu #2370 to the DFRobot FIT0579 (Mouser 426-FIT0579) for budget and efficiency reasons; see [Component Selection](../02-Component-Selection/Component-Selection.md). It has the same 6 V rating and two-wire connection, so the drive circuit is unchanged.
* **Team link:** J3 changed from a keyed IDC box header with a ribbon cable to an unshrouded 2 × 4 pin header used with female-to-female jumper wires. The footprint is now `PinHeader_2x04_P2.54mm_Vertical`. Its pad positions and pin numbers are the same as the old IDC footprint, so the pin assignment and wiring do not change.

**Revision 2.2:** the motor PWM lines MOT_FWD and MOT_REV moved from RB0 / RB1 to **RC4 / RC5**. MCC showed that the PIC18F57Q43 can route its PWM1 outputs only to PORTC and PORTF, and neither PWM1 nor CCP1 / CCP2 can reach PORTB. Only the two Nano pins changed; R8, R9 and the FAN8100N side are the same.

## 3.3 V Operation Check

The PIC18F57Q43 on this board runs at **3.3 V**. It is powered by the Curiosity Nano's own MIC5353 regulator from USB, and the VTG pin (+3V3 in the schematic) is that regulator's output. Nothing on this board drives VTG. Every connection to the PIC was checked against 3.3 V operation:

| Check | Requirement | Result |
|---|---|---|
| PIC18F57Q43 supply range | Operating voltage 1.8 V – 5.5 V (PIC18-Q43 family product brief) | 3.3 V is inside the range ✔ |
| Curiosity Nano target voltage | MIC5353 adjustable 1.8 V – 5.1 V, **set to 3.3 V at the factory** ([user guide](../Appendix/Datasheets/PIC18F57Q43-Curiosity-Nano-HW-UserGuide-DS40002186B.pdf), sec. 3.3.1 "Target Regulator") | Leave the target voltage at 3.3 V in the MPLAB X project properties ✔ |
| Regulator current | 3.3 V loads need about 99 mA with margin ([Power Budget](../05-Power-Budget/Power-Budget.md)); MIC5353 supplies 500 mA | ✔ |
| PIC → FAN8100N inputs (RC4, RC5) | FAN8100N input high ≥ 1.8 V, input low ≤ 0.7 V, input current ≤ 200 µA; datasheet lists "3.3 V and 5 V micro-controller interface" ([datasheet](../Appendix/Datasheets/FAN8100N,MTC.pdf)) | A 3.3 V output is well above 1.8 V. The FAN8100N logic supply is 5 V, but its inputs only need 1.8 V, so no level shifter is needed ✔ |
| SPEED_SET analog input (RA1) | ADC reference = VDD = 3.3 V; the User board's speed knob also runs from its Nano's 3.3 V, so the signal is 0 – 3.3 V | ✔ |
| Team-link signals to and from the other boards | All three boards use PIC18F57Q43 Curiosity Nanos at 3.3 V, so every logic level on the team link is 0 / 3.3 V | ✔ **All three Nanos must stay at 3.3 V.** If one board's target voltage were changed to 5 V, its outputs would exceed this PIC's 3.3 V supply. |
| Debug LED DS2 on RE0 | (3.3 V − 2.1 V) / 330 Ω ≈ 3.6 mA, a small load for one I/O pin | ✔ |
| Debug button SW1 on RE1 | Internal weak pull-up to 3.3 V; the button pulls to GND | ✔ |
| J4 3.3 V pin | Comes from VTG, so an add-on sensor runs at the same 3.3 V logic level as the PIC | ✔ |

The only 5 V and 6 V nets on the board are the FAN8100N supply pins (VCC, PVCC), the motor and the power LED. None of them connects to a PIC pin.

## Footprints

Every part on the board has a through-hole footprint that was checked against its datasheet before PCB layout. B1 (the motor) is off-board and connects through J2.

| Ref | Part | Footprint | Checked against |
|---|---|---|---|
| A1 | PIC18F57Q43 Curiosity Nano | YR_Custom:YR_Curiosity_Nano_PIC18F57Q43 | User guide pinout (Fig. 4-1); 2 × 28 at 2.54 mm, rows 15.24 mm apart |
| U1 | FAN8100N | YR_Custom:YR_DIPH-12_W7.62mm_Fin | 12-DIPH-300 package drawing (datasheet p. 12) |
| VR1, VR2 | LM317T, L7805CV | TO-220-3_Vertical | TO-220 pinout: LM317 1 ADJ / 2 OUT / 3 IN; L7805 1 IN / 2 GND / 3 OUT |
| D1 | 1N5819 | D_DO-41_SOD81_P10.16mm_Horizontal | DO-41 axial |
| F1 | Keystone 3517 clips | Fuseholder_Clip-5x20mm_Keystone_3517 | Keystone 3517 |
| J1 | PJ-102A | BarrelJack_Horizontal | PJ-102A layout: pins 1–2 6.0 mm apart, pin 3 4.7 mm to the side, slotted holes |
| J2 | Phoenix 1935161 | TerminalBlock_Phoenix_PT-1,5-2-5.0-H | 5 mm pitch, 1.3 mm holes |
| J3 | 2 × 4 pin header | PinHeader_2x04_P2.54mm_Vertical | 2.54 mm grid |
| J4, J5 | 1 × 6 pin headers | PinHeader_1x06_P2.54mm_Vertical | 2.54 mm grid |
| C1, C3 | Vishay K334K20 (size 20) | C_Disc_D5.1mm_W3.2mm_P5.00mm | 5.0 × 3.2 mm body, 5.0 mm leads |
| C2, C4–C6, C8 | Vishay K104K15 (size 15) | C_Disc_D5.0mm_W2.5mm_P5.00mm | 4.0 × 2.6 mm body, 5.0 mm leads |
| C7 | Panasonic EEU-FC1C470H | CP_Radial_D5.0mm_P2.00mm | 5 mm diameter, 2.0 mm leads |
| R1–R12 | 1/4 W axial | R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal | 1/4 W body, 10.16 mm lead bend |
| DS1, DS2 | 3 mm LEDs | LED_D3.0mm | 2.54 mm leads; pad 1 = cathode |
| SW1 | Omron B3F-1000 | SW_PUSH_6mm | 6.5 × 4.5 mm pin pattern |
| TP1–TP3 | Keystone 5001 | TestPoint_Keystone_5000-5004_Miniature | Keystone 5000–5004 |

**Layout notes:** the 577102B00000G heat sink on VR1 has no PCB tabs. It is held by the TO-220 mounting screw, so leave about 10 mm of clear space behind VR1's tab. The LM317T tab is at +6 V, so the heat sink must not touch other parts. Keep the motor current path (J1 → F1 → D1 → VR1 → U1 → J2) short and wide, at least 0.6 mm (25 mil) for 0.65 A worst case.

## How the Schematic Meets the User Needs and Product Requirements

The team grouped its user needs into eleven categories and turned them into product requirements PR-01 to PR-18 ([user needs](https://egr304-2026-f-107.github.io/03-User-Needs-and%20Benchmarking/#organized-need-statements), [product requirements](https://egr304-2026-f-107.github.io/04-Product-Requirements/)). The table shows which parts of this schematic serve each need that applies to the Arm Motion Control board, and how.

| User need category | Requirements | What in the schematic serves it | How it works |
|---|---|---|---|
| **Safety** | PR-12, PR-14, Reg. 6.3, 6.7 | R2, R3, R5 pull-downs on SAFE_OK, RUN_REQ, OBJ_HELD; R8, R9 pull-downs on the H-bridge inputs; F1; D1; FAN8100N thermal shutdown | If a jumper wire or the whole team link is unplugged or the User board drops SAFE_OK, the inputs read 0 and the firmware stops the motor. R8 and R9 hold both H-bridge inputs low while the PIC resets, so the motor cannot twitch at power-up. F1 (1 A slow-blow) opens on a short, D1 blocks a reversed adapter, and the FAN8100N shuts down if it overheats during a stall. |
| **Accuracy & Repeatability** | PR-01, PR-02, PR-04 | VR1 LM317T regulated 6 V rail; C6, C7 on the motor supply; PWM on RC4 / RC5 | The motor always sees a regulated 6.0 V (set by 1 % resistors R11 / R12) instead of a raw adapter voltage, so the same PWM duty gives the same speed every run. Bulk and bypass capacitors keep the rail steady when the motor starts. |
| **Programming & Control** | PR-07, PR-16 | FAN8100N forward / reverse inputs on two PWM pins; SPEED_SET on RA1 (ADC) | Speed and direction are two duty-cycle values, which is easy for a student to change in code and see on the arm. SPEED_SET from the User board is read by the ADC through a 1 kΩ / 0.1 µF filter, so the speed knob gives a smooth reading. |
| **Gripper & Object Handling** (team link) | PR-01, PR-03 | J3 team link: GRIP_CMD and ARM_IN_POS outputs with R4, R6 (330 Ω); OBJ_HELD input | The arm tells the gripper when to close and reports when it is in position, and it waits for OBJ_HELD before moving on. The 330 Ω resistors limit current if two boards ever drive the same wire. |
| **Documentation & Troubleshooting** | PR-09, PR-18 | TP1 (+6 V), TP2 (+5 V), TP3 (GND); J5 test header; power LED DS1; debug LED DS2 on RE0; button SW1 on RE1 | DS1 shows at a glance that the 5 V rail is up. The test points let a user check both rails against a nearby ground, and J5 brings the PWM, speed and in-position signals to a 0.1 in header for a scope or logic analyser. DS2 and SW1 let the firmware show its state and step through a sequence during troubleshooting. |
| **Sensors, Vision & Expansion** | PR-10, PR-11 | J4 header (3.3 V, GND, RA0, RA2, RB2, RB3); unused FAN8100N channel B | A sensor such as a joint potentiometer or magnetic encoder can be added on J4 (RA0 and RA2 are analog-capable) without a new PCB. The second H-bridge channel is available for a second motor. |
| **Calibration, Maintenance & Repair** | PR-05, PR-10 | Curiosity Nano on two 1 × 28 female headers; J2 screw terminal for the motor; through-hole U1 | The MCU board and the motor can each be replaced without desoldering. U1 is soldered directly, because its heat-sink fin leads do not fit a DIP socket, but as a through-hole part it can still be desoldered and replaced with ordinary tools. |
| **Assembly, Wiring & Components** | PR-10, PR-14 | All through-hole parts; J3 2 × 4 pin header with labelled pins; parts run within ratings | The board can be hand-soldered and built on a breadboard first. J3 is not keyed, so pin 1 and the signal names are marked next to it and GND uses a fixed wire colour. A wire plugged into the wrong pin cannot damage anything: the header carries only 3.3 V logic and GND, outputs have 330 Ω series resistors, and inputs have pull-downs. The [Power Budget](../05-Power-Budget/Power-Budget.md) shows every part stays within its limits. |
| **Power, Stability & Physical Design** | PR-13, PR-14, Reg. 6.1 | 9 V adapter, VR1 with heat sink, VR2, separate motor and logic rails | Everything runs from a low-voltage desktop adapter. The motor and the logic have separate regulators, so motor noise does not reach the logic supply, and VR1's heat sink keeps it cool at stall. |
| **Cost & Accessibility** | PR-15, PR-17 | FAN8100N and passives already in hand; common TO-220 regulators | The parts to order cost $128.35 in total, and every part is a common, documented through-hole component. |

**Signal path, start to finish:** the User board raises SAFE_OK and RUN_REQ → the PIC reads SPEED_SET on the ADC and drives PWM on RC4 (forward) or RC5 (reverse) → the FAN8100N switches the 6 V rail across the motor → when the move is done the PIC raises ARM_IN_POS and GRIP_CMD → the Gripper board answers on OBJ_HELD → the arm moves to the place position. At any point, SAFE_OK going low sets both PWM outputs to 0 % and the motor stops.

## Resources

The schematic (rev 2.5) is available as a [*PDF download*](Arm_Motion_Control.pdf). The complete KiCad project (schematic, PCB layout and the YR_Custom symbol and footprint libraries) and the Gerber files are on the [PCB Design](../06-PCB-Design/PCB-Design.md) page.
