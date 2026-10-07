# Adverse-event summary requirements

## AE-3: Severe-event summary

The adverse-event summary must include records where `AESEV` is exactly `SEVERE`.

### Output

The output must preserve these columns in this order:

1. `USUBJID`
2. `AETERM`
3. `AESEV`

### Constraints

- Use only the synthetic data in `data/synthetic_adae.csv`.
- Do not change source values.
- Preserve the output column names and ordering.
- Record assumptions or terminology questions for human review.

## Change-control note

Requirements may change during the workshop. A changed requirement must be updated together with the implementation, expected output, and automated checks.
