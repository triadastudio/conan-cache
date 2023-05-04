from conan import ConanFile

class ConanCache(ConanFile):
    settings = "arch", "build_type", "compiler", "os"
    requires = (
        "imgui/1.89.4",
        "spdlog/1.11.0",
        "bullet3/3.25",
        "lodepng/cci.20200615",
        "zstd/1.5.0"
    )

    def requirements(self):
        if self.settings.os in ["Windows", "Linux"]:
            self.requires("glfw/3.3.8")
        if self.settings.os in ["Windows", "Linux", "Macos"]:
            self.requires("gtest/1.13.0")
