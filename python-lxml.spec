%bcond_without python2

Name:           python-lxml
Version:        3.3.5
Release:        1
Summary:        ElementTree-like Python bindings for libxml2 and libxslt


License:        BSD
URL:            http://lxml.de
Source0:        http://lxml.de/files/lxml-%{version}.tgz
Source1:        http://lxml.de/files/lxml-%{version}.tgz.asc
Source2:        %{name}.rpmlintrc

BuildRequires:  libxslt-devel

%if %{with python2}
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-distribute
BuildRequires:  python2-cython >= 0.17.1
%endif

BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:	python-cython >= 0.20.2-2

Requires:       python-cssselect

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
This package provides the documentation for %{name}, e.g. the API as html.

%if %{with python2}
%package -n python2-lxml
Summary:        ElementTree-like Python 2 bindings for libxml2 and libxslt


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

# remove the C extension so that it will be rebuilt using the latest Cython
rm -f src/lxml/lxml.etree.c
rm -f src/lxml/lxml.etree.h
rm -f src/lxml/lxml.etree_api.h
rm -f src/lxml/lxml.objectify.c

chmod a-x doc/rest2html.py
%{__sed} -i 's/\r//' doc/s5/ui/default/print.css \
    doc/s5/ep2008/atom.rng \
    doc/s5/ui/default/iepngfix.htc

%if 0%{?with_python2}
rm -rf ../py2
cp -r . ../py2
%endif

%build
CFLAGS="%{optflags}" python setup.py build --with-cython

%if %{with python2}
cp src/lxml/lxml.etree.c ../py2/src/lxml
cp src/lxml/lxml.etree.h ../py2/src/lxml
cp src/lxml/lxml.etree_api.h ../py2/src/lxml
cp src/lxml/lxml.objectify.c ../py2/src/lxml

pushd ../py2
CFLAGS="%{optflags}" python2 setup.py build --with-cython
popd
%endif

%install
rm -rf %{buildroot}
python setup.py install --skip-build --no-compile --with-cython --root %{buildroot}

%if %{with python2}
pushd ../py2
python2 setup.py install --skip-build --no-compile --with-cython --root %{buildroot}
popd
%endif

%files
%defattr(-,root,root,-)
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%files docs
%defattr(-,root,root,-)
%doc doc/*

%if %{with python2}
%files -n python2-lxml
%defattr(-,root,root,-)
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt
%{python2_sitearch}/lxml-*.egg-info
%{python2_sitearch}/lxml
%endif
