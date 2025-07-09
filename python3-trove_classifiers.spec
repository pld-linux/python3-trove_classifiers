#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	trove_classifiers
Summary:	Canonical source for classifiers on PyPI
Summary(pl.UTF-8):	Kanoniczne źródła dla klasyfikatorów na PyPi
Name:		python3-%{module}
Version:	2025.5.9.12
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/trove-classifiers/
Source0:	https://files.pythonhosted.org/packages/source/t/trove-classifiers/trove_classifiers-%{version}.tar.gz
# Source0-md5:	382d0838616b5078d21596cd1cd0eeb2
URL:		https://pypi.org/project/trove-classifiers/
BuildRequires:	python3-build
BuildRequires:	python3-calver
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
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
# test_entry_point,test_module_run_is_entry_point require /usr/bin/trove-classifiers
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests -k 'not test_entry_point and not test_module_run_is_entry_point'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/trove-classifiers
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
