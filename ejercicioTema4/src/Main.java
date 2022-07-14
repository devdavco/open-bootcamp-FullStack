public class Main {
    public static void main(String[] args) {
        comparar(0); //Punto 1
        segundoPunto(2);
        tercerPunto(2);
        cuartoPunto(2);
        quintoPunto("VERANO");
    }

    public static void comparar(int numeroIf){
        System.out.println("Punto 1");
        if (numeroIf > 0){
            System.out.println("El número ingresado es Positivo");
        } else if (numeroIf < 0 ) {
            System.out.println("El número ingresado es Negativo");
        }
        else {
            System.out.println("Número ingresado es Cero");
        }

    }
    public static void segundoPunto(int numeroWhile){
        System.out.println("Punto 2");

        while (numeroWhile < 3 ){
            System.out.println(numeroWhile);
            numeroWhile++;
        }
    }
    public static void tercerPunto(int numeroDo){
        System.out.println("Punto 3");

        do {
            System.out.println(numeroDo);
            numeroDo++;
        }while (numeroDo<3);
    }
    public static void cuartoPunto(int numeroFor){
        System.out.println("Punto 4");
        for(int i = 0; i <= 3; i++){
            System.out.println(i);
        }
    }
    public static void quintoPunto(String estacion){
        System.out.println("Punto 5");
        switch (estacion){
            case "VERANO":
                System.out.println("Está en Verano");
                break;
            case "INVIERNO":
                System.out.println("Está en Invierno");
                break;
            case "PRIMAVERA":
                System.out.println("Está en Primavera");
                break;
            case  "OTOÑO":
                System.out.println("Está en Otoño");
                break;
            default:
                System.out.println("Estacion ingresada no existe");
        }
    }
}