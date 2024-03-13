cmake_minimum_required (VERSION 2.8)

project(cpp_programs)

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(webcam src/webcam.cpp)
target_link_libraries(webcam ${OpenCV_LIBS})

add_executable(version src/cv_ver.cpp)
target_link_libraries(version ${OpenCV_LIBS})

add_executable(face src/facefinder.cpp)
target_link_libraries(face ${OpenCV_LIBS})

add_executable(gridfinder src/grid_finder.cpp)
target_link_libraries(gridfinder ${OpenCV_LIBS})

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")
