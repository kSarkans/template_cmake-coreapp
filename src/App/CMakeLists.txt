project(ExampleApp LANGUAGES CXX)

add_executable(exapp)

file(GLOB_RECURSE EXAPP_SOURCES "*.cpp")

target_sources(exapp PRIVATE ${EXAPP_SOURCES})

# Link application with it's libraries
target_link_libraries(exapp PUBLIC
    excore
)