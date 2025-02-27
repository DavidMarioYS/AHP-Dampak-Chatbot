# -*- coding: utf-8 -*-
"""AHP - Dampak Chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YFdfRxcuLR2ucQSd5pYbUQC0muVGPXAB

## Data Wrangling
"""

from google.colab import files

# Mengunggah file dari komputer lokal
uploaded = files.upload()

# Menyimpan file yang diunggah ke dalam file lokal di Colab
with open('KuesionerAHP.csv', 'wb') as f:
    f.write(uploaded['KuesionerAHP.csv'])

import pandas as pd

# Load Dataset
df = pd.read_csv('./KuesionerAHP.csv')

df

# Display basic information about the dataset
dataset_info = df.info()

# Check for missing values in the dataset
missing_values = df.isnull().sum()
missing_values

# Summary statistics of the numerical columns
summary_statistics = df.describe()
summary_statistics

# Count the number of occurrences of each unique value in categorical columns
value_counts = df.nunique()
value_counts

# Distribution of responses for numerical columns
distribution_responses = df.describe(include=[int, float])
distribution_responses

# Distribution of responses for categorical columns
categorical_distribution = df.describe(include=[object])
categorical_distribution

# Count occurrences of each unique value in the numerical columns for visualization
numerical_value_counts = {}
for col in df.select_dtypes(include=[int, float]).columns:
    numerical_value_counts[col] = df[col].value_counts()

numerical_value_counts

# prompt: Visualiasasi dari setiap jumlah value yang dimiliki

import matplotlib.pyplot as plt

# Visualisasi untuk kolom numerik
for col, counts in numerical_value_counts.items():
  plt.figure(figsize=(8, 6))
  plt.bar(counts.index, counts.values)
  plt.title(f'Distribution of {col}')
  plt.xlabel(col)
  plt.ylabel('Frequency')
  plt.show()

# Visualisasi untuk kolom kategorikal
for col in df.select_dtypes(include=[object]).columns:
  plt.figure(figsize=(8, 6))
  df[col].value_counts().plot(kind='bar')
  plt.title(f'Distribution of {col}')
  plt.xlabel(col)
  plt.ylabel('Frequency')
  plt.show()

"""## **Identifikasi Kriteria dan Sub-Kriteria**


- [K1] Pengetahuan dan Penggunaan Chatbot
  - [SK1] Apakah Anda mengetahui Chatbot AI?
    - (Ya/Tidak)
  - [SK2] Apakah Anda pernah menggunakan Chatbot AI khususnya pada saat pembelajaran dalam jaringan (online)?
    - (Ya/Tidak)
- [K2] Efektivitas Chatbot
  - [SK1] Seberapa efektif Chatbot dalam meningkatkan interaktivitas dan hasil belajar mahasiswa?
    - (Skala 1-10)
  - [SK2] Seberapa efektif menurut Anda penggunaan Chatbot dalam memberikan bantuan dan dukungan kepada mahasiswa dalam menjawab pertanyaan atau mengatasi kesulitan selama proses belajar?
    - (Skala 1-10)
- [K3] Kemudahan dan Kepuasan Penggunaan
  - [SK1] Seberapa mudah mahasiswa menggunakan Chatbot sebagai alat pembelajaran?
    - (Skala 1-10)
  - [SK2] Seberapa puas mahasiswa dengan penggunaan Chatbot dalam proses pembelajaran?
    - (Skala 1-10)
- [K4] Relevansi Dukungan Chatbot
  - [SK1] Sejauh mana Chatbot memberikan dukungan yang relevan terhadap materi pembelajaran?
   - (Skala 1-10)
  - [SK2] Apa pendapat Anda tentang penggunaan Chatbot dalam meningkatkan hasil belajar mahasiswa?
    - (Skala 1-10)
- [K5] Interaktivitas dan Partisipasi
  - [SK1] Apa pendapat Anda tentang penggunaan Chatbot dalam meningkatkan interaktivitas pada saat belajar dalam jaringan?
    - (Skala 1-10)
  - [SK2] Menurut Anda, sejauh mana penggunaan Chatbot dapat meningkatkan partisipasi mahasiswa dalam proses pembelajaran?
    - (Skala 1-10)
- [K6] Ketergantungan dan Motivasi
  - [SK1] Apakah Anda berpendapat bahwa penggunaan Chatbot dapat menyebabkan siswa mengandalkan terlalu banyak pada teknologi dan mengurangi kemampuan mereka untuk mengembangkan keterampilan sosial interpersonal?
    - (Skala 1-10)
  - [SK2] Bagaimana Anda menilai kemungkinan terjadinya ketergantungan siswa terhadap Chatbot dalam proses pembelajaran?
    - (Skala 1-10)
  - [SK3] Sejauh mana Anda percaya bahwa penggunaan Chatbot dapat mengurangi motivasi siswa untuk berpartisipasi aktif dalam diskusi dan interaksi kelas?
    - (Skala 1-10)
  - [SK3] Sejauh mana Anda percaya bahwa ketersediaan Chatbot yang memberikan jawaban secara instan dapat membuat siswa malas dan enggan untuk berusaha lebih keras dalam mencari pemahaman yang mendalam?
    - (Skala 1-10)

**Keterangan Nilai pada matriks berpasangan:**
  - 1: Kriteria di baris dianggap sama pentingnya dengan kriteria di kolom.
  - '> 1': Kriteria di baris dianggap lebih penting dibandingkan kriteria di kolom.
  - '< 1': Kriteria di baris dianggap kurang penting dibandingkan kriteria di kolom.
  - Angka dalam bentuk pecahan (misalnya 1/3): Mengindikasikan seberapa kurang penting kriteria di baris dibandingkan kriteria di kolom.

Catatan:
- Nilai pada diagonal utama adalah 1 (karena perbandingan terhadap dirinya sendiri).
- Nilai di atas diagonal utama adalah nilai perbandingan (misalnya, "2" berarti kriteria di baris lebih penting daripada kriteria di kolom).
- Nilai di bawah diagonal utama adalah invers dari nilai di atas diagonal utama (misalnya, "0.5" adalah invers dari "2").

Daftar Indeks Konsistensi Acak (Random Consistency Index, RCI) adalah nilai-nilai yang digunakan untuk menghitung rasio konsistensi dalam Analytic Hierarchy Process (AHP). Nilai-nilai RCI bervariasi berdasarkan ukuran matriks. Berikut adalah tabel informasi yang berisi nilai RCI untuk berbagai ukuran matriks:

| Ukuran Matriks (n) | Indeks Konsistensi Acak (RCI) |
|---------------------|-------------------------------|
| 1                   | 0.00                          |
| 2                   | 0.00                          |
| 3                   | 0.58                          |
| 4                   | 0.90                          |
| 5                   | 1.12                          |
| 6                   | 1.24                          |
| 7                   | 1.32                          |
| 8                   | 1.41                          |
| 9                   | 1.45                          |
| 10                  | 1.49                          |
| 11                  | 1.51                          |
| 12                  | 1.48                          |
| 13                  | 1.56                          |
| 14                  | 1.57                          |
| 15                  | 1.59                          |

Nilai-nilai RCI ini digunakan untuk menghitung rasio konsistensi (CR) dalam AHP. Rasio konsistensi dihitung dengan rumus:

$$ [ \text{CR} = \frac{\text{CI}}{\text{RI}} ] $$

Di mana:
- CI adalah Indeks Konsistensi (Consistency Index), dihitung sebagai $$( \text{CI} = \frac{\lambda_{\text{max}} - n}{n - 1} )$$
- RI adalah Indeks Konsistensi Acak (Random Consistency Index) dari tabel di atas
- $$( \lambda_{\text{max}})$$ adalah nilai eigen maksimum dari matriks perbandingan berpasangan
- n adalah ukuran matriks (jumlah kriteria)

Jika rasio konsistensi (CR) kurang dari 0.1 (10%), maka matriks dianggap konsisten; jika lebih besar dari 0.1, matriks dianggap tidak konsisten dan perlu ditinjau kembali.

## Perhitungan Kriteria
"""

import numpy as np

# Matriks perbandingan berpasangan
matrix = np.array([
    [1, 2, 0.33333333, 0.5, 1, 2],
    [0.5, 1, 0.25, 0.33333333, 0.5, 1],
    [3, 4, 1, 2, 1.5, 3],
    [2, 3, 0.5, 1, 1, 2],
    [1, 2, 0.66666667, 1, 1, 1],
    [0.5, 1, 0.33333333, 0.5, 1, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan:")
print(matrix)

# Langkah 1: Normalisasi matriks
col_sum = np.sum(matrix, axis=0)
normalized_matrix = matrix / col_sum

# Menampilkan hasil
print("Normalisasi matriks: {}")
print(normalized_matrix)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities = np.mean(normalized_matrix, axis=1)

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks
weighted_sum_vector = np.dot(matrix, priorities)
lambda_max = np.mean(weighted_sum_vector / priorities)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max}")

# Langkah 4: Menghitung Consistency Index (CI)
n = matrix.shape[0]
CI = (lambda_max - n) / (n - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI}")

# Langkah 5: Menghitung Consistency Ratio (CR)
RI = 1.24  # Nilai dari tabel Index Random Consistency untuk n = 6
CR = CI / RI

# Menampilkan hasil
print(f"Nilai CR: {CR}")

# Menampilkan kondisi konsistensi
if CR <= 0.1:
    print("\nPerhitungan KONSISTEN")
else:
    print("\nPerhitungan Tidak Konsisten")

"""## Perhitungan Sub Kriteria

### Sub Kriteria K1
"""

# Matriks perbandingan berpasangan untuk subkriteria K1
matrix_k1 = np.array([
    [1, 2],
    [1/2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K1:")
print(matrix_k1)

# Langkah 1: Normalisasi matriks
col_sum_k1 = np.sum(matrix_k1, axis=0)
normalized_matrix_k1 = matrix_k1 / col_sum_k1

# Menampilkan hasil
print("Normalisasi matriks Sub-K1: {}")
print(normalized_matrix_k1)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k1 = np.mean(normalized_matrix_k1, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k1)
priorities_k1_adjusted = priorities_k1 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k1, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K1:")
for i, priority in enumerate(priorities_k1_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k1
weighted_sum_vector_k1 = np.dot(matrix_k1, priorities_k1)
lambda_max_k1 = np.mean(weighted_sum_vector_k1 / priorities_k1)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k1}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k1
n_k1 = matrix_k1.shape[0]
CI_k1 = (lambda_max_k1 - n_k1) / (n_k1 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k1}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k1
RI_k1 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k1 = CI_k1 / RI_k1 if RI_k1 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k1}")

# Menampilkan kondisi konsistensi
if CR_k1 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

"""### Sub Kriteria K2"""

# Matriks perbandingan berpasangan untuk subkriteria k2
matrix_k2 = np.array([
    [1, 2],
    [1/2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K2:")
print(matrix_k2)

# Langkah 1: Normalisasi matriks
col_sum_k2 = np.sum(matrix_k2, axis=0)
normalized_matrix_k2 = matrix_k2 / col_sum_k2

# Menampilkan hasil
print("Normalisasi matriks Sub-K2: {}")
print(normalized_matrix_k2)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k2 = np.mean(normalized_matrix_k2, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k2)
priorities_k2_adjusted = priorities_k2 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k2, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K2:")
for i, priority in enumerate(priorities_k2_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k2
weighted_sum_vector_k2 = np.dot(matrix_k2, priorities_k2)
lambda_max_k2 = np.mean(weighted_sum_vector_k2 / priorities_k2)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k2}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k2
n_k2 = matrix_k2.shape[0]
CI_k2 = (lambda_max_k2 - n_k2) / (n_k2 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k2}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k2
RI_k2 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k2 = CI_k2 / RI_k2 if RI_k2 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k2}")

# Menampilkan kondisi konsistensi
if CR_k2 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

"""### Sub Kriteria K3"""

# Matriks perbandingan berpasangan untuk subkriteria k3
matrix_k3 = np.array([
    [1, 1/2],
    [2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K3:")
print(matrix_k3)

# Langkah 1: Normalisasi matriks
col_sum_k3 = np.sum(matrix_k3, axis=0)
normalized_matrix_k3 = matrix_k3 / col_sum_k3

# Menampilkan hasil
print("Normalisasi matriks Sub-K3: {}")
print(normalized_matrix_k3)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k3 = np.mean(normalized_matrix_k3, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k3)
priorities_k3_adjusted = priorities_k3 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k3, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K3:")
for i, priority in enumerate(priorities_k3_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k3
weighted_sum_vector_k3 = np.dot(matrix_k3, priorities_k3)
lambda_max_k3 = np.mean(weighted_sum_vector_k3 / priorities_k3)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k3}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k3
n_k3 = matrix_k3.shape[0]
CI_k3 = (lambda_max_k3 - n_k3) / (n_k3 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k3}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k3
RI_k3 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k3 = CI_k3 / RI_k3 if RI_k3 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k3}")

# Menampilkan kondisi konsistensi
if CR_k3 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

"""### Sub Kriteria K4"""

# Matriks perbandingan berpasangan untuk subkriteria k4
matrix_k4 = np.array([
    [1, 1/2],
    [2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K4:")
print(matrix_k4)

# Langkah 1: Normalisasi matriks
col_sum_k4 = np.sum(matrix_k4, axis=0)
normalized_matrix_k4 = matrix_k4 / col_sum_k4

# Menampilkan hasil
print("Normalisasi matriks Sub-K4: {}")
print(normalized_matrix_k4)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k4 = np.mean(normalized_matrix_k4, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k4)
priorities_k4_adjusted = priorities_k4 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k4, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K4:")
for i, priority in enumerate(priorities_k4_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k4
weighted_sum_vector_k4 = np.dot(matrix_k4, priorities_k4)
lambda_max_k4 = np.mean(weighted_sum_vector_k4 / priorities_k4)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k4}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k4
n_k4 = matrix_k4.shape[0]
CI_k4 = (lambda_max_k4 - n_k4) / (n_k4 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k4}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k4
RI_k4 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k4 = CI_k4 / RI_k4 if RI_k4 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k4}")

# Menampilkan kondisi konsistensi
if CR_k4 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

"""### Sub Kriteria K5"""

# Matriks perbandingan berpasangan untuk subkriteria k5
matrix_k5 = np.array([
    [1, 2],
    [1/2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K5:")
print(matrix_k5)

# Langkah 1: Normalisasi matriks
col_sum_k5 = np.sum(matrix_k5, axis=0)
normalized_matrix_k5 = matrix_k5 / col_sum_k5

# Menampilkan hasil
print("Normalisasi matriks Sub-K5: {}")
print(normalized_matrix_k5)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k5 = np.mean(normalized_matrix_k5, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k5)
priorities_k5_adjusted = priorities_k5 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k5, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K5:")
for i, priority in enumerate(priorities_k5_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k5
weighted_sum_vector_k5 = np.dot(matrix_k5, priorities_k5)
lambda_max_k5 = np.mean(weighted_sum_vector_k5 / priorities_k5)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k5}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k5
n_k5 = matrix_k5.shape[0]
CI_k5 = (lambda_max_k5 - n_k5) / (n_k5 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k5}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k5
RI_k5 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k5 = CI_k5 / RI_k5 if RI_k5 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k5}")

# Menampilkan kondisi konsistensi
if CR_k5 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

"""### Sub Kriteria K6"""

# Matriks perbandingan berpasangan untuk subkriteria k6
matrix_k6 = np.array([
    [1, 2, 1/3, 1/2],
    [1/2, 1, 1/4, 1/2],
    [3, 4, 1, 2],
    [2, 2, 1/2, 1]
])

# Menampilkan hasil
print("Matriks perbandingan berpasangan Sub-K6:")
print(matrix_k6)

# Langkah 1: Normalisasi matriks
col_sum_k6 = np.sum(matrix_k6, axis=0)
normalized_matrix_k6 = matrix_k6 / col_sum_k6

# Menampilkan hasil
print("Normalisasi matriks Sub-K6: {}")
print(normalized_matrix_k6)

# Langkah 2: Menghitung vektor prioritas (rata-rata baris)
priorities_k6 = np.mean(normalized_matrix_k6, axis=1)
# Menghitung vektor prioritas subkriteria
max_priority = np.max(priorities_k6)
priorities_k6_adjusted = priorities_k6 / max_priority

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities_k6, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K6:")
for i, priority in enumerate(priorities_k6_adjusted, start=1):
    print(f"K{i}: {priority}")

# Langkah 3: Menghitung lambda maks untuk k6
weighted_sum_vector_k6 = np.dot(matrix_k6, priorities_k6)
lambda_max_k6 = np.mean(weighted_sum_vector_k6 / priorities_k6)

# Menampilkan hasil
print(f"Nilai lambda maks: {lambda_max_k6}")

# Langkah 4: Menghitung Consistency Index (CI) untuk k6
n_k6 = matrix_k6.shape[0]
CI_k6 = (lambda_max_k6 - n_k6) / (n_k6 - 1)

# Menampilkan hasil
print(f"Nilai CI: {CI_k6}")

# Langkah 5: Menghitung Consistency Ratio (CR) untuk k6
RI_k6 = 0  # Untuk n = 2, RI = 0 berdasarkan tabel Random Consistency Index
CR_k6 = CI_k6 / RI_k6 if RI_k6 != 0 else 0

# Menampilkan hasil
print(f"Nilai CR: {CR_k6}")

# Menampilkan kondisi konsistensi
if CR_k6 <= 0.1:
    print("Perhitungan Konsisten")
else:
    print("Perhitungan Tidak Konsisten")

# Menampilkan hasil
print(f"Prioritas:")
for i, priority in enumerate(priorities, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K1:")
for i, priority in enumerate(priorities_k1_adjusted, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K2:")
for i, priority in enumerate(priorities_k2_adjusted, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K3:")
for i, priority in enumerate(priorities_k3_adjusted, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K4:")
for i, priority in enumerate(priorities_k4_adjusted, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K5:")
for i, priority in enumerate(priorities_k5_adjusted, start=1):
    print(f"K{i}: {priority}")

print(f"\nPrioritas Sub-K6:")
for i, priority in enumerate(priorities_k6_adjusted, start=1):
    print(f"K{i}: {priority}")

"""### Perhitungan Alternative"""

import numpy as np

# Fungsi untuk menghitung prioritas dari matriks perbandingan berpasangan
def calculate_priorities(matrix):
    col_sum = np.sum(matrix, axis=0)
    normalized_matrix = matrix / col_sum
    priorities = np.mean(normalized_matrix, axis=1)
    return priorities

# Matriks perbandingan berpasangan untuk setiap sub-kriteria
sub_criteria_matrices = {
    "K1": np.array([[1, 2], [0.5, 1]]),
    "K2": np.array([[1, 2], [0.5, 1]]),
    "K3": np.array([[1, 0.5], [2, 1]]),
    "K4": np.array([[1, 0.5], [2, 1]]),
    "K5": np.array([[1, 2], [0.5, 1]]),
    "K6": np.array([
        [1, 0.35051663192241456, 0.22960663464152994, 0.5407867307169402],
        [2.8512756, 1, 0.655269, 1.5439231],
        [4.3518595, 1.5251132, 1, 2.3551432],
        [1.8495041, 0.647751, 0.424479, 1]
    ])
}

# Perhitungan prioritas untuk setiap sub-kriteria
sub_criteria_priorities = {}
for key, matrix in sub_criteria_matrices.items():
    sub_criteria_priorities[key] = calculate_priorities(matrix)

# Menampilkan prioritas sub-kriteria
for key, priorities in sub_criteria_priorities.items():
    print(f"Prioritas untuk sub-kriteria {key}: {priorities}")

# Prioritas kriteria
criteria_priorities = {
    "K1": 0.1412284879525525,
    "K2": 0.07772291513986818,
    "K3": 0.32200277210027134,
    "K4": 0.1995163433150929,
    "K5": 0.15820483969350876,
    "K6": 0.10132464179870632
}

# Matriks nilai alternatif terhadap sub-kriteria
alternatives = {
    "K1": np.array([[1, 0.5], [0.5, 1]]),
    "K2": np.array([[1, 0.5], [0.5, 1]]),
    "K3": np.array([[0.5, 1], [1, 0.5]]),
    "K4": np.array([[0.5, 1], [1, 0.5]]),
    "K5": np.array([[1, 0.5], [0.5, 1]]),
    "K6": np.array([
        [0.35051663192241456, 0.22960663464152994, 1, 0.5407867307169402],
        [0.655269, 0.424479, 1, 0.424479],
        [0.424479, 0.655269, 1, 0.655269],
        [1, 0.424479, 0.424479, 0.22960663464152994]
    ])
}

# Menghitung prioritas alternatif untuk setiap sub-kriteria
alternative_priorities = {}
for key, matrix in alternatives.items():
    alternative_priorities[key] = calculate_priorities(matrix)

print("\n")

# Menampilkan prioritas alternatif
for key, priorities in alternative_priorities.items():
    print(f"Prioritas alternatif untuk sub-kriteria {key}: {priorities}")

# Menggabungkan prioritas sub-kriteria dan kriteria untuk menghitung nilai akhir alternatif
final_scores = {}
for key, priorities in alternative_priorities.items():
    sub_priorities = sub_criteria_priorities[key]
    criteria_weight = criteria_priorities[key]
    final_scores[key] = np.dot(sub_priorities, criteria_weight)

print("\n")

# Menampilkan nilai akhir alternatif
for key, score in final_scores.items():
    print(f"Nilai akhir untuk kriteria {key}: {score}")

"""### Prioritas untuk Sub-Kriteria
Prioritas ini menunjukkan bobot relatif dari setiap sub-kriteria dalam setiap kriteria utama. Nilai ini dihitung berdasarkan matriks perbandingan berpasangan untuk masing-masing sub-kriteria.

#### K1: Pengetahuan dan Penggunaan Chatbot
- **SK1 (Apakah Anda mengetahui Chatbot AI?):** 0.66666667
- **SK2 (Apakah Anda pernah menggunakan Chatbot AI khususnya pada saat pembelajaran dalam jaringan (online)?):** 0.33333333

#### K2: Efektivitas Chatbot
- **SK1 (Seberapa efektif Chatbot dalam meningkatkan interaktivitas dan hasil belajar mahasiswa?):** 0.66666667
- **SK2 (Seberapa efektif menurut Anda penggunaan Chatbot dalam memberikan bantuan dan dukungan kepada mahasiswa dalam menjawab pertanyaan atau mengatasi kesulitan selama proses belajar?):** 0.33333333

#### K3: Kemudahan dan Kepuasan Penggunaan
- **SK1 (Seberapa mudah mahasiswa menggunakan Chatbot sebagai alat pembelajaran?):** 0.33333333
- **SK2 (Seberapa puas mahasiswa dengan penggunaan Chatbot dalam proses pembelajaran?):** 0.66666667

#### K4: Relevansi Dukungan Chatbot
- **SK1 (Sejauh mana Chatbot memberikan dukungan yang relevan terhadap materi pembelajaran?):** 0.33333333
- **SK2 (Apa pendapat Anda tentang penggunaan Chatbot dalam meningkatkan hasil belajar mahasiswa?):** 0.66666667

#### K5: Interaktivitas dan Partisipasi
- **SK1 (Apa pendapat Anda tentang penggunaan Chatbot dalam meningkatkan interaktivitas pada saat belajar dalam jaringan?):** 0.66666667
- **SK2 (Menurut Anda, sejauh mana penggunaan Chatbot dapat meningkatkan partisipasi mahasiswa dalam proses pembelajaran?):** 0.33333333

#### K6: Ketergantungan dan Motivasi
- **SK1 (Apakah Anda berpendapat bahwa penggunaan Chatbot dapat menyebabkan siswa mengandalkan terlalu banyak pada teknologi dan mengurangi kemampuan mereka untuk mengembangkan keterampilan sosial interpersonal?):** 0.099449
- **SK2 (Bagaimana Anda menilai kemungkinan terjadinya ketergantungan siswa terhadap Chatbot dalam proses pembelajaran?):** 0.28375385
- **SK3 (Sejauh mana Anda percaya bahwa penggunaan Chatbot dapat mengurangi motivasi siswa untuk berpartisipasi aktif dalam diskusi dan interaksi kelas?):** 0.43293151
- **SK4 (Sejauh mana Anda percaya bahwa ketersediaan Chatbot yang memberikan jawaban secara instan dapat membuat siswa malas dan enggan untuk berusaha lebih keras dalam mencari pemahaman yang mendalam?):** 0.18386563

### Prioritas Alternatif untuk Sub-Kriteria
Nilai prioritas ini menunjukkan bobot relatif dari setiap alternatif dalam sub-kriteria yang bersangkutan. Karena semua sub-kriteria memiliki dua alternatif (ya/tidak atau skala), nilai prioritas untuk dua alternatif adalah sama.

### Nilai Akhir untuk Kriteria
Nilai akhir ini adalah hasil perkalian dari bobot kriteria utama dengan bobot sub-kriteria dan prioritas alternatif.

#### K1: Pengetahuan dan Penggunaan Chatbot
- **Alternatif 1:** 0.09415233
- **Alternatif 2:** 0.04707616

#### K2: Efektivitas Chatbot
- **Alternatif 1:** 0.05181528
- **Alternatif 2:** 0.02590764

#### K3: Kemudahan dan Kepuasan Penggunaan
- **Alternatif 1:** 0.10733426
- **Alternatif 2:** 0.21466851

#### K4: Relevansi Dukungan Chatbot
- **Alternatif 1:** 0.06650545
- **Alternatif 2:** 0.1330109

#### K5: Interaktivitas dan Partisipasi
- **Alternatif 1:** 0.10546989
- **Alternatif 2:** 0.05273495

#### K6: Ketergantungan dan Motivasi
- **Alternatif 1:** 0.01007663
- **Alternatif 2:** 0.02875126
- **Alternatif 3:** 0.04386663
- **Alternatif 4:** 0.01863012

### Interpretasi Nilai Akhir
- **K1:** Nilai lebih tinggi pada alternatif 1 menunjukkan bahwa responden cenderung lebih mengetahui Chatbot AI daripada menggunakannya secara khusus dalam pembelajaran daring.
- **K2:** Efektivitas Chatbot dalam interaktivitas dan hasil belajar lebih diutamakan dibandingkan bantuan dan dukungan selama pembelajaran.
- **K3:** Kepuasan penggunaan Chatbot lebih tinggi dibandingkan dengan kemudahan penggunaannya.
- **K4:** Dukungan Chatbot terhadap materi pembelajaran lebih relevan dibandingkan dengan peningkatan hasil belajar.
- **K5:** Chatbot lebih berperan dalam meningkatkan interaktivitas dibandingkan partisipasi mahasiswa.
- **K6:** Ketergantungan terhadap teknologi dan pengurangan motivasi memiliki bobot lebih tinggi dibandingkan faktor lainnya.

Keseluruhan hasil menunjukkan bahwa meskipun Chatbot memiliki beberapa manfaat, terdapat kekhawatiran yang cukup signifikan terhadap ketergantungan dan pengurangan motivasi siswa dalam penggunaan Chatbot dalam pembelajaran.
"""