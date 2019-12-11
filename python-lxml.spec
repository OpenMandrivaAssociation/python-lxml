%bcond_without python2

Name:		python-lxml
Version:	4.4.1
Release:	2
Summary:	ElementTree-like Python bindings for libxml2 and libxslt
Group:		Development/Python
License:	BSD
URL:		http://lxml.de
Source0:	https://files.pythonhosted.org/packages/c4/43/3f1e7d742e2a7925be180b6af5e0f67d38de2f37560365ac1a0b9a04c015/lxml-4.4.1.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	libxslt-devel
%if %{with python2}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-distribute
BuildRequires:	python2-cython
%endif
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python-setuptools
Requires:	python-cssselect

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%package docs
Summary:	Documentation for %{name}
BuildArch:	noarch

%description docs
This package provides the documentation for %{name}, e.g. the API as html.

%if %{with python2}
%package -n python2-lxml
Summary:	ElementTree-like Python 2 bindings for libxml2 and libxslt

%description -n python2-lxml
lxml provides a Python 2 binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.
%endif

%prep
%setup -q -n lxml-%{version}

%if 0%{?with_python2}
rm -rf ../py2
cp -r . ../py2
%endif

%build
CFLAGS="%{optflags}" python setup.py build --without-cython

%if %{with python2}
pushd ../py2
CFLAGS="%{optflags}" python2 setup.py build --without-cython
popd
%endif

%install
rm -rf %{buildroot}
python setup.py install --skip-build --no-compile --without-cython --root %{buildroot}

%if %{with python2}
pushd ../py2
python2 setup.py install --skip-build --no-compile --without-cython --root %{buildroot}
popd
%endif

%files
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%files docs
%doc doc/*

%if %{with python2}
%files -n python2-lxml
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python2_sitearch}/lxml-*.egg-info
%{python2_sitearch}/lxml
%endif
