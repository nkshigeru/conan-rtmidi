import os
from conans import ConanFile, CMake, tools


class RtmidiConan(ConanFile):
    name = "rtmidi"
    version = "4.0.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Rtmidi here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    source_subfolder = "rtmidi-{version}".format(version=version)

    def source(self):
        url = "http://www.music.mcgill.ca/~gary/rtmidi/release/rtmidi-{version}.tar.gz".format(version=self.version)
        tools.get(url)

        insert_position = "project(RtMidi LANGUAGES CXX)"
        tools.replace_in_file(os.path.join(self.source_subfolder, "CMakeLists.txt"),
            insert_position, insert_position + '''
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["rtmidi"]
        if self.settings.os == "Windows":
            self.cpp_info.libs.append("winmm")
        elif self.settings.os == 'Macos':
            for framework in ['Foundation',
                              'CoreAudio',
                              'CoreMIDI']:
                self.cpp_info.exelinkflags.append('-framework %s' % framework)
            self.cpp_info.sharedlinkflags = self.cpp_info.exelinkflags

