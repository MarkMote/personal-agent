"""
Unit Conversion — Jane Street Mock Interview Problem

You're given conversion facts as tuples: (from_unit, quantity, to_unit)
meaning "1 from_unit = quantity to_units."

The system doesn't know what any unit means. It just knows the
relationships you feed it and can chain them together.

Facts:
    ("m", 3.28, "ft")       # 1 meter = 3.28 feet
    ("ft", 12, "in")        # 1 foot = 12 inches
    ("in", 2.54, "cm")      # 1 inch = 2.54 centimeters
    ("km", 1000, "m")       # 1 kilometer = 1000 meters
    ("hr", 60, "min")       # 1 hour = 60 minutes
    ("min", 60, "sec")      # 1 minute = 60 seconds
    ("mi", 5280, "ft")      # 1 mile = 5280 feet
    ("lb", 16, "oz")        # 1 pound = 16 ounces
    ("kg", 2.205, "lb")     # 1 kilogram = 2.205 pounds
    ("gal", 3.785, "L")     # 1 gallon = 3.785 liters
    ("L", 1000, "mL")       # 1 liter = 1000 milliliters

Example queries:
    convert(2, "m", "ft")        # → 6.56       (direct)
    convert(2, "m", "in")        # → 78.72      (2 hops: m → ft → in)
    convert(1, "km", "in")       # → 39,360     (3 hops: km → m → ft → in)
    convert(1, "hr", "sec")      # → 3600       (2 hops: hr → min → sec)
    convert(1, "mi", "km")       # → ~1.609     (3 hops: mi → ft → m → km)
    convert(5, "kg", "oz")       # → 176.4      (2 hops: kg → lb → oz)
    convert(1, "m", "hr")        # → ERROR      (no path: length vs time)
"""


class UnitConverter:
    def __init__(self):
        pass

    def add_fact(self, from_unit: str, quantity: float, to_unit: str) -> None:
        """Register that 1 from_unit = quantity to_units.
        Should also store the inverse (1 to_unit = 1/quantity from_units)."""
        pass

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        """Convert value from from_unit to to_unit.
        May require chaining through intermediate units.
        Raise ValueError if no conversion path exists."""
        pass


# ─── Tests ───────────────────────────────────────────────────────────────────

def test_stage1_direct():
    """Stage 1: Direct conversions only."""
    uc = UnitConverter()
    uc.add_fact("m", 3.28, "ft")
    uc.add_fact("ft", 12, "in")
    uc.add_fact("hr", 60, "min")
    uc.add_fact("min", 60, "sec")

    # Direct conversions
    assert abs(uc.convert(1, "m", "ft") - 3.28) < 0.01
    assert abs(uc.convert(2, "ft", "in") - 24.0) < 0.01
    assert abs(uc.convert(1, "hr", "min") - 60.0) < 0.01

    # Inverse (should work from the stored inverse fact)
    assert abs(uc.convert(3.28, "ft", "m") - 1.0) < 0.01
    assert abs(uc.convert(24, "in", "ft") - 2.0) < 0.01

    # Same unit
    assert abs(uc.convert(5, "m", "m") - 5.0) < 0.01

    print("Stage 1 passed!")


def test_stage2_multihop():
    """Stage 2: Multi-hop conversions (chaining through intermediate units)."""
    uc = UnitConverter()
    uc.add_fact("m", 3.28, "ft")
    uc.add_fact("ft", 12, "in")
    uc.add_fact("hr", 60, "min")
    uc.add_fact("min", 60, "sec")

    # Two hops: m → ft → in
    assert abs(uc.convert(1, "m", "in") - 39.36) < 0.01
    assert abs(uc.convert(2, "m", "in") - 78.72) < 0.01

    # Two hops: hr → min → sec
    assert abs(uc.convert(1, "hr", "sec") - 3600.0) < 0.01

    # Inverse multi-hop: in → ft → m
    assert abs(uc.convert(39.36, "in", "m") - 1.0) < 0.01

    # No path between unrelated units (length vs time)
    try:
        uc.convert(1, "m", "hr")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    # Unknown unit
    try:
        uc.convert(1, "m", "kg")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass

    print("Stage 2 passed!")


def test_stage2_longer_chains():
    """Stage 2 bonus: Longer chains and branching graphs."""
    uc = UnitConverter()
    uc.add_fact("km", 1000, "m")
    uc.add_fact("m", 100, "cm")
    uc.add_fact("cm", 10, "mm")3. **connect_four.md** — Reported by multiple candidates

    uc.add_fact("m", 3.28, "ft")
    uc.add_fact("ft", 12, "in")

    # Three hops: km → m → ft → in
    assert abs(uc.convert(1, "km", "in") - 39360.0) < 1.0

    # Four hops: km → m → cm → mm
    assert abs(uc.convert(1, "km", "mm") - 1_000_000) < 0.01

    # Cross-branch: in → ft → m → cm
    assert abs(uc.convert(12, "in", "cm") - 100.0) < 1.0

    print("Stage 2 longer chains passed!")


if __name__ == "__main__":
    test_stage1_direct()
    test_stage2_multihop()
    test_stage2_longer_chains()
    print("\nAll tests passed!")
