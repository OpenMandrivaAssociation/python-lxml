%bcond_without python2

Name:		python-lxml
Version:	4.7.1
Release:	1
Summary:	ElementTree-like Python bindings for libxml2 and libxslt
Group:		Development/Python
License:	BSD
URL:		http://lxml.de
Source0:	https://files.pythonhosted.org/packages/84/74/4a97db45381316cd6e7d4b1eb707d7f60d38cb2985b5dfd7251a340404da/lxml-4.7.1.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(libxslt)
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

%build
CFLAGS="%{optflags}" python setup.py build --without-cython

%install
python setup.py install --skip-build --no-compile --without-cython --root %{buildroot}

%files
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%files docs
%doc doc/*
