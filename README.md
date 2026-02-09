# GitHub Natural Contribution Backfill

Tool sederhana untuk mengisi contribution GitHub secara natural (1-3 commit per hari dengan waktu random).

## Cara Pakai

1. Clone repo kosong atau repo testing kamu
2. Masuk ke folder repo tersebut
3. Copy file `backfill.py` ke dalam repo
4. Jalankan:

```
python3 backfill.py
```

5. Setelah selesai:

```
git push origin main
```

## Konfigurasi

Edit bagian CONFIG di dalam file `backfill.py`:

- DAYS_BACK = berapa hari ke belakang ingin diisi
- MIN_COMMITS = minimal commit per hari
- MAX_COMMITS = maksimal commit per hari

## Penting

Pastikan email git kamu sudah sesuai dengan email GitHub:

```
git config user.email
```

Jika belum:

```
git config --global user.email "emailkamu@gmail.com"
```
