Name:		python-lxml
Version:	4.9.2
Release:	1
Summary:	ElementTree-like Python bindings for libxml2 and libxslt
Group:		Development/Python
License:	BSD
URL:		http://lxml.de
Source0:	https://files.pythonhosted.org/packages/source/l/lxml/lxml-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python-setuptools
#BuildRequires:	python3dist(cython)
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

%prep
%autosetup -n lxml-%{version} -p1
# Remove pregenerated Cython C sources
#find -type f -name '*.c' -print -delete

%build
%py_build -- --without-cython

%install
%py_install

%files
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%files docs
%doc doc/*
