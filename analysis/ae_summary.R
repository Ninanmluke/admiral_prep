# Synthetic implementation of requirement AE-3.

adae <- read.csv("data/synthetic_adae.csv", stringsAsFactors = FALSE)

ae_summary <- adae[
  adae$AESEV == "SEVERE",
  c("USUBJID", "AETERM", "AESEV")
]

print(ae_summary)
