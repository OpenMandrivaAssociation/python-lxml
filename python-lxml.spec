%define modname lxml

Name:           python-%{modname}
URL:            http://codespeak.net/lxml/
Summary:        A Pythonic binding for the libxml2 and libxslt libraries
Version:        2.2.8
Release:        %mkrel 2
License:        BSD
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/l/lxml/%{modname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  python-devel
BuildRequires:  libxml2-devel libxslt-devel python-pyrex

%description
lxml is a Pythonic binding for the libxml2 and libxslt libraries. It follows
the ElementTree API as much as possible, building it on top of the native
libxml2 tree. It also extends this API to expose libxml2 and libxslt specific
functionality, such as XPath, Relax NG, XML Schema, XSLT, and c14n.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
%{__python} setup.py build

export PYTHONPATH="%{buildroot}%{_libdir}/python%{pyver}/site-packages"

%install
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf  %{buildroot}

%files
%defattr(-,root,root)
%doc doc CHANGES.txt CREDITS.txt LICENSES.txt README.txt TODO.txt
%py_platsitedir/lxml*
