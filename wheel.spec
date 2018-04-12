#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.31.0
Release  : 40
URL      : http://pypi.debian.net/wheel/wheel-0.31.0.tar.gz
Source0  : http://pypi.debian.net/wheel/wheel-0.31.0.tar.gz
Summary  : A built-package format for Python.
Group    : Development/Tools
License  : MIT
Requires: wheel-bin
Requires: wheel-python3
Requires: wheel-python
Requires: keyring
Requires: pyxdg
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


%package python
Summary: python components for the wheel package.
Group: Default
Requires: wheel-python3

%description python
python components for the wheel package.


%package python3
Summary: python3 components for the wheel package.
Group: Default
Requires: python3-core

%description python3
python3 components for the wheel package.


%prep
%setup -q -n wheel-0.31.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523552667
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
