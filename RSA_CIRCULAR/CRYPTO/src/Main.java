import java.security.KeyPair;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a sentence to encrypt:");
        String inputText = scanner.nextLine();

        try {
            // Configuration for ciphers and DSA
            KeyPair keyPair = CipherUtils.generateDSAKeyPair();
            CryptoConfig config = new CryptoConfig(3, 5, 8, keyPair); // Example values

            // Shift Cipher encryption and decryption
            String shifted = CipherUtils.shiftEncrypt(inputText, config.shiftKey);
            System.out.println("Shift Encrypted: " + shifted);
            System.out.println("Shift Decrypted: " + CipherUtils.shiftDecrypt(shifted, config.shiftKey));

            // Affine Cipher encryption and decryption
            String affineEncrypted = CipherUtils.affineEncrypt(inputText, config.affineA, config.affineB);
            System.out.println("Affine Encrypted: " + affineEncrypted);
            System.out.println("Affine Decrypted: " + CipherUtils.affineDecrypt(affineEncrypted, config.affineA, config.affineB));

            // Signing and verifying the message
            String signature = CipherUtils.signMessage(affineEncrypted, config.dsaKeyPair.getPrivate());
            System.out.println("Signature: " + signature);
            System.out.println("Signature Verified: " + CipherUtils.verifySignature(affineEncrypted, signature, config.dsaKeyPair.getPublic()));

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}
