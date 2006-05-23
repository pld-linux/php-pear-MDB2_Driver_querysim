%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_querysim
%define		_status		beta
%define		_pearname	MDB2_Driver_querysim

Summary:	%{_pearname} - querysim MDB2 driver
Summary(pl):	%{_pearname} - sterownik querysim dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	772ebc9a0b4e2d4f9712539a190c5c43
URL:		http://pear.php.net/package/MDB2_Driver_querysim/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-common >= 3:4.3.0
Requires:	php-pear-PEAR-core >= 1:1.0b1
Requires:	php-pear-MDB2 >= 1:2.0.0-0.RC1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Querysim MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik Querysim dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/querysim_readme.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/querysim.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
