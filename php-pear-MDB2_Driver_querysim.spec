%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	MDB2_Driver_querysim
Summary:	%{_pearname} - querysim MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik querysim dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	4
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e4f515fcff4e8ea111cd995ade51135a
URL:		http://pear.php.net/package/MDB2_Driver_querysim/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.3.0
Requires:	php-pear-MDB2 >= 2.3.0
Obsoletes:	php-pear-MDB2_Driver_querysim-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Querysim MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik Querysim dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/MDB2/Driver/Datatype/querysim.php

%{php_pear_dir}/data/%{_pearname}
