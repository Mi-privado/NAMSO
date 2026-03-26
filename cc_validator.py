from datetime import datetime

def luhn_check(card_number):
    """Algoritmo Luhn"""
    card = ''.join(filter(str.isdigit, str(card_number)))
    if len(card) < 13 or len(card) > 19:
        return False
    
    digits = [int(d) for d in card[::-1]]
    total = 0
    
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    
    return total % 10 == 0


def get_card_type(card_number):
    card = ''.join(filter(str.isdigit, str(card_number)))
    if card.startswith('4'):
        return "VISA"
    elif card.startswith(('51','52','53','54','55')):
        return "MASTERCARD"
    else:
        return "UNKNOWN"


# ================== TUS TARJETAS ==================
cards = [
    "4207670324504961|08|2028|363",
    "4207670324994410|08|2028|546",
    "4207670324528580|08|2028|118",
    "4207670324038200|08|2028|588",
    "4207670324003725|08|2028|852",
    "4207670324425167|08|2028|714",
    "4207670324122624|08|2028|843",
    "4207670324809485|08|2028|189",
    "4207670324103590|08|2028|136",
    "4207670324952467|08|2028|363"
]
# ================================================

print("=" * 80)
print("          LIVE CARD VALIDATOR PRO v2.0")
print("          " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("=" * 80)

live_count = 0
died_count = 0
lives_list = []

for i, line in enumerate(cards, 1):
    parts = line.split('|')
    if len(parts) < 4:
        print(f"[{i:2d}] ❌ Formato inválido")
        continue
    
    number = parts[0].strip()
    month = parts[1].strip()
    year = parts[2].strip()
    cvv = parts[3].strip()
    
    if luhn_check(number):
        card_type = get_card_type(number)
        print(f"[{i:2d}] ✅ LIVE  | {number} | {month}/{year} | {cvv} | {card_type}")
        live_count += 1
        lives_list.append(line)
    else:
        print(f"[{i:2d}] ❌ DIED  | {number} | {month}/{year} | {cvv}")
        died_count += 1

print("\n" + "=" * 80)
print("RESUMEN FINAL")
print("=" * 80)
print(f"Total procesadas : {len(cards)}")
print(f"✅ LIVE           : {live_count}")
print(f"❌ DIED           : {died_count}")
if len(cards) > 0:
    print(f"Porcentaje LIVE   : {round((live_count / len(cards)) * 100, 2)}%")
print("=" * 80)

# Guardar LIVEs en archivo
if live_count > 0:
    with open("lives.txt", "w", encoding="utf-8") as f:
        f.write(f"LIVES - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        for live in lives_list:
            f.write(live + "\n")
    print(f"\n✅ Las tarjetas LIVE se guardaron en: lives.txt")
else:
    print("\nNo se encontraron LIVEs.")

print("\nListo.")