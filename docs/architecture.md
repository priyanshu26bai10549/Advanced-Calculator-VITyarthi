# System Architecture

```text
+----------------------+
|      User / CLI      |
+----------+-----------+
           |
           v
+----------------------+
|     Application      |
|       app.py         |
+----------+-----------+
           |
           v
+----------------------+       +----------------------+
|  Calculator Service  |------>|   Logger Service    |
+----------+-----------+       +----------------------+
           |
     +-----+-------------------------------+
     |                 |                   |
     v                 v                   v
+---------+      +-----------+      +-------------+
| Engine  |      | Scientific|      |   Advanced  |
|Validator|      | Functions |      | Math Tools  |
+---------+      +-----------+      | Eq/Stats/Mat|
                                   +------+-------+
                                          |
                                          v
                                   +-------------+
                                   | History JSON|
                                   +-------------+
```

## Architectural Style
A lightweight layered/modular architecture is used:
- Presentation/application layer
- Service layer
- Core calculation layer
- Persistence layer

This separation improves maintainability and makes individual components testable.
