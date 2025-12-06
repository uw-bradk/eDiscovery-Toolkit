# excel_to_loadfile.py
# Turns any Excel export into perfect OPT + DAT in < 2 minutes

import pandas as pd
import os

input_file = "sample_data/messy_export.xlsx"
df = pd.read_excel(input_file)

# Standardize column names (common messy variations)
df = df.rename(columns=lambda x: x.strip().upper())
df = df.rename(columns={
    "BEGDOC": "BEGDOC", "ENDDOC": "ENDDOC", "BEGATTACH": "BEGATTACH", "ENDATTACH": "ENDATTACH",
    "CUSTODIAN": "CUSTODIAN", "FILEPATH": "NATIVELINK", "FOLDER": "FOLDER"
})

# Fill missing families
df["BEGATTACH"] = df["BEGATTACH"].fillna(df["BEGDOC"])
df["ENDATTACH"] = df["ENDATTACH"].fillna(df["ENDDOC"])

# Create DAT (Concordance default: ¶20 delimiter, þ quote)
dat_path = "sample_data/output_concordance.dat"
df.to_csv(dat_path, sep="¶", index=False, encoding="utf-8", line_terminator="\n", quotechar="þ")

# Create OPT (image load file pointer)
opt_lines = []
for _, row in df.iterrows():
    if pd.notna(row.get("NATIVELINK")):
        opt_lines.append(f"@{row['NATIVELINK']}\n@IMAGES\\{row['BEGDOC']}.tif")

with open("sample_data/output_images.opt", "w", encoding="utf-8") as f:
    f.write("\n".join(opt_lines))

print("Load files created!")
print("   → output_concordance.dat")
print("   → output_images.opt")
