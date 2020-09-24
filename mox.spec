#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mox
Version  : 0.5.3
Release  : 25
URL      : http://pypi.debian.net/mox/mox-0.5.3.tar.gz
Source0  : http://pypi.debian.net/mox/mox-0.5.3.tar.gz
Summary  : Mock object framework
Group    : Development/Tools
License  : Apache-2.0
Requires: mox-license = %{version}-%{release}
Requires: mox-python = %{version}-%{release}
Requires: mox-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Mox is an open source mock object framework for Python, inspired by
the Java library EasyMock.

%package license
Summary: license components for the mox package.
Group: Default

%description license
license components for the mox package.


%package python
Summary: python components for the mox package.
Group: Default
Requires: mox-python3 = %{version}-%{release}

%description python
python components for the mox package.


%package python3
Summary: python3 components for the mox package.
Group: Default
Requires: python3-core
Provides: pypi(mox)

%description python3
python3 components for the mox package.


%prep
%setup -q -n mox-0.5.3
cd %{_builddir}/mox-0.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583174219
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mox
cp %{_builddir}/mox-0.5.3/COPYING %{buildroot}/usr/share/package-licenses/mox/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mox/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
