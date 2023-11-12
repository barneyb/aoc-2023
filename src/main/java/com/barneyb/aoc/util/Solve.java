package com.barneyb.aoc.util;

import java.lang.management.GarbageCollectorMXBean;
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryPoolMXBean;
import java.lang.management.MemoryUsage;
import java.time.Month;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;

abstract class Solve<Model> {

    private static final int FIRST_YEAR = 2015;
    private static final int FIRST_DAY = 1;
    private static final int LAST_DAY = 25;

    private final int year;
    private final int day;

    protected Solve(int year, int day) {
        validateDay(year, day);
        this.year = year;
        this.day = day;
    }

    private void validateDay(int year, int day) {
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
        int maxDay = LAST_DAY;
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

    protected abstract Model buildModel(Input input);

    abstract void solve(Model model,
                        Consumer<Info<?>> doneWithPart);

    protected record Info<T>(T result,
                             long nanos,
                             Mem mem) {

        public Info(T result) {
            this(result, 0, Mem.empty());
        }

        public <R> Info<R> map(Function<T, R> map) {
            return new Info<>(map.apply(result),
                              nanos,
                              mem);
        }

    }

    private record Mem(long bytes, long gcCount, long gcMillis) {

        static Mem empty() {
            return new Mem(0, 0, 0);
        }

        static Mem build() {
            long gcMillis = 0;
            long gcCount = 0;
            long bytes = 0;

            List<GarbageCollectorMXBean> gcBeans = ManagementFactory.getGarbageCollectorMXBeans();
            for (GarbageCollectorMXBean gc : gcBeans) {
                gcCount += gc.getCollectionCount();
                gcMillis += gc.getCollectionTime();
            }

            List<MemoryPoolMXBean> memoryPoolMXBeans = ManagementFactory.getMemoryPoolMXBeans();
            for (MemoryPoolMXBean pool : memoryPoolMXBeans) {
                MemoryUsage usage = pool.getUsage();
                bytes += usage.getUsed();
            }

            return new Mem(bytes, gcCount, gcMillis);
        }

        Mem minus(Mem other) {
            return new Mem(bytes - other.bytes,
                           gcCount - other.gcCount,
                           gcMillis - other.gcMillis);
        }

    }

    protected final <T> Info<T> workInfo(Supplier<T> work) {
        Runtime.getRuntime().gc();
        Mem mem = Mem.build();
        long startTime = System.nanoTime();
        T result = work.get();
        return new Info<>(result,
                          System.nanoTime() - startTime,
                          Mem.build().minus(mem));
    }

    public final void solveAndPrint() {
        Input input = Input.of(year, day);
        Info<Model> model = workInfo(() -> buildModel(input));
        System.out.println("Load Data");
        System.out.println(info(model));
        AtomicInteger pn = new AtomicInteger();
        solve(model.result, a -> {
            System.out.println("Part " + part(pn.incrementAndGet()) + ": " + answer(a.result));
            if (a.nanos > 0) System.out.println(info(a));
        });
    }

    private String part(int i) {
        if (i == 1) return "One";
        if (i == 2) return "Two";
        return Integer.toString(i);
    }

    private String answer(Object value) {
        StringBuilder sb = new StringBuilder();
        String s = Objects.toString(value);
        if (s.contains("\n")) {
            for (String l : s.split("\\n")) {
                sb.append('\n').append(l);
            }
        } else {
            sb.append(s);
        }
        return sb.toString();
    }

    @SuppressWarnings("IntegerDivisionInFloatingPointContext")
    private String info(Info<?> info) {
        StringBuilder sb = new StringBuilder();
        sb.append("    runtime: ")
                .append(info.nanos / 10_000 / 100.0)
                .append(" ms\n");
        Mem mem = info.mem;
        if (mem.gcCount == 0) {
            sb.append("     ~alloc: ")
                    .append(mem.bytes / 1_000 / 1000.0)
                    .append(" MB");
        } else {
            sb.append("        GCs: ")
                    .append(mem.gcCount)
                    .append('\n');
            sb.append("    GC time: ")
                    .append(mem.gcMillis)
                    .append(" ms");
        }
        return sb.toString();
    }

}
