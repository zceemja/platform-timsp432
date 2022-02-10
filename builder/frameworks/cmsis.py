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

board_name = board.get('build.variant').lower().replace('_exp', '')

env.Replace(
    LIBPATH=[],
)
env.Append(
    CPPPATH=[
        join(variants_dir, board.get("build.variant")),
        join(FRAMEWORK_DIR, 'system/source'),
        join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/driverlib'),
        join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/inc'),
        join(FRAMEWORK_DIR, 'system/source/third_party/CMSIS/Include'),
        join(FRAMEWORK_DIR, 'system/kernel/tirtos/boards', board.get("build.variant")),
    ],

    _LIBDIRFLAGS=[
        '-Wl,-T' + join(FRAMEWORK_DIR, "system/source/ti/devices/msp432p4xx/linker_files/gcc/%s.lds" % board_name),
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ],
)

env.BuildSources(
   join("$BUILD_DIR", "startup_%s" % (board.get("build.core"))),
   join(FRAMEWORK_DIR, 'system/source/ti/devices/msp432p4xx/startup_system_files/'),
   ["+<system_%s.c>" % board_name, "+<gcc/startup_%s_gcc.c>" % board_name]
)
