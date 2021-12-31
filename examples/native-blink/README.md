How to build PlatformIO based project
=====================================

1. [Install PlatformIO Core](http://docs.platformio.org/page/core.html)
2. Download examples directory
3. Extract ZIP archive
4. Run these commands:

```shell
# Change directory to example
$ cd platform-timsp432/examples/native-blink

# Build project
$ pio run

# Upload firmware
$ pio run --target upload

# Clean build files
$ pio run --target clean
```
