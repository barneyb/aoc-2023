import csv
import glob
import importlib
import importlib.util
import os
import subprocess
import tempfile

from util.aoc import entry_point


def is_supported(y, d):
    mod = importlib.import_module(f"aoc{y}.day{d:02}")
    mod_attrs = dir(mod)
    return "part_one" in mod_attrs or "both_parts" in mod_attrs


def support():
    search_pattern = os.path.join("..", "aoc*", "day*", "__init__.py")
    files = glob.glob(
        search_pattern,
        root_dir=os.path.dirname(__file__),
        recursive=True,
    )
    pairs = [(int(y[3:]), int(d[3:])) for y, d in [f.split("/")[1:3] for f in files]]
    return [(y, d) for y, d in pairs if is_supported(y, d)]


def solve(year, day, data):
    return entry_point(year, day, data)


def java_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..")


def java_env():
    return {"JAVA_VERSION": "17"}


def support_java():
    # mvn exec:java --quiet -Dexec.args="support"
    proc = subprocess.run(
        ["./mvnw", "compile", "exec:java", "--quiet", "-Dexec.args=support"],
        cwd=java_dir(),
        env=java_env(),
        capture_output=True,
        text=True,
    )

    return [
        (y, d)
        for y, d in [
            map(int, l) for l in csv.reader(proc.stdout.strip().splitlines(True))
        ]
    ]


def solve_java(year, day, data):
    with tempfile.NamedTemporaryFile(
        mode="w+t", prefix=f"input_{year}_{day}_", suffix=".txt"
    ) as fp:
        fp.write(data)
        fp.flush()
        # mvn exec:java --quiet -Dexec.args="solve 2015 1"
        proc = subprocess.run(
            [
                "./mvnw",
                "exec:java",
                "--quiet",
                f"-Dexec.args=solve {year} {day} {fp.name}",
            ],
            cwd=java_dir(),
            env=java_env(),
            input=data,
            capture_output=True,
            text=True,
        )

    ans = {p: a for p, a in csv.reader(proc.stdout.strip().splitlines(True))}
    return ans["a"], ans["b"]
