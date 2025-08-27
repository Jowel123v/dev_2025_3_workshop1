class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = str(jugador1).strip().lower()
        jugador2 = str(jugador2).strip().lower()

        validos = {"piedra", "papel", "tijera"}
        if jugador1 not in validos or jugador2 not in validos:
         return "invalid"

        if jugador1 == jugador2:
            return "empate"
        elif (jugador1 == "piedra" and jugador2 == "tijera") or \
             (jugador1 == "tijera" and jugador2 == "papel") or \
             (jugador1 == "papel" and jugador2 == "piedra"):
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """
        if intento == numero_secreto:
            return "correcto"
        elif intento < numero_secreto:
            return "muy bajo"
        else:
            return "muy alto"
    
    def ta_te_ti_ganador(self, tablero):
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        filas = tablero
        columnas = [[tablero[r][c] for r in range(3)] for c in range(3)]
        diagonal = [
            [tablero[i][i] for i in range(3)],
            [tablero[i][2 - i] for i in range(3)]
        ]
        lineas = filas + columnas + diagonal

        for i in ("X", "O"):
            if any(all(c == i for c in linea) for linea in lineas):
                return i
        espacios = any(" " in fila for fila in tablero)
        return "continua" if espacios else "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        colores = []
        n = len(colores_disponibles)
        for i in range(longitud):
            colores.append(colores_disponibles[i % n])
        return colores

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        for v in (desde_fila, desde_col, hasta_fila, hasta_col):
            if v < 0 or v > 7:
                return False
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        if not (desde_fila == hasta_fila or desde_col == hasta_col):
            return False

        def vacia(celda):
            return celda is None or (isinstance(celda, str) and celda.strip() == "")

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if not vacia(tablero[desde_fila][c]):
                    return False
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for f in range(desde_fila + paso, hasta_fila, paso):
                if not vacia(tablero[f][desde_col]):
                    return False
        return True