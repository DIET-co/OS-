import java.security.KeyPair;
public class CryptoConfig {
    int shiftKey;
    int affineA;
    int affineB;
    KeyPair dsaKeyPair;

    public CryptoConfig(int shiftKey, int affineA, int affineB, KeyPair dsaKeyPair) {
        this.shiftKey = shiftKey;
        this.affineA = affineA;
        this.affineB = affineB;
        this.dsaKeyPair = dsaKeyPair;
    }
}
