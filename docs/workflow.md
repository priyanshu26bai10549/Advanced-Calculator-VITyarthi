# Process Workflow

```text
START
  |
  v
Display Menu
  |
  v
User selects operation
  |
  +---- Basic expression ----> Validate --> Calculate --> Save history
  |
  +---- Scientific ----------> Validate domain --> Calculate --> Save history
  |
  +---- Equation ------------> Validate coefficients --> Solve
  |
  +---- Statistics ----------> Parse dataset --> Analyze
  |
  +---- Matrix --------------> Validate dimensions --> Calculate
  |
  +---- History -------------> Read/Clear JSON
  |
  v
Display result/error
  |
  v
Return to menu
  |
  +---- Exit ----> END
