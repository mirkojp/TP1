# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
# deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
# esa base imponible


from activity_1 import SingletonMeta


class TaxesCalculator(metaclass=SingletonMeta):
    """
    Class for calculating taxes. It uses the Singleton pattern to ensure only one instance exists.
    """

    def calculate_taxes(self, base):
        """
        Calculate taxes based on the given base amount.
        """
        iva = base * 0.21  # Calculate VAT (21%)
        iibb = base * 0.05  # Calculate IIBB (5%)
        mun_contribution = base * 0.012  # Calculate municipal contributions (1.2%)
        total_taxes = iva + iibb + mun_contribution  # Sum up all taxes
        total_amount = base + total_taxes  # Add taxes to the base amount
        return total_amount  # Return the total amount including taxes


if __name__ == "__main__":
    try:
        ts_1 = TaxesCalculator()
        salary = 1500
        taxed_salary = ts_1.calculate_taxes(salary)
        print(f"Your salary with taxes is: {taxed_salary}")
    except ValueError as e:
        print("Error:", e)
