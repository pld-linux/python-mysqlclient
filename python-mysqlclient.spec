# Conditional build:
%define		module	mysqlclient
Summary:	A Python interface to MySQL (MySQLdb compatible)
Summary(pl.UTF-8):	Interfejs Pythona do MySQL (kompatybilny z MySQLdb)
Name:		python-%{module}
Version:	1.3.6
Release:	5
License:	GPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/m/mysqlclient/mysqlclient-%{version}.tar.gz
# Source0-md5:	58d7c9c617a4286a88db290e7857d3aa
URL:		https://pypi.python.org/pypi/mysqlclient
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-modules
Provides:	python-MySQLdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlclient is a fork of MySQL-python. It adds Python 3.3 support and
merges some pull requests.

MySQLdb is an interface to the popular MySQL database server for
Python.

%description -l pl.UTF-8
mysqlclient to fork MySQL-python. Dodaje obsługę Pythona 3.3 oraz
nakłada kilka patchy.

MySQLdb to pythonowy interfejs do MySQL-a.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py?
%dir %{py_sitedir}/MySQLdb
%{py_sitedir}/MySQLdb/*.py?
%dir %{py_sitedir}/MySQLdb/constants
%{py_sitedir}/MySQLdb/constants/*.py?
%{py_sitedir}/*.egg-info
