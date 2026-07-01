from conan import ConanFile

class ConanCache(ConanFile):
    settings = "arch", "build_type", "compiler", "os"
    requires = (
        "imgui/1.92.8",
        "spdlog/1.17.0",
        "rapidjson/cci.20250205",
        "zstd/1.5.7",
        "miniaudio/0.11.22",
        "toml11/4.4.0",
    )

    def requirements(self):
        if self.settings.os in ["Windows", "Linux"]:
            self.requires("glfw/3.4")
        if self.settings.os in ["Windows", "Linux", "Macos"]:
            self.requires("gtest/1.13.0")
