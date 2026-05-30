import pandas as pd
import math

INPUT_CSV = "faz1_cycle_results_clean.csv"   # elindeki en iyi csv adı buysa
OUTPUT_CSV = "faz1_cycle_results_corrected.csv"

EXPECTED_CYCLE_SEC = 7.5
LONG_GAP_FACTOR = 1.8

df = pd.read_csv(INPUT_CSV)

# cycle_time_sec boş olan ilk satırı atıyoruz
df = df.dropna(subset=["cycle_time_sec"]).reset_index(drop=True)

corrected_times = []

for t in df["cycle_time_sec"]:
    t = float(t)

    # Normal süre ise direkt ekle
    if t <= EXPECTED_CYCLE_SEC * LONG_GAP_FACTOR:
        corrected_times.append(t)

    # Uzun boşluk varsa kaç cycle kaçmış olabilir diye böl
    else:
        estimated_cycles = round(t / EXPECTED_CYCLE_SEC)

        if estimated_cycles < 2:
            estimated_cycles = 1

        split_time = t / estimated_cycles

        for _ in range(estimated_cycles):
            corrected_times.append(split_time)

corrected_df = pd.DataFrame({
    "cycle_no": range(1, len(corrected_times) + 1),
    "cycle_time_sec": [round(x, 3) for x in corrected_times]
})

corrected_df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

print("Düzeltme bitti.")
print(f"Ham cycle sayısı: {len(df) + 1}")  # ilk boş cycle dahil
print(f"Düzeltilmiş cycle sayısı: {len(corrected_df)}")
print(f"Ortalama cycle time: {corrected_df['cycle_time_sec'].mean():.3f}")
print(f"Min: {corrected_df['cycle_time_sec'].min():.3f}")
print(f"Max: {corrected_df['cycle_time_sec'].max():.3f}")
print(f"CSV kaydedildi: {OUTPUT_CSV}")