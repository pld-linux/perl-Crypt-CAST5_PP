#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CAST5_PP
Summary:	Crypt::CAST5_PP Perl module - CAST5 block cipher implemented in pure Perl
Summary(pl):	Modu³ Perla Crypt::CAST5_PP - szyfr blokowy CAST5 zaimplementowany w samym Perlu
Name:		perl-Crypt-CAST5_PP
Version:	1.02
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Test-Simple >= 0.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
Provides:	perl(Crypt::CAST5_PP::Tables)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a pure Perl implementation of the CAST5 block
cipher. CAST5 is also known as CAST-128. It is a product of the CAST
design procedure developed by C. Adams and S. Tavares. The CAST5
cipher is available royalty-free.

%description -l pl
Ten modu³ zawiera implementacjê szyfru blokowego CAST5 napisan± w
samym Perlu. CAST5 jest znany tak¿e jako CAST-128 i jest produktem
procesu projektowania CAST, tworzonego przez C. Adamsa i S. Tavaresa.
Szyfr CAST5 jest dostêpny bezp³atnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/CAST5_PP.pm
%{perl_sitelib}/Crypt/CAST5_PP
%dir %{perl_sitelib}/auto/Crypt/CAST5_PP
%{perl_sitelib}/auto/Crypt/CAST5_PP/autosplit.ix
%{perl_sitelib}/auto/Crypt/CAST5_PP/*.al
%{_mandir}/man3/*
