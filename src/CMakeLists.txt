set(CMAKE_CXX_STANDARD 20)

add_compile_definitions(
    "$<$<CONFIG:Debug>:EX_DEBUG>"
    "$<$<CONFIG:Release>:NDEBUG>"
)

if(UNIX)
    add_compile_definitions(EX_PLATFORM_UNIX)
endif()

if(WINDOWS)
    add_compile_definitions(EX_PLATFORM_WINDOWS)
elseif(LINUX)
    add_compile_definitions(EX_PLATFORM_LINUX)
    add_compile_definitions(EX_PLATFORM_LINUXBSD)
elseif(BSD)
    add_compile_definitions(EX_PLATFORM_BSD)
    add_compile_definitions(EX_PLATFORM_LINUXBSD)
elseif(MACOS)
    add_compile_definitions(EX_PLATFORM_MACOS)
endif()

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/Include
)

add_subdirectory(Core)
add_subdirectory(App)
