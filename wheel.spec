#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.29.0
Release  : 20
URL      : https://pypi.python.org/packages/source/w/wheel/wheel-0.29.0.tar.gz
Source0  : https://pypi.python.org/packages/source/w/wheel/wheel-0.29.0.tar.gz
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
%setup -q -n wheel-0.29.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

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
