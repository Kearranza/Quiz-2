package ac.cr.tec;

public class Singleton {
    public static Singleton instance = null;

    public static Singleton getInstance(){
        if (instance == null){
            instance = new Singleton();
            System.out.println("Creación de instancia");
        }
        else{
            System.out.println("La instancia ya fue creada, por lo cual no se puede crear una nueva");
        }
        return instance;
    }
}
