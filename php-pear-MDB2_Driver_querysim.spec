%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_querysim
%define		_status		alpha
%define		_pearname	MDB2_Driver_querysim

Summary:	%{_pearname} - querysim MDB2 driver
Summary(pl):	%{_pearname} - sterownik querysim dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	50dff3867f5f1eabfae547cf0eb65ec7
URL:		http://pear.php.net/package/MDB2_Driver_querysim/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.3.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0beta6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Querysim MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
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
%{php_pear_dir}/package_querysim.php
