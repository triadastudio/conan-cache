from conan import ConanFile

class ConanCache(ConanFile):
    settings = "arch", "build_type", "compiler", "os"
    requires = (
        "imgui/1.91.0",
        "spdlog/1.14.1",
        "bullet3/3.25",
        "lodepng/cci.20200615",
        "zstd/1.5.5"
    )

    def requirements(self):
        if self.settings.os in ["Windows", "Linux"]:
            self.requires("glfw/3.4")
        if self.settings.os in ["Windows", "Linux", "Macos"]:
            self.requires("gtest/1.13.0")
