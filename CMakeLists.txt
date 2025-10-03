cmake_minimum_required(VERSION 3.30)

project(Example DESCRIPTION "This project is a template!" VERSION 0.1.0 LANGUAGES CXX)

# Output files
set(EX_OUTPUT_BASE_PATH ${CMAKE_BINARY_DIR}/target/$<CONFIG>-${CMAKE_SYSTEM_NAME})
set(EX_OUTPUT_INTERMEDIATE_PATH ${CMAKE_BINARY_DIR}/target/$<CONFIG>-${CMAKE_SYSTEM_NAME}/__obj__)
# Links to source files
set(EX_PROJECTS_DIR ${CMAKE_SOURCE_DIR}/src)
set(EX_VENDOR_DIR ${CMAKE_SOURCE_DIR}/vendor)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${EX_OUTPUT_BASE_PATH})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${EX_OUTPUT_BASE_PATH}/bin)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${EX_OUTPUT_INTERMEDIATE_PATH}/lib)

# Make application libraries shared or static
option(EX_BUILD_SHARED "Build application's libraries as shared libraries." ON)

# Projects
add_subdirectory(src)