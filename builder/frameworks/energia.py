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

core_lib = env.BuildLibrary(
    join("$BUILD_DIR", "core_%s" % board.get("build.core")),
    join(FRAMEWORK_DIR, 'cores', board.get("build.core"), 'ti/runtime/wiring'),
),

env.Append(
    CPPDEFINES=[
        ("ARDUINO", 10807),
        ("ENERGIA", int(FRAMEWORK_VERSION.split(".")[1])),
    ],
    _LIBDIRFLAGS=[core_lib],
    LIBS=[core_lib],
)

env.BuildSources(
    join("$BUILD_DIR", "arduino_%s" % (board.get("build.core"))),
    join(FRAMEWORK_DIR, 'extras/arduino'),
)

env.BuildSources(
    join("$BUILD_DIR", "core_%s_%s" % (board.get("build.core"), board.get("build.variant"))),
    join(FRAMEWORK_DIR, 'variants', board.get("build.variant")),
)

env.SConscript("tirtos.py")
