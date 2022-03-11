#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-kimisc
Version  : 0.4
Release  : 30
URL      : https://cran.r-project.org/src/contrib/kimisc_0.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/kimisc_0.4.tar.gz
Summary  : Kirill's Miscellaneous Functions
Group    : Development/Tools
License  : GPL-3.0
Requires: R-memoise
Requires: R-plyr
Requires: R-pryr
BuildRequires : R-memoise
BuildRequires : R-plyr
BuildRequires : R-pryr
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n kimisc
cd %{_builddir}/kimisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641041905

%install
export SOURCE_DATE_EPOCH=1641041905
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kimisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kimisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library kimisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc kimisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/kimisc/DESCRIPTION
/usr/lib64/R/library/kimisc/INDEX
/usr/lib64/R/library/kimisc/Meta/Rd.rds
/usr/lib64/R/library/kimisc/Meta/features.rds
/usr/lib64/R/library/kimisc/Meta/hsearch.rds
/usr/lib64/R/library/kimisc/Meta/links.rds
/usr/lib64/R/library/kimisc/Meta/nsInfo.rds
/usr/lib64/R/library/kimisc/Meta/package.rds
/usr/lib64/R/library/kimisc/NAMESPACE
/usr/lib64/R/library/kimisc/NEWS.md
/usr/lib64/R/library/kimisc/R/kimisc
/usr/lib64/R/library/kimisc/R/kimisc.rdb
/usr/lib64/R/library/kimisc/R/kimisc.rdx
/usr/lib64/R/library/kimisc/help/AnIndex
/usr/lib64/R/library/kimisc/help/aliases.rds
/usr/lib64/R/library/kimisc/help/kimisc.rdb
/usr/lib64/R/library/kimisc/help/kimisc.rdx
/usr/lib64/R/library/kimisc/help/paths.rds
/usr/lib64/R/library/kimisc/html/00Index.html
/usr/lib64/R/library/kimisc/html/R.css
/usr/lib64/R/library/kimisc/staticdocs/index.R
/usr/lib64/R/library/kimisc/tests/test-all.R
/usr/lib64/R/library/kimisc/tests/testthat/scripts/thisfile-cat.R
/usr/lib64/R/library/kimisc/tests/testthat/scripts/thisfile.R
/usr/lib64/R/library/kimisc/tests/testthat/test-cut.R
/usr/lib64/R/library/kimisc/tests/testthat/test-gdiff.R
/usr/lib64/R/library/kimisc/tests/testthat/test-kimisc.R
/usr/lib64/R/library/kimisc/tests/testthat/test-list_to_df.R
/usr/lib64/R/library/kimisc/tests/testthat/test-thisfile.R
/usr/lib64/R/library/kimisc/tests/testthat/test-vswitch.R
