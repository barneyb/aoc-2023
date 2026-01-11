package com.barneyb.aoc.util;

import lombok.SneakyThrows;
import org.reflections.Reflections;

import java.util.List;
import java.util.Objects;
import java.util.stream.Stream;

/**
 * I implement the aoc-all protocol. Run me as either:
 *
 * <ul>
 *     <li>{@code AocAll support} to print a list of supported days as
 *     {@code year,day} CSV records (e.g., {@code 2015,1}).
 *     </li>
 *     <li>{@code AocAll solve 2015 1} to print the given problem's answers as
 *     {@code part,answer} as CSV records (e.g., {@code a,123}). If an answer
 *     contains newline, comma, or double-quote, any double-quotes will be
 *     doubled, and the entire answer double-quoted. If a part has no answer,
 *     a record will not be emitted.
 *     </li>
 * </ul>
 */
public class AocAll {

    public static void main(String[] args) {
        if (args.length == 0) throw new RuntimeException("Expected at least one argument");
        var aa = new AocAll();
        switch (args[0]) {
            case "support" -> {
                if (args.length != 1) throw new RuntimeException("'support' expects zero additional args");
                for (Day d : aa.support()) {
                    System.out.println(d.year + "," + d.day);
                }
            }
            case "solve" -> {
                if (args.length != 4)
                    throw new RuntimeException("'solve' expects three additional args (year, day, input_filename");
                var d = new Day(Integer.parseInt(args[1]),
                                Integer.parseInt(args[2]));
                var info = aa.solve(d, new TempFileInputSupplier(args[3]));
                var ans = info.result();
                printRow("a", ans.partOne());
                printRow("b", ans.partTwo());
                printRow("nanos", info.nanos());
            }
            default -> throw new RuntimeException("Unrecognized '" + args[0] + "' command");
        }
    }

    private static void printRow(String key, Object value) {
        String s = Objects.toString(value);
        if (s == null || s.isBlank()) {
            System.out.println(key + ',');
        } else if (s.contains("\n")
                   || s.contains(",")
                   || s.contains("\"")) {
            System.out.println(key + ",\"" + s.replace("\"", "\"\"") + '"');
        } else {
            System.out.println(key + ',' + s);
        }
    }

    public record Day(int year,
                      int day) implements Comparable<Day> {

        @Override
        public int compareTo(Day o) {
            int c = year - o.year;
            return c != 0 ? c : (day - o.day);
        }

    }

    public List<Day> support() {
        return streamSolverTypes("com.barneyb.aoc")
                .map(Class::getPackageName)
                .map(pkg -> pkg.split("\\."))
                .filter(parts -> parts[3].startsWith("aoc"))
                .map(parts -> List.of(
                        parts[3].substring(3),
                        parts[4].substring(3)))
                .map(parts -> parts.stream()
                        .map(Integer::parseInt)
                        .iterator())
                .map(parts -> new Day(
                        parts.next(),
                        parts.next()))
                .distinct()
                .sorted()
                .toList();
    }

    @SuppressWarnings("rawtypes")
    private Stream<Class<? extends Solve>> streamSolverTypes(String pkgName) {
        Reflections reflections = new Reflections(pkgName);
        return reflections.getSubTypesOf(Solve.class)
                .stream()
                .filter(c -> c.getPackageName().startsWith(pkgName));
    }

    @SneakyThrows
    Solve.Info<Answers<?, ?>> solve(Day d, InputSupplier inputSupplier) {
        @SuppressWarnings("rawtypes")
        List<Class<? extends Solve>> types = streamSolverTypes(String.format(
                "com.barneyb.aoc.aoc%4d.day%02d",
                d.year,
                d.day))
                .toList();
        if (types.isEmpty()) throw new RuntimeException(String.format(
                "No solver for %d/%d found?!",
                d.year,
                d.day));
        if (types.size() > 1) throw new RuntimeException(String.format(
                "Found %d solvers for %d/%d?!",
                types.size(),
                d.year,
                d.day));
        Solve<?> solver = types.get(0)
                .getDeclaredConstructor()
                .newInstance();
        solver.setInputSupplier(inputSupplier);
        return solver.getAnswers();
    }

}
