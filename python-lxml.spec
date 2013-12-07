%define modname lxml

Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Name:		python-%{modname}
Version:	3.2.3
Release:	3
License:	BSD
Group:		Development/Python
Url:		http://codespeak.net/lxml/
Source0:	http://pypi.python.org/packages/source/l/lxml/lxml-%{version}.tar.gz
BuildRequires:	python-cython
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(python)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It follows
the ElementTree API as much as possible, building it on top of the native
libxml2 tree. It also extends this API to expose libxml2 and libxslt specific
functionality, such as XPath, Relax NG, XML Schema, XSLT, and c14n.

%package -n python3-%{modname}
Summary:	A Pythonic binding for the libxml2 and libxslt libraries
Group:		Development/Python
BuildRequires:	python3-devel
BuildRequires:	pkgconfig(python3)

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It follows
the ElementTree API as much as possible, building it on top of the native
libxml2 tree. It also extends this API to expose libxml2 and libxslt specific
functionality, such as XPath, Relax NG, XML Schema, XSLT, and c14n.

%package docs
Summary:	Documentation for %{name}
Group:		Development/Python

%description docs
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It follows
the ElementTree API as much as possible, building it on top of the native
libxml2 tree. It also extends this API to expose libxml2 and libxslt specific
functionality, such as XPath, Relax NG, XML Schema, XSLT, and c14n.

This package contains the documentation. The documentation is located in
%{_docdir}/%{name}/doc.

%prep
%setup -q -c
mv %{modname}-%{version} python2
cp -r python2 python3

%build

pushd python2
%{__python} setup.py build --with-cython
popd

pushd python3
%{__python3} setup.py build --with-cython
popd

%install
pushd python2
%{__python} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

#docs
mkdir -p %{buildroot}%{_docdir}/%{name}/doc
cp -r python2/doc/* %{buildroot}%{_docdir}/%{name}/doc

%files
%doc python2/CHANGES.txt python2/CREDITS.txt python2/LICENSES.txt python2/README.rst python2/TODO.txt
%{py_platsitedir}/lxml*
%exclude %{_docdir}/%{name}/doc

%files -n python3-%{modname}
%doc python3/CHANGES.txt python3/CREDITS.txt python3/LICENSES.txt python3/README.rst python3/TODO.txt
%{py3_platsitedir}/lxml*
%exclude %{_docdir}/%{name}/doc

%files docs
%doc %{_docdir}/%{name}/doc

