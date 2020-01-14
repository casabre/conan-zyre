from conans import ConanFile, CMake, tools
from sys import platform
import re
import os


class ZyreConan(ConanFile):
    name = "zyre"
    version = "2.0.0"
    license = "MPL-2.0"
    url = "https://github.com/zeromq/zyre.git"
    description = "Zyre - Local Area Clustering for Peer-to-Peer Applications."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False], }
    default_options = {"shared": True,
                       "fPIC": True, }
    generators = "cmake"

    def requirements(self):
        self.requires("czmq/4.2.0@conan/stable")

    def source(self):
        git = tools.Git()
        git.clone(self.url, "v%s" % self.version, shallow=True)

    def system_requirements(self):
        pass

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder='cmake-build')
        return cmake

    def build(self):
        tools.replace_in_file("CMakeLists.txt", "project(zyre)",
                              '''project(zyre)
                              include(${CMAKE_CURRENT_SOURCE_DIR}/conanbuildinfo.cmake)
                              conan_basic_setup()''')
        env_build = self._configure_cmake()
        env_build.build()
        env_build.test()

    def package(self):
        self.copy("*.h", dst="include", src="include")
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["zyre"]
