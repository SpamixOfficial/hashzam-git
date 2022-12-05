
# Maintainer: SpamixOfficial <spamixofficial@gmail.com>
pkgname=hashzam-git
pkgver=1.0.r4.9259d14
pkgrel=1
pkgdesc="A simple command line tool written in python that calculate and compare hashes!"
arch=(x86_64)
url="https://github.com/SpamixOfficial/hashzam-git-aur.git"
license=('GPL-3.0')
depends=()
makedepends=(git python-pip python)
optdepends=()
provides=(hashzam)
source=("git+$url")
md5sums=('SKIP')

pkgver() {
	cd "${_pkgname}"
	printf "1.0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {

	pip install colorama
}

package() {
	cd hashzam-git-aur
	chmod +x hashzam.py 
	cp hashzam.py "$/usr/local/bin/hashzam"
	cp LICENSE "/usr/share/licenses/${pkgname}/LICENSE"
	cp README.md "/usr/share/doc/${pkgname}/README.md"
}
