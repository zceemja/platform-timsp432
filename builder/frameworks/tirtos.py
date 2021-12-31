"""
Based on https://github.com/energia/msp432r-core
References https://energia.nu/reference/
"""

from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()

FRAMEWORK_DIR = platform.get_package_dir("framework-energiamsp432r")
FRAMEWORK_VERSION = platform.get_package_version("framework-energiamsp432r")
assert isdir(FRAMEWORK_DIR)

board = env.BoardConfig()

variants_dir = join(
    "$PROJECT_DIR", board.get("build.variants_dir")) if board.get(
        "build.variants_dir", "") else join(FRAMEWORK_DIR, "variants")

env.Append(
    CPPDEFINES=[
        ("CORE_VERSION", 5252),
        ("xdc_target_types__", "gnu/targets/arm/std.h"),
        ("xdc_target_name__", "M4F"),
        ("xdc_cfg__xheader__", '\\"configPkg/package/cfg/energia_pm4fg.h\\"'),
        ("xdc__nolocalstring", 1),
        "_DEFAULT_SOURCE",
    ],

    CPPPATH=[
        join(variants_dir, board.get("build.variant")),
        join(FRAMEWORK_DIR, 'system/source'),
        join(FRAMEWORK_DIR, 'system/energia'),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core")),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core"), 'ti/runtime/wiring'),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core"), 'ti/runtime/wiring/msp432'),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/packages/ti/sysbios/posix'),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/packages'),
        join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/driverlib'),
        join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/inc'),
        join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/'),
        join(FRAMEWORK_DIR, 'system/source/third_party/CMSIS/Include'),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/boards', board.get("build.variant")),
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ],

    LINKFLAGS=[
        "-nostartfiles",
        "-Wl,-u,main",
        "-Wl,-u,_printf_float,-u,-_scanf_float",
        "-Wl,--check-sections",
        "-Wl,--gc-sections",
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "cores", board.get("build.core")),
        join(FRAMEWORK_DIR, 'system/kernel'),
        join(FRAMEWORK_DIR, 'system/source'),
        join(FRAMEWORK_DIR, 'system/energia'),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/packages'),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core")),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core"), 'ti/runtime/wiring/msp432'),
        join(FRAMEWORK_DIR, 'cores', board.get("build.core"), 'ti/runtime/wiring/msp432/variants', board.get("build.variant")),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/packages/gnu/targets/arm/libs/install-native/arm-none-eabi/lib/thumb/v7e-m/fpv4-sp/hard'),
    ],

    _LIBDIRFLAGS=[
        '-Wl,-T' + join(FRAMEWORK_DIR, "system/energia/linker.cmd"),
    ],

    LIBS=[
        env.File(join(FRAMEWORK_DIR, "system/source/ti/devices/msp432p4xx/driverlib/gcc/msp432p4xx_driverlib.a")),
    ],
)