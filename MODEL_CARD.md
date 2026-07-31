# LLX2026 model card

## Intended use

LLX2026 is an explicit research model for estimating the magnitude of concrete
drying shrinkage from drying time, age at drying, relative humidity,
volume-to-surface ratio, water-to-cement ratio, and total aggregate content.

## Release status

Version 1 implements the nine-parameter equation and an empirical
prediction interval. The interval is based on drying-age-conditioned,
experiment-group out-of-fold residual scatter. It is not a confidence interval
for the mean response and is not a substitute for project-specific uncertainty
assessment.

The associated manuscript has not been accepted or published. This repository
is a software record and does not imply peer-review endorsement of the model.

## Aggregate proxy

The software estimates aggregate volume fraction as total aggregate mass per
unit concrete volume divided by a nominal density of 2650 kg/m3. This is a
conversion proxy, not a measured particle density for each aggregate source.
Users with a measured aggregate volume fraction should use the Python API and
supply it directly. The public `ModelParameters` object also permits an
alternative nominal density to be supplied without modifying package code.

## Limitations

- The current model was calibrated on records from the Northwestern University
  concrete creep and shrinkage database.
- Database records are not equivalent to independent experiments; grouped
  validation uses original experiment identifiers.
- Predictions outside the database-supported material and exposure ranges are
  uncertain.
- The program is research software and must not be used as the sole basis for
  structural design, safety assessment, or compliance decisions.
- The original database is not redistributed by this repository.
