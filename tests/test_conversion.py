import pytest
from src.conversion.conversion import Conversion

class TestConversion:
    def setup_method(self):
        self.conversion = Conversion()
    
    def test_celsius_a_fahrenheit(self):
        # Test con punto de congelación del agua
        assert self.conversion.celsius_a_fahrenheit(0) == 32.0
        # Test con punto de ebullición del agua
        assert self.conversion.celsius_a_fahrenheit(100) == 212.0
        # Test con temperatura corporal normal
        assert round(self.conversion.celsius_a_fahrenheit(37), 1) == 98.6
        # Test con temperatura negativa (cero absoluto aproximado)
        assert round(self.conversion.celsius_a_fahrenheit(-273.15), 2) == -459.67
        # Test con valor decimal
        assert self.conversion.celsius_a_fahrenheit(25.5) == 77.9
    
    def test_fahrenheit_a_celsius(self):
        # Test con punto de congelación del agua
        assert self.conversion.fahrenheit_a_celsius(32) == 0.0
        # Test con punto de ebullición del agua
        assert self.conversion.fahrenheit_a_celsius(212) == 100.0
        # Test con temperatura corporal normal
        assert round(self.conversion.fahrenheit_a_celsius(98.6), 1) == 37.0
        # Test con temperatura negativa
        assert round(self.conversion.fahrenheit_a_celsius(-40), 1) == -40.0
        # Test con valor decimal
        assert round(self.conversion.fahrenheit_a_celsius(77.9), 1) == 25.5
    
    def test_metros_a_pies(self):
        # Test con 1 metro exacto
        assert round(self.conversion.metros_a_pies(1), 5) == 3.28084
        # Test con valor cero
        assert self.conversion.metros_a_pies(0) == 0
        # Test con valor decimal
        assert round(self.conversion.metros_a_pies(1.5), 5) == 4.92126
        # Test con valor grande (1 kilómetro)
        assert round(self.conversion.metros_a_pies(1000), 2) == 3280.84
        # Test con valor pequeño (1 centímetro)
        assert round(self.conversion.metros_a_pies(0.01), 7) == 0.0328084
    
    def test_pies_a_metros(self):
        # Test con conversión exacta
        assert round(self.conversion.pies_a_metros(3.28084), 0) == 1.0
        # Test con valor cero
        assert self.conversion.pies_a_metros(0) == 0
        # Test con 1 pie exacto
        assert round(self.conversion.pies_a_metros(1), 4) == 0.3048
        # Test con valor grande
        assert round(self.conversion.pies_a_metros(1000), 1) == 304.8
        # Test con valor decimal
        assert round(self.conversion.pies_a_metros(6.56168), 1) == 2.0
    
    def test_decimal_a_binario(self):
        # Test con números básicos
        assert self.conversion.decimal_a_binario(0) == "0"
        assert self.conversion.decimal_a_binario(1) == "1"
        assert self.conversion.decimal_a_binario(2) == "10"
        assert self.conversion.decimal_a_binario(10) == "1010"
        # Test con potencias de 2
        assert self.conversion.decimal_a_binario(8) == "1000"
        assert self.conversion.decimal_a_binario(16) == "10000"
        assert self.conversion.decimal_a_binario(255) == "11111111"
        # Test con números más grandes
        assert self.conversion.decimal_a_binario(1024) == "10000000000"
    
    def test_binario_a_decimal(self):
        # Test con números básicos
        assert self.conversion.binario_a_decimal("0") == 0
        assert self.conversion.binario_a_decimal("1") == 1
        assert self.conversion.binario_a_decimal("10") == 2
        assert self.conversion.binario_a_decimal("1010") == 10
        # Test con potencias de 2
        assert self.conversion.binario_a_decimal("1000") == 8
        assert self.conversion.binario_a_decimal("10000") == 16
        assert self.conversion.binario_a_decimal("11111111") == 255
        # Test con números más grandes
        assert self.conversion.binario_a_decimal("10000000000") == 1024
    
    def test_decimal_a_romano(self):
        # Test con números básicos
        assert self.conversion.decimal_a_romano(1) == "I"
        assert self.conversion.decimal_a_romano(5) == "V"
        assert self.conversion.decimal_a_romano(10) == "X"
        assert self.conversion.decimal_a_romano(50) == "L"
        assert self.conversion.decimal_a_romano(100) == "C"
        assert self.conversion.decimal_a_romano(500) == "D"
        assert self.conversion.decimal_a_romano(1000) == "M"
        # Test con números con substracción
        assert self.conversion.decimal_a_romano(4) == "IV"
        assert self.conversion.decimal_a_romano(9) == "IX"
        assert self.conversion.decimal_a_romano(40) == "XL"
        assert self.conversion.decimal_a_romano(90) == "XC"
        assert self.conversion.decimal_a_romano(400) == "CD"
        assert self.conversion.decimal_a_romano(900) == "CM"
        # Test con números complejos
        assert self.conversion.decimal_a_romano(1994) == "MCMXCIV"
        assert self.conversion.decimal_a_romano(3999) == "MMMCMXCIX"
        assert self.conversion.decimal_a_romano(2023) == "MMXXIII"
    
    def test_romano_a_decimal(self):
        # Test con números básicos
        assert self.conversion.romano_a_decimal("I") == 1
        assert self.conversion.romano_a_decimal("V") == 5
        assert self.conversion.romano_a_decimal("X") == 10
        assert self.conversion.romano_a_decimal("L") == 50
        assert self.conversion.romano_a_decimal("C") == 100
        assert self.conversion.romano_a_decimal("D") == 500
        assert self.conversion.romano_a_decimal("M") == 1000
        # Test con números con substracción
        assert self.conversion.romano_a_decimal("IV") == 4
        assert self.conversion.romano_a_decimal("IX") == 9
        assert self.conversion.romano_a_decimal("XL") == 40
        assert self.conversion.romano_a_decimal("XC") == 90
        assert self.conversion.romano_a_decimal("CD") == 400
        assert self.conversion.romano_a_decimal("CM") == 900
        # Test con números complejos
        assert self.conversion.romano_a_decimal("MCMXCIV") == 1994
        assert self.conversion.romano_a_decimal("MMMCMXCIX") == 3999
        assert self.conversion.romano_a_decimal("MMXXIII") == 2023
    
    def test_texto_a_morse(self):
        # Test con letras básicas
        assert self.conversion.texto_a_morse("A") == ".-"
        assert self.conversion.texto_a_morse("B") == "-..."
        assert self.conversion.texto_a_morse("C") == "-.-."
        # Test con la señal de socorro SOS
        assert self.conversion.texto_a_morse("SOS") == "... --- ..."
        # Test con palabra completa
        assert self.conversion.texto_a_morse("HELLO") == ".... . .-.. .-.. ---"
        # Test con números
        assert self.conversion.texto_a_morse("123") == ".---- ..--- ...--"
        # Test con texto mixto (letras y números)
        assert self.conversion.texto_a_morse("A1B2") == ".- .---- -... ..---"
        # Test con texto vacío
        assert self.conversion.texto_a_morse("") == ""
        # Test con minúsculas (deben convertirse igual que mayúsculas)
        assert self.conversion.texto_a_morse("hello") == ".... . .-.. .-.. ---"
    
    def test_morse_a_texto(self):
        # Test con letras básicas
        assert self.conversion.morse_a_texto(".-") == "A"
        assert self.conversion.morse_a_texto("-...") == "B"
        assert self.conversion.morse_a_texto("-.-.") == "C"
        # Test con la señal de socorro SOS
        assert self.conversion.morse_a_texto("... --- ...") == "SOS"
        # Test con palabra completa
        assert self.conversion.morse_a_texto(".... . .-.. .-.. ---") == "HELLO"
        # Test con números
        assert self.conversion.morse_a_texto(".---- ..--- ...--") == "123"
        # Test con código mixto
        assert self.conversion.morse_a_texto(".- .---- -... ..---") == "A1B2"
        # Test con código vacío
        assert self.conversion.morse_a_texto("") == ""
        # Test con espacios extra (deben ser ignorados)
        assert self.conversion.morse_a_texto("...  ---  ...") == "SOS"
