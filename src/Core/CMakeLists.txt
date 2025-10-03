project(ExampleCore LANGUAGES CXX)

if(EX_BUILD_SHARED)
    add_library(excore SHARED)
else()
    add_library(excore STATIC)
endif()

# Add source files recursively
file(GLOB_RECURSE CORE_SOURCES "*.cpp")

target_sources(excore PRIVATE ${CORE_SOURCES})