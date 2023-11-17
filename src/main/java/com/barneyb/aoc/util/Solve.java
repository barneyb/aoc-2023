package com.barneyb.aoc.util;

import java.lang.management.GarbageCollectorMXBean;
import java.lang.management.ManagementFactory;
import java.lang.management.MemoryPoolMXBean;
import java.lang.management.MemoryUsage;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;

abstract class Solve<Model> {

    protected abstract Model buildModel(Input input);

    abstract void solve(Model model,
                        Consumer<Info<?>> doneWithPart);

    record Info<T>(T result,
                   long nanos,
                   Mem mem) {

        /**
         * This is used by {@link SolveTogether}.
         */
        @SuppressWarnings("unused")
        Info(T result) {
            this(result, 0, Mem.empty());
        }

        <R> Info<R> map(Function<T, R> map) {
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

    final <T> Info<T> workInfo(Supplier<T> work) {
        Runtime.getRuntime().gc();
        Mem mem = Mem.build();
        long startTime = System.nanoTime();
        T result = work.get();
        return new Info<>(result,
                          System.nanoTime() - startTime,
                          Mem.build().minus(mem));
    }

    public final void solveAndPrint() {
        Info<Model> model = workInfo(() -> buildModel(getInput()));
        System.out.println("Load Data");
        System.out.println(info(model));
        AtomicInteger pn = new AtomicInteger();
        solve(model.result, a -> {
            System.out.println("Part " + part(pn.incrementAndGet()) + ": " + answer(a.result));
            if (a.nanos > 0) System.out.println(info(a));
        });
    }

    Input getInput() {
        return Input.of(getClass());
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

    public void test(Object... expected) {
        Model model = buildModel(getInput());
        List<Object> actual = new ArrayList<>();
        test(model, actual::add);
        Iterator<Object> itr = actual.iterator();
        for (Object e : expected) {
            if (!itr.hasNext()) throw new RuntimeException(String.format(
                    "Too many expected answers provided; '%s' has no corresponding solution",
                    e));
            Object a = itr.next();
            // let assertions use ints for long too
            if (e instanceof Integer i && a instanceof Long) {
                e = i.longValue();
            }
            if (!Objects.equals(e, a)) throw new AssertionError(String.format(
                    "Expected '%s' but got '%s'",
                    e,
                    a));
        }
    }

    abstract void test(Model model,
                       Consumer<Object> solutionConsumer);

}
