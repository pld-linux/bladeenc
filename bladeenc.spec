Summary:	Blade's MP3 Encoder
Summary(pl):	Encoder MP3 Blade'a
Name:		bladeenc
Version:	0.91
Release:	2
Epoch:		1
Copyright:	LGPL
Vendor:		Tord Jansson <tord.jansson@swipnet.se>
Group:		Applications/Sound
Group(pl):	Aplikacje/D¼wiêk
Source:		http://bladeenc.mp3.no/source/bladeenc-%{version}-src-stable.tar.gz
URL:		http://bladeenc.mp3.no/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	BladeEnc

%description
BladeEnc is a program to generate MP3 files from WAV or AIFF sound files.

%description -l pl
BladeEnc jest programem s³u¿±cym do generowania plików MP3 z plików
d¼wiêkowych w formacie WAV lub AIFF.

%prep
%setup -q -n %{name}-%{version}.0

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make 

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9fn README TODO ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,ChangeLog,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/*
