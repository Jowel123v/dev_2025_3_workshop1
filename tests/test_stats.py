import pytest
from src.stats.stats import Stats

class TestStats:
    def setup_method(self):
        self.stats = Stats()
    
    def test_promedio(self):
        # Test con números enteros positivos
        assert self.stats.promedio([1, 2, 3, 4, 5]) == 3.0
        # Test con números decimales
        assert self.stats.promedio([1.5, 2.5, 3.5]) == 2.5
        # Test con un solo elemento
        assert self.stats.promedio([42]) == 42.0
        # Test con números negativos
        assert self.stats.promedio([-1, -2, -3]) == -2.0
        # Test con números mixtos (positivos y negativos)
        assert self.stats.promedio([-5, 0, 5]) == 0.0
        # Test con lista vacía (debe manejar el caso especial)
        assert self.stats.promedio([]) == 0
        # Test con números grandes
        assert self.stats.promedio([1000, 2000, 3000]) == 2000.0
    
    def test_mediana(self):
        # Test con número impar de elementos (valor central)
        assert self.stats.mediana([1, 2, 3, 4, 5]) == 3.0
        # Test con número par de elementos (promedio de valores centrales)
        assert self.stats.mediana([1, 2, 3, 4]) == 2.5
        # Test con un solo elemento
        assert self.stats.mediana([42]) == 42.0
        # Test con dos elementos
        assert self.stats.mediana([10, 20]) == 15.0
        # Test con lista desordenada
        assert self.stats.mediana([5, 1, 3, 2, 4]) == 3.0
        # Test con números decimales
        assert self.stats.mediana([1.1, 2.2, 3.3]) == 2.2
        # Test con números negativos
        assert self.stats.mediana([-3, -1, -2]) == -2.0
        # Test con números duplicados
        assert self.stats.mediana([1, 2, 2, 3]) == 2.0
        # Test con lista vacía
        assert self.stats.mediana([]) == 0
    
    def test_moda(self):
        # Test con moda clara (un valor más frecuente)
        assert self.stats.moda([1, 2, 2, 3, 3, 3]) == 3
        # Test con empate (debe retornar el primer valor encontrado)
        assert self.stats.moda([1, 1, 2, 2, 3]) == 1
        # Test con todos los elementos iguales
        assert self.stats.moda([5, 5, 5, 5]) == 5
        # Test con todos elementos únicos (debe retornar el primero)
        assert self.stats.moda([1, 2, 3, 4, 5]) == 1
        # Test con un solo elemento
        assert self.stats.moda([42]) == 42
        # Test con números decimales
        assert self.stats.moda([1.5, 2.5, 1.5, 3.5]) == 1.5
        # Test con números negativos
        assert self.stats.moda([-1, -2, -1, -3]) == -1
        # Test con strings (si la función lo permite)
        assert self.stats.moda(["a", "b", "b", "c"]) == "b"
        # Test con lista vacía
        assert self.stats.moda([]) == None
    
    def test_desviacion_estandar(self):
        # Test con conjunto simple conocido
        assert round(self.stats.desviacion_estandar([1, 2, 3, 4, 5]), 4) == 1.4142
        # Test con números idénticos (desviación = 0)
        assert self.stats.desviacion_estandar([5, 5, 5, 5]) == 0.0
        # Test con un solo elemento (desviación = 0)
        assert self.stats.desviacion_estandar([42]) == 0.0
        # Test con números con mayor variabilidad
        assert round(self.stats.desviacion_estandar([1, 10, 1, 10]), 4) == 4.5
        # Test con números decimales
        assert round(self.stats.desviacion_estandar([1.5, 2.5, 3.5]), 6) == 0.816497
        # Test con números negativos
        assert round(self.stats.desviacion_estandar([-2, -1, 0, 1, 2]), 4) == 1.4142
        # Test con lista vacía
        assert self.stats.desviacion_estandar([]) == 0
        # Test caso conocido: [2, 4, 4, 4, 5, 5, 7, 9]
        assert round(self.stats.desviacion_estandar([2, 4, 4, 4, 5, 5, 7, 9]), 1) == 2.0
    
    def test_varianza(self):
        # Test con conjunto simple conocido (varianza = desviación²)
        assert round(self.stats.varianza([1, 2, 3, 4, 5]), 1) == 2.0
        # Test con números idénticos (varianza = 0)
        assert self.stats.varianza([5, 5, 5, 5]) == 0.0
        # Test con un solo elemento (varianza = 0)
        assert self.stats.varianza([42]) == 0.0
        # Test con números con mayor variabilidad
        assert self.stats.varianza([1, 10, 1, 10]) == 20.25
        # Test con números decimales
        assert round(self.stats.varianza([1.5, 2.5, 3.5]), 6) == 0.666667
        # Test con números negativos
        assert round(self.stats.varianza([-2, -1, 0, 1, 2]), 1) == 2.0
        # Test con lista vacía
        assert self.stats.varianza([]) == 0
        # Test caso conocido
        assert round(self.stats.varianza([2, 4, 4, 4, 5, 5, 7, 9]), 1) == 4.0
    
    def test_rango(self):
        # Test con números enteros positivos
        assert self.stats.rango([1, 5, 3, 9, 2]) == 8
        # Test con números decimales
        assert self.stats.rango([1.5, 3.7, 2.1, 4.8]) == 3.3
        # Test con un solo elemento (rango = 0)
        assert self.stats.rango([42]) == 0
        # Test con números negativos
        assert self.stats.rango([-5, -1, -3, -10]) == 9
        # Test con números mixtos (positivos y negativos)
        assert self.stats.rango([-5, 0, 5]) == 10
        # Test con números idénticos (rango = 0)
        assert self.stats.rango([7, 7, 7, 7]) == 0
        # Test con dos elementos
        assert self.stats.rango([10, 25]) == 15
        # Test con lista vacía
        assert self.stats.rango([]) == 0
        # Test con números grandes
        assert self.stats.rango([1000, 5000, 2000, 8000]) == 7000

