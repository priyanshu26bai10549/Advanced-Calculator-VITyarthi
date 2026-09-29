import math
from statistics import mean, median, mode, pstdev


class StatisticsCalculator:
    """Descriptive statistics for a numeric dataset."""

    @staticmethod
    def parse(data: str):
        values = [float(x.strip()) for x in data.split(",") if x.strip()]
        if not values:
            raise ValueError("Enter at least one number.")
        if len(values) > 10000:
            raise ValueError("Maximum dataset size is 10,000 values.")
        return values

    @staticmethod
    def summary(values):
        result = {
            "count": len(values),
            "mean": mean(values),
            "median": median(values),
            "min": min(values),
            "max": max(values),
            "population_std_dev": pstdev(values),
        }
        try:
            result["mode"] = mode(values)
        except Exception:
            result["mode"] = "No unique mode"
        return result
