# c-template

Template respository for C/C++ projects.

---

[![Latest Release][release-badge]][release-url]
[![License][license-badge]](LICENSE)
[![CI Status][ci-badge]][ci-url]

---

## Build

To clone the repository on your local machine, please run the following git command in the terminal:
`git clone https://github.com/austinlucaslake/c-template.git`

Assuming [Conan][conan-url] is installed, you may build and run this project as follows:
`conan build . -b=missing -pr=profile && ./build/Release/main`

Similarly, to build and run the program in debug mode, the following command may be used instead: 
`conan build . -b=missing -pr=profile -s=build_type=Debug && ./build/Debug/main`

[release-badge]: https://img.shields.io/github/v/release/austinlucaslake/c-template
[release-url]: https://github.com/austinlucaslake/c-template/releases/latest
[license-badge]: https://img.shields.io/github/license/austinlucaslake/c-template
[ci-badge]: https://github.com/austinlucaslake/c-template/actions/workflows/ci.yaml/badge.svg
[ci-url]: https://github.com/austinlucaslake/c-template/actions
