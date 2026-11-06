---
title: Individual Block Diagram
---

## Overview

This block diagram shows the blocks of the Arm Motion Control board, how power and signals move between them, and how the board connects to the rest of the team.

* **Microcontroller:** the board runs on a PIC18F57Q43 Curiosity Nano. The Nano is powered from its own USB port and uses 3.3 V logic with a 0–3.3 V analog range.
* **Power:** a 9 V DC wall adapter plugs into a barrel jack.
    * The input goes through a 1 A slow-blow fuse and a 1N5819 reverse-polarity diode.
    * An LM317T, set by R11 = 240 Ω and R12 = 910 Ω, makes the 6.0 V motor rail.
    * An L7805 makes the 5 V logic rail.
    * Motor current never passes through the microcontroller board.
    * In the diagram, the power path is drawn only from the source to the regulators. Blocks that receive power have no supply lines pointing to them; instead the rail each block runs from is written in bold inside it (for example **PVCC +6 V / VCC +5 V** on the H-bridge, **3.3 V** on the LED, button and J4).
* **Actuator:** an onsemi FAN8100N H-bridge drives a 6 V DFRobot FIT0579 DC gearmotor (298:1). The motor has two wires, M+ and M−. RC4 and RC5 (PWM1 outputs 1 and 2, routed with PPS) provide the two PWM inputs.
* **Debug:**
    * A status LED on RE0.
    * A push button on RE1, using the weak pull-up.
    * Expansion header J4, which brings out 3.3 V, GND and the spare pins RA0, RA2, RB2 and RB3.
* **Team connection:** the board connects to the Gripper & Object Handling board through the 8-pin team link: a 2 × 4 pin header (J3) and female-to-female jumper wires, one per signal.
    * It receives SAFE_OK, RUN_REQ, OBJ_HELD and the analog SPEED_SET.
    * It sends GRIP_CMD and ARM_IN_POS.
    * Pin 7 (GRIP_FORCE) is not used on this board and is left open. Pin 8 is GND.
* **Ground:** all grounds are tied together. This includes USB, the 9 V supply, the H-bridge and team-link pin 8.

## Block Diagram

![Arm Motion Control individual block diagram](Arm_Motion_Control_Individual_Block_Diagram.png)
**Figure 1:** Arm Motion Control individual block diagram.

## Resources

The block diagram source files (the editable draw.io file and the exported PNG) are available as a [*Zip download*](Arm_Motion_Control_Individual_Block_Diagram_source.zip). The draw.io file can also be opened directly: [*Arm_Motion_Control_Individual_Block_Diagram.drawio*](Arm_Motion_Control_Individual_Block_Diagram.drawio).
