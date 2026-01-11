package com.barneyb.aoc.util;

import lombok.SneakyThrows;

import javax.annotation.Nonnull;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.time.Month;
import java.time.ZoneId;
import java.time.ZonedDateTime;

class AocdInputSupplier implements InputSupplier {

    private static final int FIRST_YEAR = 2015;
    private static final int FIRST_HALF_YEAR = 2025;
    private static final int FIRST_DAY = 1;
    private static final int LAST_DAY = 25;

    private TempFileInputSupplier fileSupplier;

    @Override
    public void prepare(Solve<?> solve) {
        if (fileSupplier != null) return;
        String[] parts = solve.getClass().getPackageName()
                .split("\\.");
        int year = Integer.parseInt(parts[parts.length - 2].substring(3));
        int day = Integer.parseInt(parts[parts.length - 1].substring(3));
        validateDay(year, day);
        fileSupplier = new TempFileInputSupplier(createTempFile(year, day));
    }

    @Override
    public Input get() {
        if (fileSupplier == null) {
            throw new IllegalStateException("This input supplier has not been prepared");
        }
        return fileSupplier.get();
    }

    private static void validateDay(int year, int day) {
        ZonedDateTime now = ZonedDateTime.now(ZoneId.of("America/New_York"));
        int maxYear = year == now.getYear() && Month.DECEMBER == now.getMonth()
                ? now.getYear()
                : now.getYear() - 1;
        if (year < FIRST_YEAR || year > maxYear) {
            throw new IllegalArgumentException(String.format(
                    "Year must be %s-%s",
                    FIRST_YEAR,
                    maxYear));
        }
        int maxDay = year < FIRST_HALF_YEAR
                ? LAST_DAY
                : LAST_DAY / 2;
        if (year == now.getYear()) {
            // already know it's december
            maxDay = Math.min(maxDay, now.getDayOfMonth());
        }
        if (day < FIRST_DAY || day > maxDay) {
            throw new IllegalArgumentException(String.format(
                    "Day must be %s-%s",
                    FIRST_DAY,
                    maxDay));
        }
    }

    @Nonnull
    @SneakyThrows
    private static File createTempFile(int year, int day)  {
        var f = File.createTempFile("input_%d_%02d_".formatted(year, day), ".txt");
        f.deleteOnExit();
        try (var in = aocd(year, day);
             var out = new BufferedOutputStream(new FileOutputStream(f))) {
            in.transferTo(out);
        }
        return f;
    }

    @Nonnull
    @SneakyThrows
    private static InputStream aocd(int year, int day)  {
        var proc = new ProcessBuilder("aocd", "" + year, "" + day)
                .start();
        if (proc.waitFor() != 0) {
            throw new RuntimeException("Failed to get input from aocd. Is your token expired (or missing)?");
        }
        return proc.getInputStream();
    }

}
