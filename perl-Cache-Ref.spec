%define upstream_name    Cache-Ref
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Hash::Util::FieldHash::Compat)
BuildRequires: perl(List::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::Role::Parameterized)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Moose)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(ok)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Unlike the CHI manpage which attempts to address the problem of caching
things persistently, this module implements in memory caching, designed
primarily for *shared references* in memory.

This collection of classes implements a number of semi related algorithms.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


