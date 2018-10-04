#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wheel
Version  : 0.32.1
Release  : 54
URL      : https://files.pythonhosted.org/packages/e2/d0/bb5eedd650e777039d984b209d229b97fa2161916c920245a85c1ef07667/wheel-0.32.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/d0/bb5eedd650e777039d984b209d229b97fa2161916c920245a85c1ef07667/wheel-0.32.1.tar.gz
Summary  : A built-package format for Python.
Group    : Development/Tools
License  : MIT
Requires: wheel-bin
Requires: wheel-python3
Requires: wheel-license
Requires: wheel-python
Requires: keyring
BuildRequires : buildreq-distutils3
BuildRequires : jsonschema-python
BuildRequires : keyring

%description
=====
        
        This library is the reference implementation of the Python wheel packaging
        standard, as defined in `PEP 427`_.

%package bin
Summary: bin components for the wheel package.
Group: Binaries
Requires: wheel-license = %{version}-%{release}

%description bin
bin components for the wheel package.


%package license
Summary: license components for the wheel package.
Group: Default

%description license
license components for the wheel package.


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

%description python3
python3 components for the wheel package.


%prep
%setup -q -n wheel-0.32.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538661587
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/wheel
cp LICENSE.txt %{buildroot}/usr/share/doc/wheel/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wheel

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/wheel/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
