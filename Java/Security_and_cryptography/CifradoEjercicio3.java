import javax.crypto.*;
import javax.crypto.KeyGenerator;
import javax.crypto.spec.SecretKeySpec;

import java.io.*;
import java.lang.reflect.Array;
import java.nio.file.Files;
import javax.print.event.PrintEvent;
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Scanner;


public class CifradoEjercicio3{
public static void main(String[] args) {
Scanner entrada = new Scanner(System.in);
System.out.print("Nombre del fichero: ");
String nameFile = entrada.nextLine();
File file = new File("/home/austria/Documents/M9/"+ nameFile);
if (!file.exists()) {
    System.out.println("Lo siento no existe el fichero: "+ file);
    return;
}




//Pide la contraseña a usuario
System.out.print("Por favor introduce una contraseña: ");
String contrasenya = entrada.nextLine();
try{
    byte[] data = contrasenya.getBytes("UTF-8");
    MessageDigest md = MessageDigest.getInstance("SHA-256");
    byte[] key = Arrays.copyOf(md.digest(data), 192/8);
    SecretKey clave = new SecretKeySpec(key,"AES");

    //Si el nombre de archivo no acabe en .aes
    if(!nameFile.endsWith(".aes")){
        //Inicializar encriptor
        Cipher encriptor = Cipher.getInstance("AES/ECB/PKCS5Padding");
        encriptor.init(Cipher.ENCRYPT_MODE, clave);
        byte[] dades = new byte[1024];
        FileInputStream input = new FileInputStream(file);
        FileOutputStream output = new FileOutputStream("/home/austria/Documents/M9/"+nameFile+".aes");
        CipherOutputStream cipherOutput = new CipherOutputStream(output,encriptor);


        //Imprimir datos cifrados por el nuevo archivo
        int numBytes = input.read(dades);
        for (int i = 0; i < numBytes; i++) {
            cipherOutput.write(dades[i]);
        }
        cipherOutput.close();
        input.close();
        file.delete();
        System.out.println("Has creado con éxito el archivo cifrado");
    }else{
        //Inicializar desencriptor
        Cipher desencriptor = Cipher.getInstance("AES/ECB/PKCS5Padding");
        desencriptor.init(Cipher.DECRYPT_MODE, clave);

        byte[] dades = new byte[1024];
        FileInputStream input = new FileInputStream(file);
        FileOutputStream output = new FileOutputStream("/home/austria/Documents/M9/"+nameFile.substring(0, nameFile.length() - 4));
        CipherInputStream cipherInput = new CipherInputStream(input, desencriptor);

        //Imprimir datos cifrados por el nuevo archivo
        int numBytes = cipherInput.read(dades);
        for (int i = 0; i < numBytes; i++) {
            output.write(dades[i]);
        }
        cipherInput.close();
        output.close();
        file.delete();
        System.out.println("Se ha creado un nuevo archivo con datos descifrados");
    }
}catch(Exception e ){
    System.out.println(e);
}
}

}
