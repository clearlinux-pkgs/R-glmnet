#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-glmnet
Version  : 2.0.5
Release  : 29
URL      : http://cran.r-project.org/src/contrib/glmnet_2.0-5.tar.gz
Source0  : http://cran.r-project.org/src/contrib/glmnet_2.0-5.tar.gz
Summary  : Lasso and Elastic-Net Regularized Generalized Linear Models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-glmnet-lib
Requires: R-evaluate
Requires: R-foreach
BuildRequires : R-evaluate
BuildRequires : R-foreach
BuildRequires : clr-R-helpers
BuildRequires : gfortran

%description
No detailed description available

%package lib
Summary: lib components for the R-glmnet package.
Group: Libraries

%description lib
lib components for the R-glmnet package.


%prep
%setup -q -c -n glmnet

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489127877

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1489127877
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library glmnet
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library glmnet


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/glmnet/CITATION
/usr/lib64/R/library/glmnet/DESCRIPTION
/usr/lib64/R/library/glmnet/INDEX
/usr/lib64/R/library/glmnet/Meta/Rd.rds
/usr/lib64/R/library/glmnet/Meta/data.rds
/usr/lib64/R/library/glmnet/Meta/hsearch.rds
/usr/lib64/R/library/glmnet/Meta/links.rds
/usr/lib64/R/library/glmnet/Meta/nsInfo.rds
/usr/lib64/R/library/glmnet/Meta/package.rds
/usr/lib64/R/library/glmnet/Meta/vignette.rds
/usr/lib64/R/library/glmnet/NAMESPACE
/usr/lib64/R/library/glmnet/R/glmnet
/usr/lib64/R/library/glmnet/R/glmnet.rdb
/usr/lib64/R/library/glmnet/R/glmnet.rdx
/usr/lib64/R/library/glmnet/data/BinomialExample.RData
/usr/lib64/R/library/glmnet/data/CVXResults.RData
/usr/lib64/R/library/glmnet/data/CoxExample.RData
/usr/lib64/R/library/glmnet/data/MultiGaussianExample.RData
/usr/lib64/R/library/glmnet/data/MultinomialExample.RData
/usr/lib64/R/library/glmnet/data/PoissonExample.RData
/usr/lib64/R/library/glmnet/data/QuickStartExample.RData
/usr/lib64/R/library/glmnet/data/SparseExample.RData
/usr/lib64/R/library/glmnet/doc/Coxnet.R
/usr/lib64/R/library/glmnet/doc/Coxnet.pdf
/usr/lib64/R/library/glmnet/doc/Coxnet.rnw
/usr/lib64/R/library/glmnet/doc/glmnet_beta.R
/usr/lib64/R/library/glmnet/doc/glmnet_beta.Rmd
/usr/lib64/R/library/glmnet/doc/glmnet_beta.html
/usr/lib64/R/library/glmnet/doc/index.html
/usr/lib64/R/library/glmnet/help/AnIndex
/usr/lib64/R/library/glmnet/help/aliases.rds
/usr/lib64/R/library/glmnet/help/glmnet.rdb
/usr/lib64/R/library/glmnet/help/glmnet.rdx
/usr/lib64/R/library/glmnet/help/paths.rds
/usr/lib64/R/library/glmnet/html/00Index.html
/usr/lib64/R/library/glmnet/html/R.css
/usr/lib64/R/library/glmnet/libs/symbols.rds
/usr/lib64/R/library/glmnet/mortran/glmnet5.m

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/glmnet/libs/glmnet.so
