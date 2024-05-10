import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class cliente {
    public static void main(String[] args) {
        // Crea e instala el gestor de seguridad
        if (System.getSecurityManager() == null) {
            System.setSecurityManager(new SecurityManager());
        }
        try {
            // Obtiene el registro RMI del servidor
            //Registry mireg = LocateRegistry.getRegistry("127.0.0.1", 1099);
            Registry mireg = LocateRegistry.getRegistry("localhost", 1099);
            
            // Obtiene la referencia al objeto remoto del servidor, que seleccione al azar de los dos servidores
            icontador micontador = (icontador) mireg.lookup(mireg.list()[0]); //mmicontador
            
            //Asignamos el dni
            String dni = "0";
            
            boolean salir = true;
            Scanner scan = new Scanner(System.in);
            int indice = 0;
            while (salir) {
            System.out.println("Bienvenido!");
            System.out.println("1. Iniciar Sesion");
	    System.out.println("2. Registrarse"); 
	    System.out.println("3. Salir");
	    String opcion1 = scan.nextLine();
	    switch (opcion1) {
		    	case "1":
		            System.out.println("Introduzca su dni: "); 
		    	    dni = scan.nextLine();
			    indice = micontador.InicioSesion(dni, mireg);
			    System.out.println("Bienvenido " + dni); 
			break;
		    	case "2":
		    	    System.out.println("Introduzca su dni: "); 
		    	    dni = scan.nextLine();
			    indice = micontador.registrar(dni, mireg);
			    System.out.println("Cliente  " + dni + " registrado con exito!"); 			    
		    	break;
		    	case "3":
		    		salir = false;
		    	break;
		    }
		    
		    while (salir && dni != "0"){
		    System.out.println("Elige una opcion:");
		    System.out.println("1. Donar");
		    System.out.println("2. Mostrar lista de donadores");
		    System.out.println("3. Salir"); 
		    String opcion2 = scan.nextLine();
		    switch (opcion2) {
		    	
		    	case "1":
		    		System.out.println("Introduzca cantidad a donar: "); 
		  		String entrada = scan.nextLine();
		  		int cant = Integer.parseInt(entrada);
		    		micontador.donar(dni, cant);
		    	break;
		    	case "2":
				micontador.imprimir();
			break;
		    	case "3":
		    		salir = false;
		    	break;
		    }
		    }
        }
        } catch (Exception e) {
            System.err.println("Excepción del sistema: " + e);
        }
    }
}
