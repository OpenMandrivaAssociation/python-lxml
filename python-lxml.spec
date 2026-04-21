%define module lxml

Name:		python-lxml
Version:	6.1.0
Release:	2
Summary:	ElementTree-like Python bindings for libxml2 and libxslt
Group:		Development/Python
License:	BSD
URL:		https://lxml.de
Source0:	https://files.pythonhosted.org/packages/source/l/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(cssselect)

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

%prep -a
# Remove pregenerated Cython C sources
find -type f -name '*.c' -print -delete

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%files
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info

%files docs
%doc doc/*
