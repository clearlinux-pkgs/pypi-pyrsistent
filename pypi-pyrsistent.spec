#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyrsistent
Version  : 0.18.1
Release  : 65
URL      : https://files.pythonhosted.org/packages/42/ac/455fdc7294acc4d4154b904e80d964cc9aae75b087bbf486be04df9f2abd/pyrsistent-0.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/ac/455fdc7294acc4d4154b904e80d964cc9aae75b087bbf486be04df9f2abd/pyrsistent-0.18.1.tar.gz
Summary  : Persistent/Functional/Immutable data structures
Group    : Development/Tools
License  : MIT
Requires: pypi-pyrsistent-filemap = %{version}-%{release}
Requires: pypi-pyrsistent-lib = %{version}-%{release}
Requires: pypi-pyrsistent-license = %{version}-%{release}
Requires: pypi-pyrsistent-python = %{version}-%{release}
Requires: pypi-pyrsistent-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)
Patch1: 0001-tests.patch

%description
Pyrsistent
==========
.. image:: https://github.com/tobgu/pyrsistent/actions/workflows/tests.yaml/badge.svg
:target: https://github.com/tobgu/pyrsistent/actions/workflows/tests.yaml

%package filemap
Summary: filemap components for the pypi-pyrsistent package.
Group: Default

%description filemap
filemap components for the pypi-pyrsistent package.


%package lib
Summary: lib components for the pypi-pyrsistent package.
Group: Libraries
Requires: pypi-pyrsistent-license = %{version}-%{release}
Requires: pypi-pyrsistent-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyrsistent package.


%package license
Summary: license components for the pypi-pyrsistent package.
Group: Default

%description license
license components for the pypi-pyrsistent package.


%package python
Summary: python components for the pypi-pyrsistent package.
Group: Default
Requires: pypi-pyrsistent-python3 = %{version}-%{release}

%description python
python components for the pypi-pyrsistent package.


%package python3
Summary: python3 components for the pypi-pyrsistent package.
Group: Default
Requires: pypi-pyrsistent-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyrsistent)

%description python3
python3 components for the pypi-pyrsistent package.


%prep
%setup -q -n pyrsistent-0.18.1
cd %{_builddir}/pyrsistent-0.18.1
%patch1 -p1
pushd ..
cp -a pyrsistent-0.18.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400098
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyrsistent
cp %{_builddir}/pyrsistent-0.18.1/LICENSE.mit %{buildroot}/usr/share/package-licenses/pypi-pyrsistent/4fdb72bba2df212e4c64c262eaebc0c2ac87cb6d
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyrsistent

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyrsistent/4fdb72bba2df212e4c64c262eaebc0c2ac87cb6d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
