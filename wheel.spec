#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.26.0
Release  : 18
URL      : https://pypi.python.org/packages/source/w/wheel/wheel-0.26.0.tar.gz
Source0  : https://pypi.python.org/packages/source/w/wheel/wheel-0.26.0.tar.gz
Summary  : A built-package format for Python.
Group    : Development/Tools
License  : MIT
Requires: wheel-bin
Requires: wheel-python
BuildRequires : jsonschema-python
BuildRequires : keyring-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : wheel-python

%description
Wheel
=====
A built-package format for Python.
A wheel is a ZIP-format archive with a specially formatted filename
and the .whl extension. It is designed to contain all the files for a
PEP 376 compatible install in a way that is very close to the on-disk
format. Many packages will be properly installed with only the "Unpack"
step (simply extracting the file onto sys.path), and the unpacked archive
preserves enough information to "Spread" (copy data and scripts to their
final locations) at any later time.

%package bin
Summary: bin components for the wheel package.
Group: Binaries

%description bin
bin components for the wheel package.


%package python
Summary: python components for the wheel package.
Group: Default
Requires: keyring-python

%description python
python components for the wheel package.


%prep
%setup -q -n wheel-0.26.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
sed -i -e s/--cov=wheel// setup.cfg  ; pushd py2; py.test; popd
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wheel

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
