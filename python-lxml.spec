%define modname lxml

Name:           python-%{modname}
URL:            http://codespeak.net/lxml/
Summary:        A Pythonic binding for the libxml2 and libxslt libraries
Version:        2.3.4
Release:        1
License:        BSD
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/l/lxml/%{modname}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python-pyrex
BuildRequires:  python-setuptools

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
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
%{__python} setup.py build

export PYTHONPATH="%{buildroot}%{_libdir}/python%{pyver}/site-packages"

%install
%{__python} setup.py install --root=%{buildroot}

#docs
mkdir -p %{buildroot}%{_docdir}/%{name}/doc
cp -r doc/* %{buildroot}%{_docdir}/%{name}/doc

%clean
rm -rf  %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES.txt CREDITS.txt LICENSES.txt README.rst TODO.txt
%exclude %{_docdir}/%{name}/doc
%py_platsitedir/lxml*

%files docs
%defattr(-,root,root)
%doc %{_docdir}/%{name}/doc
