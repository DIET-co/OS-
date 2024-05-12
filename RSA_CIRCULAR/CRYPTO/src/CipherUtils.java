import java.security.*;
import java.util.Base64;

public class CipherUtils {
    private static final int ALPHABET_SIZE = 26;

    // Shift Cipher methods
    public static String shiftEncrypt(String text, int key) {
        return shift(text, key);
    }

    public static String shiftDecrypt(String text, int key) {
        return shift(text, ALPHABET_SIZE - key);
    }

    private static String shift(String text, int shift) {
        StringBuilder result = new StringBuilder();
        for (char character : text.toCharArray()) {
            if (Character.isLetter(character)) {
                char base = Character.isLowerCase(character) ? 'a' : 'A';
                character = (char) ((character - base + shift + ALPHABET_SIZE) % ALPHABET_SIZE + base);
            }
            result.append(character);
        }
        return result.toString();
    }

    // Affine Cipher methods
    public static String affineEncrypt(String text, int a, int b) {
        return affine(text, a, b);
    }

    public static String affineDecrypt(String text, int a, int b) {
        int a_inv = 0;
        for (int i = 1; i < ALPHABET_SIZE; i++) {
            if ((a * i) % ALPHABET_SIZE == 1) {
                a_inv = i;
                break;
            }
        }
        return affine(text, a_inv, -b);
    }

    private static String affine(String text, int a, int b) {
        StringBuilder result = new StringBuilder();
        for (char character : text.toCharArray()) {
            if (Character.isLetter(character)) {
                char base = Character.isLowerCase(character) ? 'a' : 'A';
                character = (char) (((a * (character - base) + b) % ALPHABET_SIZE + ALPHABET_SIZE) % ALPHABET_SIZE + base);
            }
            result.append(character);
        }
        return result.toString();
    }

    // DSA key generation
    public static KeyPair generateDSAKeyPair() throws NoSuchAlgorithmException {
        KeyPairGenerator generator = KeyPairGenerator.getInstance("DSA");
        generator.initialize(2048);
        return generator.generateKeyPair();
    }

    // DSA message signing
    public static String signMessage(String message, PrivateKey privateKey) throws Exception {
        Signature signature = Signature.getInstance("SHA256withDSA");
        signature.initSign(privateKey);
        signature.update(message.getBytes());
        byte[] sigBytes = signature.sign();
        return Base64.getEncoder().encodeToString(sigBytes);
    }

    // DSA signature verification
    public static boolean verifySignature(String message, String signature, PublicKey publicKey) throws Exception {
        Signature sig = Signature.getInstance("SHA256withDSA");
        sig.initVerify(publicKey);
        sig.update(message.getBytes());
        return sig.verify(Base64.getDecoder().decode(signature));
    }
}
