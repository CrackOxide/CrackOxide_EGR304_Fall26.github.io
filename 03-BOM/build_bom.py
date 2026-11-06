#!/usr/bin/env python3
"""Single source for the Arm Motion Control BOM.

Edit the ROWS list below, then run (from this folder):
    python3 build_bom.py
It rewrites bom.csv and the table between the BOM markers in BOM.md.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

M = "Mouser Electronics (to order)"
H = "In hand (still used, not ordered again)"
L = "Peralta 109 / class stock (not ordered)"

# vendor, description, refs, qty, unit (USD or None), manufacturer, mfr #, vendor URL, datasheet URL, note
ROWS = [
    (H, "Adjustable linear regulator, 1.5 A, TO-220 (set to 6.0 V for the motor rail)", "VR1", 3, 0.76,
     "STMicroelectronics", "LM317T", "https://www.mouser.com/ProductDetail/STMicroelectronics/LM317T?qs=swDD%2BF%2Bps7c8uLyY%2B3mJJw%3D%3D",
     "https://www.st.com/resource/en/datasheet/lm217.pdf",
     "Replaces the L7806 (obsolete at Mouser). Vout = 1.25 V x (1 + 910/240) = 6.0 V with R11 / R12."),
    (H, "5 V linear regulator, 1.5 A, TO-220", "VR2", 3, 0.60,
     "STMicroelectronics", "L7805CV", "https://www.mouser.com/en/ProductDetail/STMicroelectronics/L7805CV?qs=9NrABl3fj%2FqplZAHiYUxWg%3D%3D",
     "https://www.st.com/resource/en/datasheet/l78.pdf", "Logic rail for the H-bridge VCC and the power LED."),
    (M, "Heat sink, TO-220, channel style, 25.9 C/W", "VR1 (heat sink)", 3, 1.07,
     "Aavid (Boyd)", "577102B00000G", "https://www.mouser.com/ProductDetail/Aavid/577102B00000G?qs=cR7Qvk1oinlekh9MFs6NUA%3D%3D",
     "https://www.mouser.com/datasheet/2/2/Aavid_Board_Level_Heatsinks_Cat_1_-3044572.pdf", "VR1 dissipates up to about 1.6 W at worst case (see Power Budget)."),
    (H, "Schottky diode 1 A 40 V, DO-41 (reverse-polarity protection)", "D1", 3, 0.55,
     "onsemi", "1N5819RLG", "https://www.mouser.com/en/ProductDetail/onsemi/1N5819RLG?qs=y2kkmE52mdN7fhfvNgYV6A%3D%3D",
     "https://www.onsemi.com/pdf/datasheet/1n5817-d.pdf", ""),
    (H, "DC power jack 2.1 x 5.5 mm, PCB mount", "J1", 3, 0.70,
     "Same Sky (CUI)", "PJ-102A", "https://www.mouser.com/en/ProductDetail/Same-Sky/PJ-102A?qs=WyjlAZoYn50UKjtnxOz%2Bqg%3D%3D",
     "https://www.mouser.com/datasheet/3/6118/1/pj_102a.pdf", "Mates with the 9 V adapter plug."),
    (M, "Fuse clip for 5 mm (5 x 20 mm) fuse, PCB mount", "F1 (holder)", 4, 0.33,
     "Keystone Electronics", "3517", "https://www.mouser.com/en/ProductDetail/Keystone-Electronics/3517?qs=qOqV1E1P08RwsK9hgzJijw%3D%3D",
     "https://www.mouser.com/datasheet/3/201/1/3517.PDF", "Two clips per fuse."),
    (H, "Ceramic capacitor 0.33 uF 50 V X7R, radial, 5 mm lead spacing", "C1, C3", 6, 1.02,
     "Vishay BC Components", "K334K20X7RF5TH5", "https://www.mouser.com/ProductDetail/Vishay-BC-Components/K334K20X7RF5TH5?qs=lQAVKuKFhkL6tfc7l6Mmyw%3D%3D",
     "https://www.vishay.com/doc?45171", "Regulator input capacitors."),
    (H, "Ceramic capacitor 0.1 uF 50 V X7R, radial, 5 mm lead spacing", "C2, C4, C5, C6, C8", 12, 0.118,
     "Vishay BC Components", "K104K15X7RF5WH5", "https://www.mouser.com/en/ProductDetail/Vishay-BC-Components/K104K15X7RF5WH5?qs=8fb2TFeI5qGYDjl7%2BWZxcg%3D%3D",
     "https://www.vishay.com/doc?45171", "Regulator outputs, H-bridge bypass, SPEED_SET RC filter."),
    (H, "Aluminum electrolytic 47 uF 16 V, radial 5 x 11 mm", "C7", 3, 0.38,
     "Panasonic", "EEU-FC1C470H", "https://www.mouser.com/ProductDetail/Panasonic/EEU-FC1C470H?qs=/C1U95aQ15vhemYBctOGEw%3D%3D",
     "https://industrial.panasonic.com/cdbs/www-data/pdf/RDF0000/ABA0000C1209.pdf", "Bulk bypass on the 6 V motor rail. 2 mm lead pitch."),
    (H, "Terminal block, 2 position, 5.0 mm pitch", "J2", 2, 0.53,
     "Phoenix Contact", "1935161", "https://www.mouser.com/ProductDetail/Phoenix-Contact/1935161?qs=W3wJikR1%252BS6eKzfFl8Rbew%3D%3D",
     "https://www.mouser.com/datasheet/3/507/9/phoenix_contact_1935161_en.pdf", "Motor + / - wires (no ground)."),
    (L, "Male pin header 2 x 4, 2.54 mm, unshrouded, through hole", "J3", 2, None,
     "Generic", "2 x 4 pin header", "", "", "Team link connector (pin 8 = GND). Two 1 x 4 pieces of breakaway header also fit the footprint."),
    (L, "Female-to-female jumper wire, 2.54 mm Dupont, 20 cm", "Team link", 8, None,
     "Generic", "F-F jumper wire", "", "", "One wire per signal to the Gripper board. Mark pin 1 and use a fixed colour for GND."),
    (M, "Tactile switch 6 x 6 mm, through hole", "SW1", 3, 0.35,
     "Omron", "B3F-1000", "https://www.mouser.com/ProductDetail/Omron-Electronics/B3F-1000?qs=lK7M36XCk6JQHckSc1xIsg%3D%3D",
     "https://www.mouser.com/datasheet/3/39/1/en_b3f.pdf", "Debug button (RE1)."),
    (M, "Test point, miniature PC loop", "TP1-TP3", 4, 0.26,
     "Keystone Electronics", "5001", "https://www.mouser.com/en/ProductDetail/Keystone-Electronics/5001?qs=q0tsjPZWdm%2FW0vdr%2FwowKg%3D%3D",
     "https://www.mouser.com/datasheet/3/201/1/5000_5004.PDF", "+6 V, +5 V and GND probe points (one spare)."),
    (H, "AC/DC wall adapter 9 V 2.55 A, 2.1 x 5.5 mm plug, C14 inlet", "External (J1)", 1, 13.70,
     "MEAN WELL", "GST25A09-P1J", "https://www.mouser.com/en/ProductDetail/MEAN-WELL/GST25A09-P1J?qs=drgMNd%252BkGPP0sFLpGSh7oQ%3D%3D",
     "https://www.meanwellusa.com/webapp/product/search.aspx?prod=GST25A", "System power source."),
    (H, "AC power cord NEMA 5-15P to IEC C13, 6 ft", "External (adapter)", 1, 6.39,
     "Same Sky", "AC-C13-R NA", "https://www.mouser.com/en/ProductDetail/Same-Sky/AC-C13-R-NA?qs=%252BXxaIXUDbq2HADzpjg7LkA%3D%3D",
     "../Appendix/Datasheets/ac-c13-r-na.pdf", "The adapter has a C14 inlet and ships without a cord."),
    (M, "Micro metal DC gearmotor 6 V, 50 rpm, 298:1", "B1 (off-board)", 3, 7.50,
     "DFRobot", "FIT0579", "https://www.mouser.com/ProductDetail/426-FIT0579",
     "https://www.robotshop.com/products/dfrobot-micro-metal-dc-geared-motor-6v-50rpm-250gcm",
     "Arm joint actuator. Stall 2.2 kg-cm, 430 mA max at 6 V. Replaces Pololu #2370 (budget and efficiency)."),
    (L, "Dual H-bridge motor driver, 12-DIPH-300 with heat-sink fin", "U1", 2, None,
     "onsemi (Fairchild)", "FAN8100N", "", "https://datasheet.sic-components.com/FAN8100N%2CMTC.pdf",
     "Already in hand (need 2: breadboard + PCB). Obsolete, so it is not ordered."),
    (L, "PIC18F57Q43 Curiosity Nano evaluation board", "A1", 1, None,
     "Microchip", "DM164150", "", "https://ww1.microchip.com/downloads/aemDocuments/documents/MCU08/ProductDocuments/UserGuides/PIC18F57Q43-Curiosity-Nano-HW-UserGuide-DS40002186B.pdf",
     "Handed out in class."),
    (L, "Fuse 1 A 250 V, 5 x 20 mm, slow-blow", "F1", 3, None,
     "Littelfuse", "0218001.MXP", "https://www.mouser.com/en/ProductDetail/Littelfuse/0218001.MXP?qs=RpX4E3T4PRboybtLF01bxg%3D%3D",
     "https://www.littelfuse.com/assetdocs/fuse-218-datasheet?assetguid=A96D72B7-5296-4815-88B4-98B2F6738874",
     "Peralta fuse stock; Mouser $1.29 if not available."),
    (L, "Resistor 1 kOhm 1/4 W 5 %, axial", "R1, R7", 6, None,
     "Stackpole", "CF14JT1K00", "https://www.mouser.com/c/?q=CF14JT1K00", "https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf", "Peralta stock."),
    (L, "Resistor 10 kOhm 1/4 W 5 %, axial", "R2, R3, R5", 8, None,
     "Stackpole", "CF14JT10K0", "https://www.mouser.com/c/?q=CF14JT10K0", "https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf", "Pull-downs on SAFE_OK, RUN_REQ, OBJ_HELD."),
    (L, "Resistor 330 Ohm 1/4 W 5 %, axial", "R4, R6, R10", 8, None,
     "Stackpole", "CF14JT330R", "https://www.mouser.com/c/?q=CF14JT330R", "https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf", "Series resistors on outputs, debug LED."),
    (L, "Resistor 100 kOhm 1/4 W 5 %, axial", "R8, R9", 6, None,
     "Stackpole", "CF14JT100K", "https://www.mouser.com/c/?q=CF14JT100K", "https://www.mouser.lt/datasheet/3/1099/1/SEI_CF_CFM.pdf", "H-bridge input pull-downs."),
    (L, "Resistor 240 Ohm 1/4 W 1 %, axial", "R11", 3, None,
     "Stackpole", "RNF14FTD240R", "https://www.mouser.com/c/?q=RNF14FTD240R", "https://www.ibselectronics.biz/datasheet/Misc/RNF14FTD20K0.pdf", "LM317 program resistor (top)."),
    (L, "Resistor 910 Ohm 1/4 W 1 %, axial", "R12", 3, None,
     "Stackpole", "RNF14FTD910R", "https://www.mouser.com/c/?q=RNF14FTD910R", "https://www.ibselectronics.biz/datasheet/Misc/RNF14FTD20K0.pdf", "LM317 program resistor (bottom)."),
    (L, "LED 3 mm green, diffused", "DS1", 3, None,
     "Kingbright", "WP710A10SGD", "https://www.mouser.com/ProductDetail/Kingbright/WP710A10SGD?qs=jBF9H7RTBaS5vBvRdVQZww%3D%3D",
     "https://www.mouser.fi/datasheet/3/308/1/WP710A10SGD.pdf", "Power indicator."),
    (L, "LED 3 mm yellow, diffused", "DS2", 3, None,
     "Kingbright", "WP710A10YD", "https://www.digikey.com/en/products/detail/kingbright/WP710A10YD/2769824",
     "../Appendix/Datasheets/WP710A10YD.pdf", "Debug LED (RE0)."),
    (L, "M3 x 8 mm screw, nut and washer (TO-220 to heat sink)", "VR1 (heat sink mounting)", 2, None,
     "Generic", "M3 screw set", "", "", "Peralta stock. The 577102B00000G heat sink has no PCB tabs; it is held by the TO-220 screw. The tab and heat sink are at +6 V."),
    (L, "Male breakaway header 1 x 40, 2.54 mm", "J4, J5 + breadboard pins", 1, None,
     "Pololu", "item #965", "https://www.pololu.com/product/965", "https://www.pololu.com/product/965", "Snap off 6 pins each for J4 and J5."),
    (L, "Female header 1 x 40, 2.54 mm", "A1 (socket)", 2, None,
     "Generic", "1 x 40 female header", "", "", "Peralta stock. Cut to the Curiosity Nano pin rows so the board can be removed."),
]


def money(v):
    if v is None:
        return ""
    return f"${v:,.3f}" if round(v, 2) != round(v, 3) else f"${v:,.2f}"


def link(text, url):
    return f"[{text}]({url})" if url else "-"


def site(url):
    for key, name in (("mouser", "Mouser"), ("pololu", "Pololu"), ("digikey", "Digi-Key")):
        if key in url:
            return name
    return "Link"


def build():
    rows = sorted(ROWS, key=lambda r: [M, H, L].index(r[0]))
    with open(HERE / "bom.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Vendor", "Part Name/Description", "Qty", "Unit Cost (USD)", "Total Cost (USD)", "Manufacturer",
                    "Manufacturer #", "Vendor Link", "Datasheet Link", "Schematic Reference Designators", "Notes"])
        for v, d, refs, q, u, mf, pn, vl, dl, note in rows:
            w.writerow([v, d, q, "" if u is None else f"{u:.2f}", "" if u is None else f"{u * q:.2f}", mf, pn, vl, dl, refs, note])
    out = []
    totals = {}
    for vendor in (M, H, L):
        part = [r for r in rows if r[0] == vendor]
        out.append(f"### {vendor}\n")
        out.append("| **Part Name/Description** | **Qty** | **Unit Cost** | **Total Cost** | **Manufacturer** | **Manufacturer #** "
                   "| **Vendor Link** | **Datasheet Link** | **Schematic Reference Designators** |")
        out.append("|:--|:--|:--|:--|:--|:--|:--|:--|:--|")
        t = 0.0
        for v, d, refs, q, u, mf, pn, vl, dl, note in part:
            tot = None if u is None else u * q
            t += tot or 0
            out.append(f"| {d} | {q} | {money(u) or '-'} | {money(tot) or '-'} | {mf} | {pn} | "
                       f"{link(site(vl), vl)} | {link('Datasheet', dl)} | {refs} |")
        totals[vendor] = t
        if vendor == M:
            out.append(f"\n**Mouser order subtotal: ${t:,.2f}** ({len(part)} line items, on the Mouser purchase request)\n")
        elif vendor == H:
            out.append(f"\nThese parts are already in hand. They are still used in the design but are not ordered again. "
                       f"Value at the listed Mouser prices: ${t:,.2f}.\n")
        else:
            out.append("\nThese parts are handed out in class or taken from Peralta 109 stock, so they are not on a purchase request.\n")
    grand = totals[M]
    out.append(f"**Total to order: ${grand:,.2f}** (one Mouser purchase request, before shipping and tax). "
               f"Total value of all purchased parts, including those in hand: ${totals[M] + totals[H]:,.2f}.\n")
    page = (HERE / "BOM.md").read_text(encoding="utf-8")
    a, b = "<!-- BOM:START -->", "<!-- BOM:END -->"
    head, rest = page.split(a, 1)
    _, tail = rest.split(b, 1)
    (HERE / "BOM.md").write_text(f"{head}{a}\n" + "\n".join(out) + f"\n{b}{tail}", encoding="utf-8")
    print(f"order ${totals[M]:.2f}, in hand ${totals[H]:.2f}")


if __name__ == "__main__":
    build()
