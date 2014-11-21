project("dbus-player-service")
cmake_minimum_required(VERSION 2.6)

list(APPEND CMAKE_MODULE_PATH
    ${CMAKE_SOURCE_DIR}/cmake/vala_macros/vala
)

#include(ValaPrecompile)
#include(ValaVersion)

find_package(Vala REQUIRED)
find_package(PkgConfig)
pkg_check_modules(DEPS REQUIRED gstreamer-1.0 gio-2.0 gee-0.8)
add_definitions(${DEPS_CFLAGS} ${DEPS_CFLAGS_OTHER})
link_libraries(${DEPS_LIBRARIES})
link_directories(${DEPS_LIBRARY_DIRS})

include(UseVala)

vala_precompile(VALA_C
    "src/player.vala"
    PACKAGES
        gstreamer-1.0
        gio-2.0
        gee-0.8
)

add_executable("player" ${VALA_C})