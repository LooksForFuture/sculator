cmake_minimum_required(VERSION 3.16)

project(myculator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set (CMAKE_AUTOMOC ON)

find_package(Qt6 REQUIRED COMPONENTS Widgets)
qt_standard_project_setup()

set(EXE_NAME sculator)
qt_add_executable(${EXE_NAME}
    sculator.hpp
    sculator.cpp

    main.cpp
)

target_link_libraries(${EXE_NAME} PRIVATE Qt6::Widgets)

target_include_directories(${EXE_NAME} PRIVATE
    ${Qt6Core_INCLUDE_DIRS}
    ${Qt6Widgets_INCLUDE_DIRS}
)


target_link_libraries(${EXE_NAME}
    PUBLIC
        ${Qt6Core_LIBRARIES}
        ${Qt6Widgets_LIBRARIES}
)
