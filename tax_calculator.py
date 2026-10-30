def calculate_tax(taxable_income):
    taxable_income = max(0, taxable_income)

    tax = 0

    # First ₦800,000 at 0%
    if taxable_income <= 800_000:
        return 0

    taxable_income -= 800_000

    # Next ₦2,200,000 at 15%
    amount = min(taxable_income, 2_200_000)
    tax += amount * 0.15
    taxable_income -= amount

    if taxable_income <= 0:
        return tax

    # Next ₦9,000,000 at 18%
    amount = min(taxable_income, 9_000_000)
    tax += amount * 0.18
    taxable_income -= amount

    if taxable_income <= 0:
        return tax

    # Next ₦13,000,000 at 21%
    amount = min(taxable_income, 13_000_000)
    tax += amount * 0.21
    taxable_income -= amount

    if taxable_income <= 0:
        return tax

    # Next ₦25,000,000 at 23%
    amount = min(taxable_income, 25_000_000)
    tax += amount * 0.23
    taxable_income -= amount

    if taxable_income <= 0:
        return tax

    # Above ₦50,000,000 at 25%
    tax += taxable_income * 0.25

    return tax