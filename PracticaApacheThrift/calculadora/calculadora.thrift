service Calculadora {
  double suma(1:double num1, 2:double num2),
  double resta(1:double num1, 2:double num2),
  double multiplicacion(1:double num1, 2:double num2),
  double division(1:double num1, 2:double num2),
  
  double seno(1:double grados),
  double coseno(1:double grados),
  double tangente(1:double grados),
  double gradosradianes(1:double grados),
  double radianesgrados(1:double grados),
  
  double potencia(1:double num1, 2:double num2),
  double raiz_cuadrada(1:double num1),
  double modulo(1:double num1, 2:double num2),
  double logaritmo(1:double num1)
  
  list<double> suma_vector(1:list<double> v1, 2:list<double> v2),
  list<double> resta_vector(1:list<double> v1, 2:list<double> v2),
  list<double> producto_vector(1:list<double> v1, 2:list<double> v2),  
}
