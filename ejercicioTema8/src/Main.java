public class Main {
    public static void main(String[] args) {

        Persona persona = new Persona();

        persona.setNombre("David");
        persona.setEdad(24);
        persona.setTelefono("317000000");

        System.out.println(persona.getNombre());
        System.out.println(persona.getEdad());
        System.out.println(persona.getTelefono());
    }


}
class Persona{
    private String nombre;
    private int edad;
    private String telefono;


    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }
    public int getEdad() {
        return edad;
    }


    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getTelefono() {
        return telefono;
    }


}

