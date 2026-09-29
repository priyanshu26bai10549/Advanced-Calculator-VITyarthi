import json
from datetime import datetime
from pathlib import Path


class HistoryStore:
    """Persists recent calculations as JSON."""

    def __init__(self, path="data/history.json", limit=100):
        self.path = Path(path)
        self.limit = limit
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read(self):
        if not self.path.exists():
            return []
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return []

    def add(self, expression, result):
        history = self._read()
        history.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "expression": expression,
            "result": str(result),
        })
        self.path.write_text(
            json.dumps(history[-self.limit:], indent=2),
            encoding="utf-8"
        )

    def all(self):
        return self._read()

    def clear(self):
        self.path.write_text("[]", encoding="utf-8")
