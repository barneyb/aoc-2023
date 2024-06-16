package com.barneyb.aoc.aoc2023.day24;

public record Ratio(long num, long denom) {

    public static final Ratio ZERO = Ratio.of(0);
    public static final Ratio ONE = Ratio.of(1);

    public static Ratio of(long n) {
        return new Ratio(n, 1);
    }

    public static Ratio of(long num, long denom) {
        return new Ratio(num, denom);
    }

    public Ratio add(long n) {
        return of(num + n * denom, denom).reduce();
    }

    public Ratio add(Ratio r) {
        if (denom == r.denom)
            return of(num + r.num, denom).reduce();
        var lcm = Factors.lcm(denom, r.denom);
        var lf = lcm / denom;
        var rf = lcm / r.denom;
        return of(num * lf + r.num * rf, lcm).reduce();
    }

    public Ratio subtract(long n) {
        return add(-n);
    }

    public Ratio subtract(Ratio r) {
        return add(r.multiply(-1));
    }

    public Ratio multiply(long n) {
        if (n == 0) return ZERO;
        return of(num * n, denom).reduce();
    }

    public Ratio multiply(Ratio r) {
        if (ZERO.equals(this) || ZERO.equals(r)) return ZERO;
        return of(num * r.num, denom * r.denom).reduce();
    }

    public Ratio divide(long n) {
        if (n == 0)
            throw new ArithmeticException("/ by zero");
        return of(num, denom * n).reduce();
    }

    public Ratio divide(Ratio r) {
        if (ZERO.equals(r))
            throw new ArithmeticException("/ by zero");
        return multiply(r.invert());
    }

    private Ratio invert() {
        return Ratio.of(denom, num);
    }

    public boolean isIntegral() {
        return denom == 1 || reduce().denom == 1;
    }

    public Ratio reduce() {
        var gcd = Factors.gcd(num, denom);
        if (denom < 0) gcd = -gcd;
        return of(num / gcd, denom / gcd);
    }

    @Override
    public String toString() {
        return isIntegral()
                ? Long.toString(num)
                : "%d/%d".formatted(num, denom);
    }

}
