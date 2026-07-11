# UK Energy Gap

A look at how UK electricity generation has shifted since 2000, and what it's cost to manage the handover from gas to offshore wind.

Built from public data published by DESNZ (the UK government department for energy) and NESO (the electricity system operator), covering:

- **Generation** by fuel type, quarterly, 2000-2026
- **Installed capacity** by fuel type, quarterly, 2000-2026
- **Capacity factor**, calculated from the above
- **Grid constraint/curtailment costs**, quarterly, 2017-2026 (the cost of paying wind farms to reduce output and gas plants to increase output to compensate)

## Files

| File | What it is |
|---|---|
| `UK_Electricity_Generation_and_Capacity_Factor.xlsx` | The full dataset. Five sheets: a Cover sheet documenting every data source, correction, and known limitation; Generation, Capacity, and Capacity Factor sheets (quarterly, 2000-2026); and a Curtailment Costs sheet (quarterly, 2017-2026). |
| `build_chart.py` | The Python script that generates the chart below directly from the workbook. |
| `gas_gap_wind_curtailment_chart.png` | The output chart. |

## The chart

Three panels:

1. UK generation mix by fuel type, 2000-2025
2. Growth in unused gas capacity since 2000, a gap that opens as gas capacity stays roughly flat while it's used less and less
3. Offshore wind generation vs. grid constraint cost, annual totals, 2017-2025

## Data sources

- **Generation**: DESNZ Energy Trends Table 5.1 (quarterly), backfilled 2000-2009 for onshore/offshore wind, solar, and marine using DUKES Table 6.2 (annual)
- **Capacity**: DESNZ DUKES Table 5.7 (thermal/nuclear) and DUKES Table 6.2 (renewables, nameplate not de-rated)
- **Curtailment costs**: NESO's "Constraint Breakdown" dataset

All three are published under the Open Government Licence. Direct source links, along with every correction, backfill, and known limitation, are documented on the Cover sheet of the workbook itself.

## Running it yourself

```
pip install pandas numpy matplotlib openpyxl
python build_chart.py
```

The script looks for the workbook in the same folder by default. It uses the Poppins font if available on your system and falls back to matplotlib's default font otherwise.

## Caveats worth knowing

A few things are flagged in more detail on the workbook's Cover sheet, but worth having up front:

- 2000-2009 onshore/offshore wind, solar, and marine generation are estimated by splitting annual DUKES totals evenly across quarters, since quarterly data doesn't exist that far back. Validated against the real quarterly data at the 2010 boundary.
- 2025-2026 capacity is forward-filled from the last available annual figure (2024), since DUKES hasn't published 2025 data yet.
- 2024 coal capacity factor is a known artefact of the UK's last coal plant closing mid-year, not a data error.
- Grid constraint costs before 2017 aren't included; NESO's data doesn't go back further in this form.

An earlier version of the curtailment data undercounted true costs by roughly 2-3x, caught by cross-checking against NESO's own published totals. That correction, and the reasoning behind it, is documented in full on the Cover sheet.
