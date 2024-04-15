# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
# deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
# esa base imponible


from singleton import SingletonMeta

class Taxes_Singleton(metaclass=SingletonMeta):


    def TriTax_Calculator(self,base):
        iva = base * 0.21
        iibb = base * 0.05
        mun_contribution = base * 0.012
        total_taxes = iva+iibb+mun_contribution
        return base + total_taxes 

if __name__ == "__main__":
    try:
        ts_1 = Taxes_Singleton()
        salary = 1500
        sad_salary = ts_1.TriTax_Calculator(salary)
        print(f"Your salary with taxes is : {sad_salary}")


    except ValueError as e:
        print("Error : " ,e)