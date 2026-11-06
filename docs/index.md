---
title: Welcome
---
<center>
<font size= "6"> Yixiang Ren Datasheet</font><br>
as part of<br>
<font size= "8"> Simple Educational Robotic Arm</font><br>
for<br>
<font size= "5"> Team 107 </font><br>

**Submission: Oct 30, 2026**
</center>

## Introduction

This datasheet documents the **Arm Motion Control** subsystem of Team 107's robotic arm, designed by Yixiang Ren for EGR 304 Embedded Systems Design at Arizona State University. It collects the design work for this one board: the block diagram, how each part was chosen, the bill of materials, the schematic and the power budget. A reader can use it to understand, build, test or modify the board without other documents.

### Project Summary

Team 107 is building a **Simple Educational Robotic Arm**: a low-cost desktop arm that performs repeatable pick-and-place tasks and is meant for students, educators and hobbyists who are learning robotics and embedded systems. The system is split into three boards, each with its own PIC18F57Q43 Curiosity Nano, linked in a daisy chain by an 8-pin ribbon cable:

| Board | Owner | Role |
|---|---|---|
| **Arm Motion Control** (this datasheet) | Yixiang Ren | Drives the arm joint motor and reports when the arm is in position |
| Gripper & Object Handling | Canyon Miller | Opens and closes the gripper and senses the held object |
| User Controls & Safety | Dunyue Yang | Start, stop and speed inputs, status LEDs and buzzer |

The full project, including user needs, product requirements, the team block diagram and the software proposal, is in the [**Team 107 report**](https://egr304-2026-f-107.github.io/).

### My Contribution

The Arm Motion Control board turns commands from the team into arm movement:

* **Power:** it takes a 9 V wall adapter, protects the input with a fuse and a reverse-polarity diode, and makes a 6 V motor rail (LM317T) and a 5 V logic rail (L7805).
* **Motor drive:** an onsemi FAN8100N H-bridge drives a 6 V DFRobot FIT0579 micro gearmotor in both directions, with speed set by PWM from the PIC.
* **Team link:** on the 8-pin team link (2 × 4 pin header and jumper wires) it reads SAFE_OK, RUN_REQ, OBJ_HELD and the analog SPEED_SET, and it sends GRIP_CMD and ARM_IN_POS. An unplugged wire reads as "stop".
* **Debug and expansion:** a status LED, a push button, test points on both rails and a spare-I/O header (J4) make the board easy to test and to extend.

### Where to find things

| Section | What it contains |
|---|---|
| [01 Block Diagram](01-Block-Diagram/Block-Diagram.md) | How power and signals move through the board and connect to the team |
| [02 Component Selection](02-Component-Selection/Component-Selection.md) | Options compared for each major part, the decisions and the MCC pin configuration |
| [03 BOM](03-BOM/BOM.md) | Every part with quantity, cost, vendor and datasheet links, plus the purchase requests |
| [04 Schematic](04-Schematic/schematic.md) | The KiCad schematic (image, PDF and project zip) and how it meets the user needs |
| [05 Power Budget](05-Power-Budget/Power-Budget.md) | Worst-case current on every rail and source, and what it means for the design |
| [Appendix](Appendix/index.md) | Datasheets for every part on the BOM |
