#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.35.1
Release  : 75
URL      : https://files.pythonhosted.org/packages/83/72/611c121b6bd15479cb62f1a425b2e3372e121b324228df28e64cc28b01c2/wheel-0.35.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/72/611c121b6bd15479cb62f1a425b2e3372e121b324228df28e64cc28b01c2/wheel-0.35.1.tar.gz
Summary  : A built-package format for Python
Group    : Development/Tools
License  : MIT
Requires: wheel-bin = %{version}-%{release}
Requires: wheel-python = %{version}-%{release}
Requires: wheel-python3 = %{version}-%{release}
Requires: keyring
BuildRequires : buildreq-distutils3
BuildRequires : jsonschema-python
BuildRequires : keyring
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wheel

%description
=====
        
        This library is the reference implementation of the Python wheel packaging
        standard, as defined in `PEP 427`_.

%package bin
Summary: bin components for the wheel package.
Group: Binaries

%description bin
bin components for the wheel package.


%package python
Summary: python components for the wheel package.
Group: Default
Requires: wheel-python3 = %{version}-%{release}

%description python
python components for the wheel package.


%package python3
Summary: python3 components for the wheel package.
Group: Default
Requires: python3-core
Provides: pypi(wheel)

%description python3
python3 components for the wheel package.


%prep
%setup -q -n wheel-0.35.1
cd %{_builddir}/wheel-0.35.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597683324
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wheel

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
