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


public class CifradoEjercicio4{
	public static void main(String[] args) {

		byte[] enc = {
					(byte)0x2d, (byte)0xb3, (byte)0x14, (byte)0x90,
					(byte)0xbd, (byte)0x0a, (byte)0xb1, (byte)0x7c, 
					(byte)0x45, (byte)0x2f, (byte)0x40, (byte)0x67, 
					(byte)0xc0, (byte)0x81, (byte)0xe2, (byte)0x79, 
					(byte)0x4d, (byte)0xa8, (byte)0x54, (byte)0x86, 
					(byte)0x3a, (byte)0xf7, (byte)0x0e, (byte)0x64, 
					(byte)0x97, (byte)0xc1, (byte)0x78, (byte)0xef, 
					(byte)0x84, (byte)0xdd, (byte)0x9a, (byte)0xf1};
						
		for (int i=0;i<=9999;i++){
			String pass = Integer.toString(i);
			while (pass.length()<4){
				pass = "0" + pass;
			}

			SecretKey sKey= null;
			try {
				byte[] data = pass.getBytes("UTF-8"); 
				MessageDigest md= MessageDigest.getInstance("SHA-256");
				byte[] hash = md.digest(data);
				byte[] key = Arrays.copyOf(hash, 192/8);
				sKey = new SecretKeySpec(key,"AES");
				Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
				cipher.init(Cipher.DECRYPT_MODE, sKey);
				data = cipher.doFinal(enc);
				System.out.println("Clave posible: "+ pass + " = " + new String(data));

			}
			catch(Exception e ) {}
		}
	}
}