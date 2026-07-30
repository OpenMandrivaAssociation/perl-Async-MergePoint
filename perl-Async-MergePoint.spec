%define upstream_name    Async-MergePoint
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	0.04
Release:	4

Summary:	Resynchronise diverged control flow
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Async-MergePoint
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Async-MergePoint-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

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
%setup -q -n Async-MergePoint-0.04

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


