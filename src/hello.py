#!/usr/bin/env python3

import matplotlib.pyplot as plt
from mylib import add

# YAML verilerini doğrudan dictionary olarak göm
veriler = {
    'persons': [
        {'name': 'Ahmet', 'age': 25, 'skor': 85},
        {'name': 'Ayşe', 'age': 30, 'skor': 92},
        {'name': 'Mehmet', 'age': 22, 'skor': 78}
    ]
}

print(veriler)

# Typst raporu oluştur
typst_content = """= Kişiler Raporu

#table(
  columns: (1fr, 1fr, 1fr),
  [*İsim*], [*Yaş*], [*Skor*],
"""

for person in veriler['persons']:
    typst_content += f"  [{person['name']}], [{person['age']}], [{person['skor']}],\n"

typst_content += ")\n\n"

# Grafiği figür olarak ekle
typst_content += """#figure(
  image("graf1.svg", width: 80%),
  caption: [Yaşa göre skor verileri]
)
"""

with open('../output/persons_rapor.typ', 'w', encoding='utf-8') as f:
    f.write(typst_content)

print("output/persons_rapor.typ oluşturuldu!")

# Yaşa göre skor bar grafiği oluştur
persons_sorted = sorted(veriler['persons'], key=lambda x: x['age'])
ages = [f"{p['name']} ({p['age']})" for p in persons_sorted]
skors = [p['skor'] for p in persons_sorted]

plt.figure(figsize=(8, 5))
plt.bar(ages, skors, color=['#3498db', '#2ecc71', '#e74c3c'])
plt.xlabel('Yaş')
plt.ylabel('Skor')
plt.title('Yaşa Göre Skorlar')
plt.ylim(0, 100)
for i, v in enumerate(skors):
    plt.text(i, v + 2, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('../output/graf1.svg', format='svg')
print("output/graf1.svg oluşturuldu!")

# now let's use the function
print(add(1, 2))

print("İşler tamamlandı!")