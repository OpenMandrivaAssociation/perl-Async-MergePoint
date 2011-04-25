%define upstream_name    Async-MergePoint
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Resynchronise diverged control flow
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Async/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Often in program logic, multiple different steps need to be taken that are
independent of each other, but their total result is needed before the next
step can be taken. In synchonous code, the usual approach is to do them
sequentially.

An asynchronous or event-based program could do this, but if each step
involves some IO idle time, better overall performance can often be gained
by running the steps in parallel. A 'Async::MergePoint' object can then be
used to wait for all of the steps to complete, before passing the combined
result of each step on to the next stage.

A merge point maintains a set of outstanding operations it is waiting on;
these are arbitrary string values provided at the object's construction.
Each time the 'done()' method is called, the named item is marked as being
complete. When all of the required items are so marked, the 'on_finished'
continuation is invoked.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


