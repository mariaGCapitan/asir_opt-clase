# Reto 2 — Conversor de bytes.
# Dada una cantidad de bytes, mostrarla en KB, MB y GB con dos decimales y separador de miles.

bytes_total = 734003200

kb = bytes_total / 1024
mb = kb / 1024
gb = mb / 1024

print(f"{bytes_total:,} bytes son:")
print(f"  {kb:,.2f} KB")
print(f"  {mb:,.2f} MB")
print(f"  {gb:,.2f} GB")
