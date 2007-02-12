Summary:	Blade's MP3 Encoder
Summary(pl.UTF-8):   Koder MP3 Blade'a
Name:		bladeenc
Version:	0.94.2
Release:	6
Epoch:		1
License:	GPL
Vendor:		Tord Jansson <tord.jansson@swipnet.se>
Group:		Applications/Sound
Source0:	http://bladeenc.mp3.no/source/%{name}-%{version}-src-stable.tar.gz
# Source0-md5:	9b9f6eafe1637a48a67f0a0f8f6e71ad
Patch0:		%{name}-fseek-sec.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://bladeenc.mp3.no/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	BladeEnc

%description
BladeEnc is a program to generate MP3 files from WAV or AIFF sound
files.

%description -l pl.UTF-8
BladeEnc jest programem służącym do generowania plików MP3 z plików
dźwiękowych w formacie WAV lub AIFF.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
