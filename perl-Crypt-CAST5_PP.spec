#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%define		pdir	Crypt
%define		pnam	CAST5_PP
Summary:	Crypt::CAST5_PP Perl module - CAST5 block cipher implemented in pure Perl
Summary(pl.UTF-8):	Moduł Perla Crypt::CAST5_PP - szyfr blokowy CAST5 zaimplementowany w samym Perlu
Name:		perl-Crypt-CAST5_PP
Version:	1.04
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	563d7ecad9193fe442cf1fe0b1da1a97
URL:		http://search.cpan.org/dist/Crypt-CAST5_PP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Test-Simple >= 0.1
BuildRequires:	rpm-perlprov >= 4.1-13
Provides:	perl(Crypt::CAST5_PP::Tables)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a pure Perl implementation of the CAST5 block
cipher. CAST5 is also known as CAST-128. It is a product of the CAST
design procedure developed by C. Adams and S. Tavares. The CAST5
cipher is available royalty-free.

%description -l pl.UTF-8
Ten moduł zawiera implementację szyfru blokowego CAST5 napisaną w
samym Perlu. CAST5 jest znany także jako CAST-128 i jest produktem
procesu projektowania CAST, tworzonego przez C. Adamsa i S. Tavaresa.
Szyfr CAST5 jest dostępny bezpłatnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/CAST5_PP.pm
%{perl_vendorlib}/Crypt/CAST5_PP
%dir %{perl_vendorlib}/auto/Crypt/CAST5_PP
%{perl_vendorlib}/auto/Crypt/CAST5_PP/autosplit.ix
%{perl_vendorlib}/auto/Crypt/CAST5_PP/*.al
%{_mandir}/man3/*
