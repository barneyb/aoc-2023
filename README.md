# Advent of Code 2023

The yearly repo, seeded with a few solvers for random problems from prior years.
If you don't know what [Advent of Code](https://adventofcode.com) is, you should
go see! It's both lovely, and will help make sense of this repo. :)

https://github.com/barneyb/aoc2017 has an index, if you want my details.

## _Python_ Solvers

I don't really know what I'm doing. Please assume that if something seems weird
it's probably just my inexperience/unfamiliarity with Python and its ecosystem.

The code uses [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data)
to manage inputs. So install that, configure your token (see the second section
of the readme), and you should be able to get _your_ answers with _my_ solvers.

## _Java_ Solvers

I have opted to package the puzzle input files as classpath resources, rather
that loading them from the filesystem at runtime. This is almost entirely to
facilitate easy use of the real puzzles as integration tests, since part of what
I think is fun is evolving the _set_ of solvers through the yearly puzzle space.
2019 required it - via the Intcode virtual machine - but there are simpler
primitives present in every year. 2D mazes, anyone?

The `Input(year,day)` constructor is the only thing aware of this, so trivial to
refactor if you have different needs/wants. I didn't bother.
