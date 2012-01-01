Name:           perl-Test-Warn
Version:        0.21
Release:        2%{?dist}
Summary:        Perl extension to test methods for warnings

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Warn/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Test-Warn-%{version}.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Uplevel) >= 0.12
BuildRequires:  perl(Test::Builder) >= 0.13
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Tree::DAG_Node)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Test::Builder) >= 0.13
Requires:       perl(Test::Builder::Tester) >= 1.02
Requires:       perl(Tree::DAG_Node)

%{?perl_default_filter}

%description
This module provides a few convenience methods for testing warning
based code.


%prep
%setup -q -n Test-Warn-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Tue Dec 22 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.21-2
- Compare::Array is not needed anymore
- Resolves: rhbz#549719 

* Fri Sep 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- add perl default filter (pro forma)
- use _fixperms incantation
- auto-update to 0.21 (by cpan-spec-update 0.01)
- altered br on perl(Test::Builder::Tester) (0 => 1.02)
- altered req on perl(Test::Builder::Tester) (0 => 1.02)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Paul Howarth <paul@city-fan.org> - 0.11-1
- Update to 0.11 (#477298)
- Buildreq ExtUtils::MakeMaker, File::Spec, Test::Builder,
  Test::Builder::Tester, and Test::More (from upstream Makefile.PL)
- Add runtime dependencies on Test::Builder and Test::Builder::Tester

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10-3
- Rebuild for perl 5.10 (again)

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.10-2
- rebuild for new perl

* Sat May  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.10-1
- Update to 0.10.

* Sun Mar 18 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.09-1
- Update to 0.09.
- New upstream maintainer.
- New BR: perl(Test::Pod).

* Sun Sep 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.08-4
- Rebuild for FC6.

* Fri Feb 24 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.08-3
- Rebuild for FC5 (perl 5.8.8).

* Fri Jul  1 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.08-2
- Dist tag.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.08-0.fdr.1
- First build.
