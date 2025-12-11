
# vibe


Bu proje kişi verilerini farklı formatlarda yöneten ve Typst raporu oluşturan bir Python uygulamasıdır.

## Proje Yapısı

```
vibe/
├── src/
│   ├── hello.py          # Ana uygulama scripti
│   └── mylib.py          # Yardımcı fonksiyonlar kütüphanesi
├── data/
│   ├── veriler.yaml      # Kişi verileri (YAML)
│   ├── veriler.json      # Kişi verileri (JSON)
│   └── veriler.csv       # Kişi verileri (CSV)
├── output/
│   ├── persons_rapor.typ # Typst raporu (tablo + grafik)
│   ├── graf1.svg         # Yaşa göre skor bar grafiği
│   └── rapor.typ         # Örnek Typst raporu
├── Makefile              # Otomasyon komutları
├── requirements.txt      # Python bağımlılıkları
└── README.md
```

## Özellikler

### Veri Yönetimi
- Kişi verileri (name, age, skor) YAML, JSON ve CSV formatlarında saklanır
- Python dictionary olarak doğrudan kodda gömülü veriler

### Rapor Oluşturma
- `hello.py` çalıştırıldığında:
  - `output/persons_rapor.typ` Typst raporu oluşturulur
  - `output/graf1.svg` bar grafiği oluşturulur (matplotlib ile)
  - Grafik rapora figür olarak gömülür

### mylib.py Fonksiyonları
- **add(a, b)**: İki sayıyı toplar ve sonucu döndürür

## Kurulum

```bash
# Bağımlılıkları yükle
make install
# veya
pip install -r requirements.txt
```

## Kullanım

```bash
# Ana scripti çalıştır
make run

# Typst dosyalarını PDF'e derle
make pdf

# Her ikisini birden yap
make all

# Oluşturulan dosyaları temizle
make clean
```

### Manuel Kullanım

```bash
cd src && python3 hello.py
typst compile output/persons_rapor.typ output/persons_rapor.pdf
```

## Gereksinimler

- Python 3
- matplotlib
- pyyaml (opsiyonel)
- typst (PDF derlemek için)