import java.rmi.RemoteException;
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class servidor {
    static String id1 ="servidor 1", id2 = "servidor 2";
    public static void main(String[] args) {
        // Crea e instala el gestor de seguridad
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }
        try {
            //creamos las dos instancias contador (servidores)
            icontador contador1 = new contador(id1);
            icontador contador2 = new contador(id2);
            
            // Crea un registro RMI en el puerto 1099
            Registry reg = LocateRegistry.createRegistry(1099);
            // Crea una instancia de contador
            Registry registry = LocateRegistry.getRegistry();  
                      
            // Vincula la instancia al registro RMI con un nombre
            registry.rebind(id1,contador1);
            registry.rebind(id2,contador2);
            
            //Se vincula tambien cada instancia contador con el otro servidor
            contador_I rep1 = (contador_I) contador1, rep2 = (contador_I) contador2;
            rep1.setreplica(id2);
            rep2.setreplica(id1);
            
            //System.out.println("Servidores " + id1 " y " + id2 + "preparado");
        } catch (Exception e) {
            System.out.println("Excepción: " + e.getMessage());
        }
    }
}
