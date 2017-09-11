#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.30.0
Release  : 31
URL      : http://pypi.debian.net/wheel/wheel-0.30.0.tar.gz
Source0  : http://pypi.debian.net/wheel/wheel-0.30.0.tar.gz
Summary  : A built-package format for Python.
Group    : Development/Tools
License  : MIT
Requires: wheel-bin
Requires: wheel-legacypython
Requires: wheel-python
Requires: jsonschema
Requires: keyring
Requires: pytest
Requires: pytest-cov
BuildRequires : jsonschema-python
BuildRequires : keyring-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=====
        
        A built-package format for Python.
        
        A wheel is a ZIP-format archive with a specially formatted filename
        and the .whl extension. It is designed to contain all the files for a
        PEP 376 compatible install in a way that is very close to the on-disk
        format. Many packages will be properly installed with only the "Unpack"
        step (simply extracting the file onto sys.path), and the unpacked archive
        preserves enough information to "Spread" (copy data and scripts to their
        final locations) at any later time.
        
        The wheel project provides a `bdist_wheel` command for setuptools
        (requires setuptools >= 0.8.0). Wheel files can be installed with a

%package bin
Summary: bin components for the wheel package.
Group: Binaries

%description bin
bin components for the wheel package.


%package legacypython
Summary: legacypython components for the wheel package.
Group: Default

%description legacypython
legacypython components for the wheel package.


%package python
Summary: python components for the wheel package.
Group: Default
Requires: wheel-legacypython

%description python
python components for the wheel package.


%prep
%setup -q -n wheel-0.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505144916
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505144916
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wheel

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
