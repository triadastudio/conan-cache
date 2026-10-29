from conan import ConanFile

class ConanCache(ConanFile):
    settings = "arch", "build_type", "compiler", "os"
    requires = (
        "imgui/1.92.8",
        "miniaudio/0.11.22",
        "rapidjson/cci.20250205",
        "spdlog/1.17.0",
        "toml11/4.4.0",
        "zstd/1.5.7",
    )

    def requirements(self):
        if self.settings.os in ["Windows", "Linux"]:
            self.requires("glfw/3.4")
        if self.settings.os == "Linux":
            self.requires("libcurl/8.23.0")
            # libcurl asks for version ranges, pin them so a newer ConanCenter release still finds these binaries
            self.requires("openssl/3.6.5", override=True)
            self.requires("zlib/1.3.2", override=True)
        if self.settings.os in ["Windows", "Linux", "Macos"]:
            self.requires("gtest/1.17.0")
