import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Cipher;
import java.util.Base64;

public class RSAUtil {
    private static final String RSA = "RSA";

    // Generates RSA key pair
    public static KeyPair generateKeyPair() throws NoSuchAlgorithmException {
        KeyPairGenerator generator = KeyPairGenerator.getInstance(RSA);
        generator.initialize(2048);
        return generator.generateKeyPair();
    }

    // Encrypts text using the public key
    public static String encrypt(String plainText, KeyPair keyPair) throws Exception {
        Cipher cipher = Cipher.getInstance(RSA);
        cipher.init(Cipher.ENCRYPT_MODE, keyPair.getPublic());
        byte[] cipherText = cipher.doFinal(plainText.getBytes());
        return Base64.getEncoder().encodeToString(cipherText);
    }

    // Decrypts text using the private key
    public static String decrypt(String cipherText, KeyPair keyPair) throws Exception {
        byte[] bytes = Base64.getDecoder().decode(cipherText);
        Cipher deCipher = Cipher.getInstance(RSA);
        deCipher.init(Cipher.DECRYPT_MODE, keyPair.getPrivate());
        return new String(deCipher.doFinal(bytes));
    }
}
