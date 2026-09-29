# Storage / ER Design

The project uses a JSON file rather than a relational database.

```text
+-------------------------------+
| CalculationHistory            |
+-------------------------------+
| timestamp                     |
| expression                    |
| result                        |
+-------------------------------+
```

The JSON structure is an array of calculation records. A maximum of 100 recent records is retained.
