from decimal import Decimal, getcontext

# Set precision for our large number calculations
getcontext().prec = 100

def calculate_key_space():
    """
    Calculate the size of the Bitcoin private key space (256-bit number)
    """
    # Number of possible private keys (2^256)
    total_keys = Decimal(2) ** 256
    return total_keys

def format_large_number(n):
    """
    Format very large numbers in scientific notation and regular notation
    """
    scientific = f"{n:.2E}"
    regular = f"{n:,}"
    return scientific, regular

def calculate_energy_requirements(keys_per_second, watts_per_try):
    """
    Calculate energy requirements for brute force attempts
    """
    total_keys = calculate_key_space()
    
    # Calculate time and energy requirements
    seconds_needed = total_keys / Decimal(keys_per_second)
    kwh_per_second = Decimal(watts_per_try * keys_per_second) / Decimal(1000)  # Convert W to kW
    total_kwh = Decimal(kwh_per_second) * Decimal(seconds_needed)  # Fixed line
    
    # Convert to years for comprehension
    years = seconds_needed / Decimal(365 * 24 * 60 * 60)
    
    return years, total_kwh

def main():
    # Calculate and display key space
    total_keys = calculate_key_space()
    scientific_notation, regular_notation = format_large_number(total_keys)
    
    print("Bitcoin Private Key Space Analysis")
    print("-" * 40)
    print(f"Total possible private keys:")
    print(f"Scientific notation: {scientific_notation}")
    print(f"Regular notation: {regular_notation}")
    print()
    
    # Example calculation using hypothetical hardware
    # Assuming very optimistic parameters
    TRIES_PER_SECOND = Decimal('1_000_000_000_000')  # 1 trillion tries per second
    WATTS_PER_TRY = Decimal('1e-9')  # 1 nanowatt per try (very optimistic)
    
    years, total_kwh = calculate_energy_requirements(TRIES_PER_SECOND, WATTS_PER_TRY)
    
    print("Brute Force Attempt Analysis")
    print("-" * 40)
    print(f"Assuming {TRIES_PER_SECOND:,} tries per second")
    print(f"Energy per try: {WATTS_PER_TRY} watts")
    print()
    print("Time required:")
    print(f"Years: {years:.2E}")
    print()
    print("Energy required:")
    print(f"Total kWh: {total_kwh:.2E}")
    
    # Add some real-world comparisons
    annual_global_energy = Decimal('170_000_000_000_000')  # ~170,000 TWh annual global energy production
    years_of_global_energy = total_kwh / annual_global_energy
    
    print()
    print("Real-world Comparison")
    print("-" * 40)
    print(f"Number of years of total global energy production required: {years_of_global_energy:.2E}")

if __name__ == "__main__":
    main()
