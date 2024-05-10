import java.rmi.Remote;
import java.rmi.RemoteException;

public interface contador_I extends Remote {
	public String getID() throws RemoteException;
	public boolean existeCliente(String dni) throws RemoteException;
    	public void setreplica(String id) throws RemoteException;
}
