# Conditional build:
%bcond_without	tests	# unit tests

%define		module	trove_classifiers
Summary:	Canonical source for classifiers on PyPI
Summary(pl.UTF-8):	Kanoniczne źródła dla klasyfikatorów na PyPi
Name:		python3-%{module}
Version:	2025.1.15.22
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://pypi.debian.net/trove-classifiers/trove_classifiers-%{version}.tar.gz
# Source0-md5:	3656424a10a761108fa8250033ffe3d4
URL:		https://pypi.org/project/trove-classifiers/
BuildRequires:	python3-calver
BuildRequires:	python3-modules >= 1:3.2
#BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

%description -l pl.UTF-8
Klasyfikatory kategoryzują projekty zgodnie z PEP 301. Tego pakietu
można użyć do sprawdzenia poprawności klasyfikatorów w pakietach przy
wysyłaniu lub pobieraniu z PyPi.

%prep
%setup -q -n trove_classifiers-%{version}

%build
%py3_build_pyproject

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
