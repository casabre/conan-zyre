# see https://github.com/zeromq/czmq/blob/master/Findlibzmq.cmake

if(CONAN_INCLUDE_DIRS_ZYRE AND CONAN_LIB_DIRS_ZMQ AND CONAN_LIBS_ZYRE)
	find_path(ZYRE_INCLUDE_DIR NAMES zyre.h zyre_library.h  PATHS ${CONAN_INCLUDE_DIRS_ZYRE} NO_CMAKE_FIND_ROOT_PATH)
	find_library(ZYRE_LIBRARY NAMES ${CONAN_LIBS_ZYRE} PATHS ${CONAN_LIB_DIRS_ZYRE} NO_CMAKE_FIND_ROOT_PATH)
else()
	find_path(ZYRE_INCLUDE_DIR NAMES zyre.h zyre_library.h )
	find_library(ZYRE_LIBRARY NAMES libzyre)
endif()

set(ZYRE_FOUND ON)
set(ZYRE_INCLUDE_DIRS ${ZYRE_INCLUDE_DIR})
set(ZYRE_LIBRARIES ${ZYRE_LIBRARY})

message(STATUS "zyre found by conan!")
message(STATUS "ZYRE_INCLUDE_DIR: ${ZYRE_INCLUDE_DIR}")
message(STATUS "ZYRE_LIBRARY: ${ZYRE_LIBRARY}")
