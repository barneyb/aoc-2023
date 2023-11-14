package com.barneyb.aoc.util;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public final class Digest {

    private Digest() {
        throw new UnsupportedOperationException("really?");
    }

    public static String toHex(byte[] bytes, int length) {
        String s = new BigInteger(bytes).toString(16);
        int deficient = length - s.length();
        if (deficient > 0) s = "0".repeat(deficient) + s;
        return s;
    }

    public static byte[] md5(Object... data) {
        String algorithm = "MD5";
        try {
            MessageDigest md = MessageDigest.getInstance(algorithm);
            for (Object d : data) {
                if (d instanceof byte[]) {
                    md.update(((byte[]) d));
                } else if (d instanceof Byte) {
                    md.update(((Byte) d));
                } else {
                    md.update(d.toString().getBytes());
                }
            }
            return md.digest();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(String.format(
                    "No '%s' digest algorithm is known",
                    algorithm), e);
        }
    }

    public static String md5hex(Object... data) {
        return toHex(md5(data), 32);
    }

}
