# Validation

- Exported model outputs compared with Python fixtures where a model exists.
- Input validation covers invalid numbers, CSV dates and duplicate dates.
- Deterministic scheduling and exact linear-fit cases checked.
- A lightweight DOM harness checks initial rendering and wired controls.
- Browser visual verification and real Vercel deployment were not completed here.
- Browser checks must include desktop/mobile layout and keyboard navigation.

Run `node tests/test.cjs .` from the project root. Rebuilding the model regenerates its fixture file.
