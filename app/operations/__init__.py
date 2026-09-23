class Operations:

    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y
    
    @staticmethod
    def sub(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def mult(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def div(x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y