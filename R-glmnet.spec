#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-glmnet
Version  : 4.1.3
Release  : 95
URL      : https://cran.r-project.org/src/contrib/glmnet_4.1-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/glmnet_4.1-3.tar.gz
Summary  : Lasso and Elastic-Net Regularized Generalized Linear Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-glmnet-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-foreach
Requires: R-shape
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-foreach
BuildRequires : R-shape
BuildRequires : buildreq-R
BuildRequires : buildreq-cmake
BuildRequires : gfortran

%description
# Lasso and Elastic-Net Regularized Generalized Linear Models <img src="man/figures/logo.png" width="100" align="right" />

%package lib
Summary: lib components for the R-glmnet package.
Group: Libraries

%description lib
lib components for the R-glmnet package.


%prep
%setup -q -c -n glmnet
cd %{_builddir}/glmnet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635955111

%install
export SOURCE_DATE_EPOCH=1635955111
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glmnet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glmnet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glmnet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc glmnet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/glmnet/CITATION
/usr/lib64/R/library/glmnet/DESCRIPTION
/usr/lib64/R/library/glmnet/INDEX
/usr/lib64/R/library/glmnet/Meta/Rd.rds
/usr/lib64/R/library/glmnet/Meta/data.rds
/usr/lib64/R/library/glmnet/Meta/features.rds
/usr/lib64/R/library/glmnet/Meta/hsearch.rds
/usr/lib64/R/library/glmnet/Meta/links.rds
/usr/lib64/R/library/glmnet/Meta/nsInfo.rds
/usr/lib64/R/library/glmnet/Meta/package.rds
/usr/lib64/R/library/glmnet/Meta/vignette.rds
/usr/lib64/R/library/glmnet/NAMESPACE
/usr/lib64/R/library/glmnet/NEWS.md
/usr/lib64/R/library/glmnet/R/glmnet
/usr/lib64/R/library/glmnet/R/glmnet.rdb
/usr/lib64/R/library/glmnet/R/glmnet.rdx
/usr/lib64/R/library/glmnet/data/BinomialExample.rda
/usr/lib64/R/library/glmnet/data/CVXResults.RData
/usr/lib64/R/library/glmnet/data/CoxExample.rda
/usr/lib64/R/library/glmnet/data/MultiGaussianExample.rda
/usr/lib64/R/library/glmnet/data/MultinomialExample.rda
/usr/lib64/R/library/glmnet/data/PoissonExample.rda
/usr/lib64/R/library/glmnet/data/QuickStartExample.rda
/usr/lib64/R/library/glmnet/data/SparseExample.rda
/usr/lib64/R/library/glmnet/doc/Coxnet.R
/usr/lib64/R/library/glmnet/doc/Coxnet.Rmd
/usr/lib64/R/library/glmnet/doc/Coxnet.pdf
/usr/lib64/R/library/glmnet/doc/glmnet.R
/usr/lib64/R/library/glmnet/doc/glmnet.Rmd
/usr/lib64/R/library/glmnet/doc/glmnet.pdf
/usr/lib64/R/library/glmnet/doc/glmnetFamily.R
/usr/lib64/R/library/glmnet/doc/glmnetFamily.Rmd
/usr/lib64/R/library/glmnet/doc/glmnetFamily.pdf
/usr/lib64/R/library/glmnet/doc/index.html
/usr/lib64/R/library/glmnet/doc/relax.R
/usr/lib64/R/library/glmnet/doc/relax.Rmd
/usr/lib64/R/library/glmnet/doc/relax.pdf
/usr/lib64/R/library/glmnet/help/AnIndex
/usr/lib64/R/library/glmnet/help/aliases.rds
/usr/lib64/R/library/glmnet/help/figures/logo.png
/usr/lib64/R/library/glmnet/help/glmnet.rdb
/usr/lib64/R/library/glmnet/help/glmnet.rdx
/usr/lib64/R/library/glmnet/help/paths.rds
/usr/lib64/R/library/glmnet/html/00Index.html
/usr/lib64/R/library/glmnet/html/R.css
/usr/lib64/R/library/glmnet/mortran/README.Rmd
/usr/lib64/R/library/glmnet/mortran/glmnet5dpclean.m
/usr/lib64/R/library/glmnet/mortran/wls.m
/usr/lib64/R/library/glmnet/testscripts/save_results.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/glmnet/libs/glmnet.so
/usr/lib64/R/library/glmnet/libs/glmnet.so.avx2
/usr/lib64/R/library/glmnet/libs/glmnet.so.avx512
