%define upstream_name    Async-MergePoint
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Resynchronise diverged control flow
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Async/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Thu Jun 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 682532
- update to new version 0.04

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2
+ Revision: 658516
- rebuild for updated spec-helper

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 394978
- update to 0.03

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 390462
- import perl-Async-MergePoint


* Mon Jun 29 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

