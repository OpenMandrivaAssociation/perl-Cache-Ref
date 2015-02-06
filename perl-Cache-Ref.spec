%define upstream_name    Cache-Ref
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	This module implements in memory caching
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Hash::Util::FieldHash::Compat)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(ok)
BuildArch:	noarch

%description
Unlike the CHI manpage which attempts to address the problem of caching
things persistently, this module implements in memory caching, designed
primarily for *shared references* in memory.

This collection of classes implements a number of semi related algorithms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 656885
- rebuild for updated spec-helper

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 595078
- update to new version 0.04

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 563308
- import perl-Cache-Ref


* Wed Jul 14 2010 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
