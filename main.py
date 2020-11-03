from converter import Converter
from colors import yellow, green

if __name__ == "__main__":
    converter = Converter()
    expr1 = '10 + 3 * 5 / ( 16 - 4 )'
    expr2 = 'A + ( B * C - ( D / E ^ F ) * G ) * H'

    print(f'Convertiendo {yellow(expr1)} a notación postfija...\nResultado:', green(converter.to_postfix(expr1)))
    print()
    print(f'Convertiendo {yellow(expr2)} a notación postfija...\nResultado:', green(converter.to_postfix(expr2)))