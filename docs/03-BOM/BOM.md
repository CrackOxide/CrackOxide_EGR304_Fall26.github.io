---
title: Bill of Materials
hide:
  - navigation
  - toc
---

## Overview

This page lists every component of the **Arm Motion Control** subsystem, taken from the subsystem schematic . It also lists the off-board items the system needs to run and the debugging and expansion hardware.

How the quantities were chosen:

* One set for a breadboard prototype, one set for the subsystem PCB, and one or two spares, as the assignment asks.
* Through-hole parts only (nothing smaller than 0805), so every part can be hand-soldered and used on a breadboard.
* Parts that are in hand, handed out in class or kept in Peralta 109 (resistors, LEDs, fuses, IC sockets, headers) are still listed, but they are not on a purchase request.

The table is sorted by vendor, one section per purchase request. Prices and stock were checked on the vendor pages on 2026-10-30 and should be re-checked before the order is sent.

## Bill of Materials

<!-- BOM:START -->
### Mouser Electronics

| **Part Name/Description** | **Qty** | **Unit Cost** | **Total Cost** | **Manufacturer** | **Manufacturer #** | **Vendor Link** | **Datasheet Link** | **Schematic Reference Designators** |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Adjustable linear regulator, 1.5 A, TO-220 (set to 6.0 V for the motor rail) | 3 | $0.76 | $2.28 | STMicroelectronics | LM317T | [Mouser](https://www.mouser.com/ProductDetail/STMicroelectronics/LM317T?qs=swDD%2BF%2Bps7c8uLyY%2B3mJJw%3D%3D) | [Datasheet](https://www.st.com/resource/en/datasheet/lm217.pdf) | VR1 |
| 5 V linear regulator, 1.5 A, TO-220 | 3 | $0.60 | $1.80 | STMicroelectronics | L7805CV | [Mouser](https://www.mouser.com/en/ProductDetail/STMicroelectronics/L7805CV?qs=9NrABl3fj%2FqplZAHiYUxWg%3D%3D) | [Datasheet](https://www.st.com/resource/en/datasheet/l78.pdf) | VR2 |
| Heat sink, TO-220, channel style, 25.9 C/W | 3 | $1.07 | $3.21 | Aavid (Boyd) | 577102B00000G | [Mouser](https://www.mouser.com/ProductDetail/Aavid/577102B00000G?qs=cR7Qvk1oinlekh9MFs6NUA%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/2/2/Aavid_Board_Level_Heatsinks_Cat_1_-3044572.pdf) | VR1 (heat sink) |
| Schottky diode 1 A 40 V, DO-41 (reverse-polarity protection) | 3 | $0.55 | $1.65 | onsemi | 1N5819RLG | [Mouser](https://www.mouser.com/en/ProductDetail/onsemi/1N5819RLG?qs=y2kkmE52mdN7fhfvNgYV6A%3D%3D) | [Datasheet](https://www.onsemi.com/pdf/datasheet/1n5817-d.pdf) | D1 |
| DC power jack 2.1 x 5.5 mm, PCB mount | 3 | $0.70 | $2.10 | Same Sky (CUI) | PJ-102A | [Mouser](https://www.mouser.com/en/ProductDetail/Same-Sky/PJ-102A?qs=WyjlAZoYn50UKjtnxOz%2Bqg%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/3/6118/1/pj_102a.pdf) | J1 |
| Fuse clip for 5 mm (5 x 20 mm) fuse, PCB mount | 4 | $0.33 | $1.32 | Keystone Electronics | 3517 | [Mouser](https://www.mouser.com/en/ProductDetail/Keystone-Electronics/3517?qs=qOqV1E1P08RwsK9hgzJijw%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/3/201/1/3517.PDF) | F1 (holder) |
| Ceramic capacitor 0.33 uF 50 V X7R, radial, 5 mm lead spacing | 6 | $1.02 | $6.12 | Vishay BC Components | K334K20X7RF5TH5 | [Mouser](https://www.mouser.com/ProductDetail/Vishay-BC-Components/K334K20X7RF5TH5?qs=lQAVKuKFhkL6tfc7l6Mmyw%3D%3D) | [Datasheet](https://www.vishay.com/doc?45171) | C1, C3 |
| Ceramic capacitor 0.1 uF 50 V X7R, radial, 5 mm lead spacing | 12 | $0.27 | $3.24 | Vishay BC Components | K104K15X7RF5WH5 | [Mouser](https://www.mouser.com/en/ProductDetail/Vishay-BC-Components/K104K15X7RF5WH5?qs=8fb2TFeI5qGYDjl7%2BWZxcg%3D%3D) | [Datasheet](https://www.vishay.com/doc?45171) | C2, C4, C5, C6, C8 |
| Aluminum electrolytic 47 uF 16 V, radial 5 x 11 mm | 3 | $0.38 | $1.14 | Panasonic | EEU-FC1C470H | [Mouser](https://www.mouser.com/ProductDetail/Panasonic/EEU-FC1C470H?qs=/C1U95aQ15vhemYBctOGEw%3D%3D) | [Datasheet](https://industrial.panasonic.com/cdbs/www-data/pdf/RDF0000/ABA0000C1209.pdf) | C7 |
| Terminal block, 2 position, 5.0 mm pitch | 2 | $0.53 | $1.06 | Phoenix Contact | 1935161 | [Mouser](https://www.mouser.com/ProductDetail/Phoenix-Contact/1935161?qs=W3wJikR1%252BS6eKzfFl8Rbew%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/3/507/9/phoenix_contact_1935161_en.pdf) | J2 |
| Shrouded box header 2 x 4, 2.54 mm, through hole | 2 | $2.88 | $5.76 | Samtec | TST-104-01-G-D | [Mouser](https://www.mouser.com/ProductDetail/Samtec/TST-104-01-G-D?qs=rU5fayqh%2BE32/80vAsdSrw%3D%3D) | [Datasheet](https://suddendocs.samtec.com/prints/tst-1xx-xx-x-x-xx-xx-mkt.pdf) | J3 |
| IDC ribbon cable assembly, 2 x 4, 2.54 mm, 9 in | 1 | $6.46 | $6.46 | Samtec | IDSD-04-D-09.00 | [Mouser](https://www.mouser.com/en/ProductDetail/Samtec/IDSD-04-D-09.00?qs=0lQeLiL1qybglLttr7ZyDQ%3D%3D) | [Datasheet](https://www.mouser.com/en/ProductDetail/Samtec/IDSD-04-D-09.00?qs=0lQeLiL1qybglLttr7ZyDQ%3D%3D) | Team cable |
| Tactile switch 6 x 6 mm, through hole | 3 | $0.35 | $1.05 | Omron | B3F-1000 | [Mouser](https://www.mouser.com/ProductDetail/Omron-Electronics/B3F-1000?qs=lK7M36XCk6JQHckSc1xIsg%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/3/39/1/en_b3f.pdf) | SW1 |
| Test point, miniature PC loop | 4 | $0.26 | $1.04 | Keystone Electronics | 5001 | [Mouser](https://www.mouser.com/en/ProductDetail/Keystone-Electronics/5001?qs=q0tsjPZWdm%2FW0vdr%2FwowKg%3D%3D) | [Datasheet](https://www.mouser.com/datasheet/3/201/1/5000_5004.PDF) | TP1, TP2 |
| AC/DC wall adapter 9 V 2.55 A, 2.1 x 5.5 mm plug, C14 inlet | 1 | $14.30 | $14.30 | MEAN WELL | GST25A09-P1J | [Mouser](https://www.mouser.com/en/ProductDetail/MEAN-WELL/GST25A09-P1J?qs=drgMNd%252BkGPP0sFLpGSh7oQ%3D%3D) | [Datasheet](https://www.meanwellusa.com/webapp/product/search.aspx?prod=GST25A) | External (J1) |
| AC power cord NEMA 5-15P to IEC C13, 6 ft | 1 | $6.39 | $6.39 | Same Sky | AC-C13-R NA | [Mouser](https://www.mouser.com/en/ProductDetail/Same-Sky/AC-C13-R-NA?qs=%252BXxaIXUDbq2HADzpjg7LkA%3D%3D) | [Datasheet](https://www.mouser.com/en/ProductDetail/Same-Sky/AC-C13-R-NA?qs=%252BXxaIXUDbq2HADzpjg7LkA%3D%3D) | External (adapter) |

**Mouser Electronics subtotal: $58.92** (16 line items)

### Pololu

| **Part Name/Description** | **Qty** | **Unit Cost** | **Total Cost** | **Manufacturer** | **Manufacturer #** | **Vendor Link** | **Datasheet Link** | **Schematic Reference Designators** |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| 250:1 Micro Metal Gearmotor MP 6 V | 3 | $23.95 | $71.85 | Pololu | item #2370 | [Pololu](https://www.pololu.com/product/2370) | [Datasheet](https://www.pololu.com/file/0J1487/pololu-micro-metal-gearmotors-rev-6-2.pdf) | B1 (off-board) |

**Pololu subtotal: $71.85** (1 line item)

### Peralta 109 / in hand (not ordered)

| **Part Name/Description** | **Qty** | **Unit Cost** | **Total Cost** | **Manufacturer** | **Manufacturer #** | **Vendor Link** | **Datasheet Link** | **Schematic Reference Designators** |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Dual H-bridge motor driver, 12-DIPH-300 with heat-sink fin | 2 | - | - | onsemi (Fairchild) | FAN8100N | - | [Datasheet](https://datasheet.sic-components.com/FAN8100N%2CMTC.pdf) | U1 |
| PIC18F57Q43 Curiosity Nano evaluation board | 1 | - | - | Microchip | DM164150 | - | [Datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/UserGuides/PIC18F57Q43-Curiosity-Nano-HW-UserGuide-DS40002186B.pdf) | A1 |
| Fuse 1 A 250 V, 5 x 20 mm, slow-blow | 3 | - | - | Littelfuse | 0218001.MXP | [Mouser](https://www.mouser.com/en/ProductDetail/Littelfuse/0218001.MXP?qs=RpX4E3T4PRboybtLF01bxg%3D%3D) | [Datasheet](https://www.littelfuse.com/assetdocs/fuse-218-datasheet?assetguid=A96D72B7-5296-4815-88B4-98B2F6738874) | F1 |
| Resistor 1 kOhm 1/4 W 5 %, axial | 6 | - | - | Stackpole | CF14JT1K00 | [Mouser](https://www.mouser.com/c/?q=CF14JT1K00) | [Datasheet](https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf) | R1, R7 |
| Resistor 10 kOhm 1/4 W 5 %, axial | 8 | - | - | Stackpole | CF14JT10K0 | [Mouser](https://www.mouser.com/c/?q=CF14JT10K0) | [Datasheet](https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf) | R2, R3, R5 |
| Resistor 330 Ohm 1/4 W 5 %, axial | 8 | - | - | Stackpole | CF14JT330R | [Mouser](https://www.mouser.com/c/?q=CF14JT330R) | [Datasheet](https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf) | R4, R6, R10 |
| Resistor 100 kOhm 1/4 W 5 %, axial | 6 | - | - | Stackpole | CF14JT100K | [Mouser](https://www.mouser.com/c/?q=CF14JT100K) | [Datasheet](https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf) | R8, R9 |
| Resistor 240 Ohm 1/4 W 1 %, axial | 3 | - | - | Stackpole | RNF14FTD240R | [Mouser](https://www.mouser.com/c/?q=RNF14FTD240R) | [Datasheet](https://www.ibselectronics.biz/datasheet/Misc/RNF14FTD20K0.pdf) | R11 |
| Resistor 910 Ohm 1/4 W 1 %, axial | 3 | - | - | Stackpole | RNF14FTD910R | [Mouser](https://www.mouser.com/c/?q=RNF14FTD910R) | [Datasheet](https://www.ibselectronics.biz/datasheet/Misc/RNF14FTD20K0.pdf) | R12 |
| LED 3 mm green, diffused | 3 | - | - | Kingbright | WP710A10SGD | [Mouser](https://www.mouser.com/ProductDetail/Kingbright/WP710A10SGD?qs=jBF9H7RTBaS5vBvRdVQZww%3D%3D) | [Datasheet](https://www.mouser.fi/datasheet/3/308/1/WP710A10SGD.pdf) | DS1 |
| LED 3 mm yellow, diffused | 3 | - | - | Kingbright | WP710A10YD | [Digi-Key](https://www.digikey.com/en/products/detail/kingbright/WP710A10YD/2769824) | [Datasheet](https://www.digikey.com/en/products/detail/kingbright/WP710A10YD/2769824) | DS2 |
| DIP IC socket, 14 pin, 0.3 in | 2 | - | - | Generic | DIP-14 socket | - | - | U1 (socket) |
| Male breakaway header 1 x 40, 2.54 mm | 1 | - | - | Pololu | item #965 | [Pololu](https://www.pololu.com/product/965) | [Datasheet](https://www.pololu.com/product/965) | J4 + breadboard pins |
| Female header 1 x 40, 2.54 mm | 2 | - | - | Generic | 1 x 40 female header | - | - | A1 (socket) |

These parts are already in hand, handed out in class or taken from Peralta 109 stock, so they are not on a purchase request.

**Total to order: $130.77** (Mouser $58.92 + Pololu $71.85, before shipping and tax).

<!-- BOM:END -->

## Remark

* **C7 (47 uF)** has a 2 mm lead pitch; the PCB footprint will be set to match.
* **Team cable:** one 2 x 4 IDC ribbon cable is listed for the link to the Gripper board. The team will confirm who orders the shared cables so they are not bought twice.

## Resources

* The same BOM as a spreadsheet: [bom.csv](bom.csv)
