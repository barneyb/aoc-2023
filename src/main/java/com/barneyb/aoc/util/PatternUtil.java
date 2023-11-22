package com.barneyb.aoc.util;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PatternUtil {

    public static Matcher match(Pattern patt, CharSequence str) {
        var m = patt.matcher(str);
        if (!m.matches()) throw new RuntimeException(String.format(
                "'%s' failed to match '%s'",
                patt,
                str));
        return m;
    }

}
