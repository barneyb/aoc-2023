package com.barneyb.aoc.util;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.function.Predicate;

/**
 * I am like a <tt>{@link Map}&lt;Bucket, Long&gt;</tt>, but with histogram
 * semantics. In particular, {@link #get} will return zero for unknown buckets,
 * not <tt>null</tt>.
 */
public class Histogram<Bucket> {

    private final Map<Bucket, Long> hist = new HashMap<>();

    public void count(Bucket bucket) {
        count(bucket, 1L);
    }

    public void count(Bucket bucket, Long times) {
        hist.merge(bucket, times, Long::sum);
    }

    public void count(Bucket bucket, int times) {
        count(bucket, (long) times);
    }

    public Long get(Bucket bucket) {
        return hist.getOrDefault(bucket, 0L);
    }

    public int size() {
        return hist.size();
    }

    public Set<Bucket> buckets() {
        return hist.keySet();
    }

    public Set<Bucket> buckets(Predicate<Long> countTest) {
        Set<Bucket> keys = new HashSet<>();
        for (Map.Entry<Bucket, Long> e : hist.entrySet()) {
            if (countTest.test(e.getValue())) {
                keys.add(e.getKey());
            }
        }
        return keys;
    }

}
