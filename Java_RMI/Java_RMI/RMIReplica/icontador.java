import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.registry.Registry;
import java.rmi.NotBoundException;

public interface icontador extends Remote {
    public int InicioSesion(String dni, Registry r) throws RemoteException, NotBoundException;
    public int registrar(String dni, Registry r) throws RemoteException, NotBoundException;
    public void imprimir() throws RemoteException;
    public void donar(String dni, int valor) throws RemoteException;
    //public void imprimirDonado(String dni) throws RemoteException;
}
