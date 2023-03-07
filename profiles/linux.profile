[settings]
os=Linux
arch=x86_64
compiler=clang
compiler.version=13
compiler.libcxx=libstdc++11
compiler.cppstd=20

[buildenv]
CC=/usr/bin/clang-13
CXX=/usr/bin/clang++-13

[conf]
tools.system.package_manager:mode=install
tools.system.package_manager:sudo=True
