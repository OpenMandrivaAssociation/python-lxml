%define modname lxml
%define pyver %(python -V 2>&1 | cut -f2 -d" " | cut -f1,2 -d".")

Name:           python-%{modname}
URL:            http://codespeak.net/lxml/
Summary:        A Pythonic binding for the libxml2 and libxslt libraries
Version:        2.1.1
Release:        %mkrel 1
License:        BSD
Group:          Development/Python
Source:         http://codespeak.net/lxml/%{modname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:       python

BuildRequires:  libxml2-devel libxslt-devel python-pyrex python-devel

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

export PYTHONPATH="$RPM_BUILD_ROOT%{_libdir}/python%{pyver}/site-packages"

%install
# -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && rm -rf  %{buildroot}

%files
%defattr(-,root,root)
%doc doc CHANGES.txt CREDITS.txt LICENSES.txt README.txt TODO.txt
%py_platsitedir/lxml*


