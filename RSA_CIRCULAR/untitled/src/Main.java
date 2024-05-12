import java.security.KeyPair;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            // Generate RSA key pair
            KeyPair keyPair = RSAUtil.generateKeyPair();

            System.out.println("Enter a message to encrypt:");
            String message = scanner.nextLine();

            // Encrypt the message
            String encryptedMessage = RSAUtil.encrypt(message, keyPair);
            System.out.println("Encrypted Message: " + encryptedMessage);

            // Decrypt the message
            String decryptedMessage = RSAUtil.decrypt(encryptedMessage, keyPair);
            System.out.println("Decrypted Message: " + decryptedMessage);
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}
