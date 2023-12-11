from conan import ConanFile

class CompressorRecipe(ConanFile):
    name = "c-template"
    version = "0.1.0"
    license = "Apache-2.0"
    author = "Austin Lucas Lake (53884490+austinlucaslake@users.noreply.github.com)"
    url = "https://github.com/austinlucaslake/c-template"
    description = "Template repository for C/C++ projects."
    topics = ("quaternion", "render", "ASCII")
    settings = "arch", "compiler", "build_type", "os"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def build_requirements(self):
        self.tool_requires("cmake/[>3.23.5]")
        self.test_requires("cppcheck/2.12.1")
        self.test_requires("uncrustify/0.78.0")

    def generate(self):
        toolchain = CMakeToolchain(self)
        toolchain.generate()
        dependancies = CMakeDeps(self)
        dependancies.check_components_exist = True
        dependancies.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def layout(self):
        cmake_layout(self, src_folder="src", build_folder="build")
