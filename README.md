# TI MSP432: development platform for [PlatformIO](http://platformio.org)

The MSP432 is a mixed-signal microcontroller family from Texas Instruments. It is based on a 32-bit ARM Cortex-M4F CPU, and extends their 16-bit MSP430 line, with a larger address space for code and data, and faster integer and floating point calculation than the MSP430. Like the MSP430, it has a number of built-in peripheral devices, and is designed for low power requirements
* [Datasheet](https://academics.uccs.edu/mlaubhan/common/MSP432/slau597b.pdf) (MSP‑EXP432P401R LaunchPad™ Development Kit)
* [Datasheet](https://www.ti.com/lit/ds/slas826e/slas826e.pdf) (MSP432P401R microcontroller)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = timsp432
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/zceemja/platform-timsp432.git
board = ...
...
```

