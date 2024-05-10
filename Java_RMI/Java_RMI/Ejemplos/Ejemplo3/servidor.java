import java.rmi.RemoteException;
import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class servidor {
    public static void main(String[] args) {
        // Crea e instala el gestor de seguridad
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }
        try {
            // Crea un registro RMI en el puerto 1099
            Registry reg = LocateRegistry.createRegistry(1099);
            
            // Crea una instancia de contador
            contador micontador = new contador();
            
            // Vincula la instancia al registro RMI con un nombre
            Naming.rebind("mmicontador", micontador);

            System.out.println("Servidor preparado");
        } catch (Exception e) {
            System.out.println("Excepción: " + e.getMessage());
        }
    }
}
