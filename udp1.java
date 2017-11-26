import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class udp1{  

public static void main(String[] args) throws Exception {  

DatagramSocket ds = new DatagramSocket();  
byte[] buf = new byte[1024];
int length= buf.length;
InetAddress ip = InetAddress.getByName("192.168.10.128");  
DatagramPacket dp = new DatagramPacket(buf,length, ip, 3000);
for (int i=0;i<20;i++){
ds.send(dp);
System.out.println("Sending "+ length +" bytes");
} 
//ds.close(); 
}
}
