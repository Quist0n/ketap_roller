## Ketap Roller

A basic dice rolling program that allows you to roll an arbitrary
number of dice of an arbitrary number of sides.

## Usage:
```sh
$ ketap_roller.py <die_spec>...
```

``<die_spec>`` is ``[<die_num>d<die_sides>+/-<mod>]``

Where ``die_num`` is the number of dice you want to roll,
``die_sides`` is the amount of sides those dice should have
and ``mod`` is the amount you want to take away or add to the result of the roll

# Examples:
```sh
$ ketap_roller.py 1d20+4 6d4+2 2d12+5 1d10-3
```

You can chain multiple ``<die_spec>`` together in order to roll multiple kinds of dice with modifiers.

# Note

Note that if you try to use a ``<die_spec>`` like ``0d20`` or ``1d1+3`` the program will fail as
at least 1 die is required and 2 sides are required on a die at minimum.
