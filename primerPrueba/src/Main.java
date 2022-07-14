public class Main {
    public static void main(String[] args) {
     //   System.out.println("Hello world!");
        var resultant = classPotato(5,7, 7);
        System.out.println(resultant);
        coche miCoche = new coche();
        miCoche.addPuertas();
        System.out.println(miCoche.numPuertas);

    }
    public static int classPotato(int a, int b, int c ) {
        return a+b+c;
    }
}
class coche {
    public int numPuertas = 0;
    public void addPuertas(){
        this.numPuertas++;
    }
}