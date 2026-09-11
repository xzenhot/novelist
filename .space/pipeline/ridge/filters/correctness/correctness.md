# Correctness Filter — Ridge

## Purpose
Verify all factual claims in the chapter: species names, geographic data, historical dates, court orders, ecological statistics, attributions.

## Domains to Check
- **Natural history:** species names (birds, trees, mammals) verified against standard references.
- **Geography:** place names, distances, administrative boundaries in Delhi NCR.
- **History:** Aravalli geology, Mangar Bani sacred grove history, DDA notifications, Supreme Court orders.
- **Ecology:** biodiversity data, migratory counts, corridor surveys.
- **Attribution:** quotes and claims attributed to named researchers or institutions.

## Outputs
- Updated chapter `model.json` with `correctness: { status, corrections, flagged_uncertainties }`
- `.space/pipeline/ridge/filters/correctness/filter-summary.md`

## Rules
- Flag, never invent. If a fact cannot be verified, mark it uncertain.
- Preferred sources: Salim Ali / BNHS for birds; Pradip Krishen for Delhi trees; Wildlife Institute of India for leopard data; CSE for policy.
